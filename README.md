# flask-monitor

## Database

I used **MySQL** as the database for the application.

1. First, create the volume to persist the MySQL data.

    ```bash
    docker volume create server_statistics_data
    ```

2. Move the `init.sql` file to the database server. This file contains database initialization (create database, table, and insert some data).

3. Create and run the database container.

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

## Flask Application 

1. Pull the app image from Docker Hub.

    ```bash
    docker pull haroon1999/sever_statistics:v1
    ```

2. Create and run the container. You must provide these system environment variables:

   - `DB_SERVER`: the IP address for the database server
   - `DB_USER`: database username
   - `DB_PASSWORD`: database password
   - `DB_DATABASE`: database name
   - `DB_PORT`: database port number

    ```bash
    docker run -d \
    --name server_st \
    -e DB_SERVER="192.168.1.14" \
    -e DB_USER="root" \
    -e DB_PASSWORD="root" \
    -e DB_DATABASE="statistics_db" \
    -e DB_PORT=3306 \
    -p 8080:8080 \
    haroon1999/sever_statistics:v1
    ```
