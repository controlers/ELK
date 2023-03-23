docker run --rm -it -v /data/elk/pipline/:/usr/share/logstash/pipeline/ logstash:7.16.3
docker run --rm -it -v /data/elk/settings/:/usr/share/logstash/config/ logstash:7.16.3
