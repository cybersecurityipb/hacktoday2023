FROM ubuntu:lunar

EXPOSE 5001

RUN apt update --fix-missing
RUN apt-get install -y socat

RUN mkdir /pwn
COPY flag.txt /pwn/flag.txt
COPY release/webserver /pwn/webserver
WORKDIR /pwn

RUN chown -R 755 /pwn
RUN chmod 700 /usr/bin/* /bin/* /tmp /dev/shm
RUN chmod 755 /usr/bin/env /bin/dash /bin/bash /bin/sh /bin/cat /usr/bin/id /bin/ls
RUN chmod +x /pwn/webserver

CMD socat TCP-LISTEN:5001,reuseaddr,fork EXEC:/pwn/webserver,su=nobody