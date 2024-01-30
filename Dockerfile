FROM python:3.8-slim-buster


# set the worcking directory to 
WORKDIR /usr/app

# copy current directory content into the worcking dir
COPY . .

# install needed packages 
RUN pip install --no-cache-dir -r requirements.txt

# install cron
RUN apt-get update && apt-get install -y cron && apt-get install -y vim

# Give Execuation permission to the script 
RUN chmod +x server_status.py

ENV DB_SERVER=192.168.1.14
ENV DB_USER=root
ENV DB_PASSWORD=root
ENV DB_DATABASE=statistics_db
ENV DB_PORT=3306

# create the cron file and install it 
COPY cronfile /etc/cron.d/server_status-cron
RUN chmod 0644 /etc/cron.d/server_status-cron
RUN crontab /etc/cron.d/server_status-cron
RUN touch /var/log/cron.log

EXPOSE 8080


# Set the FLASK_APP environment variable
ENV FLASK_APP=app.py

CMD env >> /etc/environment && cron && flask run --host=0.0.0.0 --port=8080


