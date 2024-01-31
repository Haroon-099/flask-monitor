# flask-monitor

## DataBase

i used **MYSQL** as database for the application 
```bash 
docker run -d \
--name statistics-database \
-p 3306:3306 \
-e MYSQL_ROOT_PASSWORD=root \
-e MYSQL_SSL_MODE=DISABLED \
-v server_statistics_data:/var/lib/mysql \
-v /home/ansadmin/server_statistics/:/docker-entrypoint-initdb.d/ \
mysql:8.3.0
```
