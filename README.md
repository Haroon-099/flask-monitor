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
