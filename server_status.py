import psutil
import time
import os
import logging
from functools import wraps
import mysql.connector as connector


GB = (1024.0 ** 3)

db_server = os.environ.get('DB_SERVER')
db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASSWORD')
db_database = os.environ.get('DB_DATABASE')
db_port = os.environ.get('DB_PORT')

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Log Function calls


def log_function_call(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        logging.info(f'Calling function: {fn.__name__}')
        res = fn(*args, **kwargs)
        logging.info(f'return : {res}')
        return res
    return wrapper


@log_function_call
def get_disk_usage():
    disk_usage = psutil.disk_usage('/')
    total = round(disk_usage.total / GB, 2)
    used = round(disk_usage.used / GB, 2)
    free = round(disk_usage.free / GB, 2)
    logging.info(
        f"Disk Usage: \nTotal: {total } GB \nUsed: {used} GB \nFree: {free} GB")
    return {'total': disk_usage.total, 'used': disk_usage.used, 'free': disk_usage.free}


@log_function_call
def get_memory_usage():
    memory_usage = psutil.virtual_memory()
    total = round(memory_usage.total / GB, 3)
    used = round(memory_usage.used / GB, 3)
    free = round(memory_usage.available / GB, 3)
    print(memory_usage)
    logging.info(
        f"Memory Usage: \nTotal: {total } GB \nUsed: {used} GB \nFree: {free} GB")
    return {'total': memory_usage.total, 'used': memory_usage.used, 'free': memory_usage.available}


@log_function_call
def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    logging.info(f"Cpu Usage: {cpu_usage}%")
    return cpu_usage


if __name__ == "__main__":
    try:
        connection = connector.connect(
            host=db_server, database=db_database, user=db_user, password=db_pass, port=db_port)
        if connection.is_connected():
            db_info = connection.get_server_info()
            cursor = connection.cursor()
            logging.info(f"Connected to MySQL Server version {db_info}")

            timestamp = time.time()
            disk_usage = get_disk_usage()
            memory_usage = get_memory_usage()
            cpu_usage = get_cpu_usage()

            mySql_insert_query = """INSERT INTO statistics ( disk_total, disk_used, disk_free, memory_total, memory_used, memory_free, cpu, time) 
                            VALUES 
                            (%s, %s, %s, %s,%s, %s, %s, FROM_UNIXTIME(%s)) """

            record = (disk_usage.get('total'), disk_usage.get('used'), disk_usage.get('free'), memory_usage.get('total'),
                      memory_usage.get('used'), memory_usage.get('free'), cpu_usage, timestamp)
            cursor.execute(mySql_insert_query, record)
            connection.commit()
            logging.info(
                "Record inserted successfully into statistics_db table")

    except connector.Error as error:
        logging.error(f"Error while connecting to MySQL {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            logging.info("MySQL connection is closed")

