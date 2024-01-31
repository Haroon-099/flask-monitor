# flask-monitor

## DataBase

i used **MYSQL** as database for the application.
1. first create the volume to persists the mysql data 
  ``` docker volume create server_statistics_data ```
2. move the init.sql to database server, this file contains database inialization(cretae database, table and insert some data)
3. create and run the database container 
  ```bash 
  docker run -d \
  --name statistics-database \
  -p 3306:3306 \
  -e MYSQL_ROOT_PASSWORD=root \
  -e MYSQL_SSL_MODE=DISABLED \
  -v server_statistics_data:/var/lib/mysql \
  -v /path/to/init.sql:/docker-entrypoint-initdb.d/ \
  mysql:8.3.0
  ```
