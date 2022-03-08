FROM ubuntu:latest
WORKDIR /flask
ENV AWS_SN='dev-ohio-phpapp-db.clbwywuriiqk.us-east-2.rds.amazonaws.com'
ENV AWS_UN='admin'
ENV AWS_PASSWORD='F14.tomcat!!'
ENV AWS_DBNAME='php_app'
COPY ./ /flask
EXPOSE 5000 3306
ENV FLASK_ENV=development
RUN apt update &&\
    apt install python3 -y &&\
    apt install python3-pip -y &&\
    pip3 install flask &&\
    apt install default-libmysqlclient-dev libssl-dev -y &&\
    pip3 install flask-mysqldb
    ENTRYPOINT ["python3"]
CMD [ "app.py" ]
