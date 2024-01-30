import os
import logging
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import server_status as stats
from functools import wraps

app = Flask(__name__)

# mysql db configration settings
db_server = os.environ.get('DB_SERVER')
db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASSWORD')
db_database = os.environ.get('DB_DATABASE')
db_port = os.environ.get('DB_PORT')

db = SQLAlchemy()


# configure database connection
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{db_user}:{db_pass}@{db_server}:{db_port}/{db_database}"

# Disable modification tracking
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initializing Flask app with SQLAlchemy
db.init_app(app)

# Configure logging
logging.basicConfig(level=logging.DEBUG)


@app.before_request
def log_request_info():
    app.logger.info(f'Handling Request: {request.method} {request.url}')


def jsonify_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        resualt = fn(*args, **kwargs)
        return jsonify(resualt)
    return wrapper


@app.route("/all-statistics", methods=['GET'])
@jsonify_data
def all_statistics():
    all_statistics = Statistics.query.all()

    # Convert the query results to a list of dictionaries
    statistics_list = []
    for stat in all_statistics:
        statistics_list.append({
            'id': stat.id,
            'disk_total': stat.disk_total,
            'disk_used': stat.disk_used,
            'disk_free': stat.disk_free,
            'memory_total': stat.memory_total,
            'memory_used': stat.memory_used,
            'memory_free': stat.memory_free,
            'cpu': f'{stat.cpu} %',
            # Convert datetime to string
            'time': stat.time.strftime('%Y-%m-%d %H:%M:%S')
        })

    # Return the list of dictionaries as JSON
    return {'statistics': statistics_list}


@app.route('/cpu-usage-last-24', methods=['GET'])
@jsonify_data
def cpu_usage_last_24():
    # calculate datetime for 24 hours ago
    last_24_ago = calculate_last_24_hours()

    # Query Cpu usage for each hour in the last 24 hour
    cpu_usage_last_24 = (
        db.session.query(
            db.func.date_format(
                Statistics.time, '%Y-%m-%d %H:%i:%S').label('hour'),
            Statistics.cpu.label('cpu')
        )
        .filter(Statistics.time >= last_24_ago)
        .all()
    )

    cpu_usage_list = [{'hour': stat.hour, 'cpu usage': f"{stat.cpu}%"}
                      for stat in cpu_usage_last_24]

    return {'cpu_usage_last_24': cpu_usage_list}


@app.route('/disk-usage-last-24', methods=['GET'])
@jsonify_data
def disk_usage_last_24():
    # calculate datetime for 24 hours ago
    last_24_ago = calculate_last_24_hours()

    # Query disk usage for each hour in the last 24 hour
    disk_usage_last_24 = (
        db.session.query(
            db.func.date_format(
                Statistics.time, '%Y-%m-%d %H:%i:%S').label('hour'),
            Statistics.disk_free.label('disk_free'),
            Statistics.disk_used.label('disk_used'),
            Statistics.disk_total.label('disk_total')
        )
        .filter(Statistics.time >= last_24_ago)
        .all())

    disk_usage_list = [{stat.hour: {'disk total': f"{stat.disk_total}", 'disk used': f"{stat.disk_used}", 'disk free': f"{stat.disk_free}"}}
                       for stat in disk_usage_last_24]

    return {'disk usage last 24': disk_usage_list}


@app.route('/memory-usage-last-24', methods=['GET'])
@jsonify_data
def memory_usage_last_24():
    # calculate datetime for 24 hours ago
    last_24_ago = calculate_last_24_hours()

    # Query memory usage for each hour in the last 24 hour
    memory_usage_last_24 = (
        db.session.query(
            db.func.date_format(
                Statistics.time, '%Y-%m-%d %H:%i:%S').label('hour'),
            Statistics.memory_free.label('memory_free'),
            Statistics.memory_used.label('memory_used'),
            Statistics.memory_total.label('memory_total')
        )
        .filter(Statistics.time >= last_24_ago)
        .all())

    memory_usage_list = [{stat.hour: {'memory total': f"{stat.memory_total}", 'memory used': f"{stat.memory_used}", 'memory free': f"{stat.memory_free}"}}
                         for stat in memory_usage_last_24]

    return {'memory usage last 24': memory_usage_list}


@app.route('/current-cpu-usage', methods=['GET'])
@jsonify_data
def current_cpu_usage():
    cpu_usage = stats.get_cpu_usage()
    return {'cpu_usage': f'{cpu_usage}%'}


@app.route('/current-disk-usage', methods=['GET'])
@jsonify_data
def current_disk_usage():
    disk_usage = stats.get_disk_usage()
    return {'disk_usage': disk_usage}


@app.route('/current-memory-usage', methods=['GET'])
@jsonify_data
def current_memory_usage():
    return {'memory_usage': stats.get_memory_usage()}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)


@stats.log_function_call
def calculate_last_24_hours():
    return datetime.utcnow() - timedelta(hours=24)
# Creating Model class for statistics Table


class Statistics(db.Model):
    '''
        id BIGINT AUTO_INCREMENT PRIMARY KEY,
        disk_total BIGINT  NOT NULL,
        disk_used BIGINT  NOT NULL,
        disk_free BIGINT  NOT NULL,
        memory_total BIGINT  NOT NULL,
        memory_used BIGINT  NOT NULL,
        memory_free BIGINT  NOT NULL,
        cpu FLOAT NOT NULL,
        time  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    '''
    __tablename__ = 'statistics'
    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    disk_total = db.Column(db.BIGINT, nullable=False)
    disk_used = db.Column(db.BIGINT, nullable=False)
    disk_free = db.Column(db.BIGINT, nullable=False)
    memory_total = db.Column(db.BIGINT, nullable=False)
    memory_used = db.Column(db.BIGINT, nullable=False)
    memory_free = db.Column(db.BIGINT, nullable=False)
    cpu = db.Column(db.FLOAT, nullable=False)
    time = db.Column(db.TIMESTAMP, nullable=False,
                     server_default=db.func.current_timestamp())

