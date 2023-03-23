FROM logstash:7.16.3
USER root
RUN  mkdir /home/logstash
COPY mysql.tar.gz /home/logstash/mysql-connector-java-8.0.30.tar.gz
RUN tar -zxf /home/logstash/mysql-connector-java-8.0.30.tar.gz -C /home/logstash \
    && mv /home/logstash/mysql-connector-java-8.0.30 /home/logstash/mysql-connector-java
