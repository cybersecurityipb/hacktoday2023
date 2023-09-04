FROM ubuntu:lunar

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install python3 -qy

COPY release /app
COPY flag /flag

USER 1000:1000

WORKDIR /app

EXPOSE 13337

CMD /app/ynetd -p 13337 "timeout 60 python3 -u ./runner.py 2>/dev/null"