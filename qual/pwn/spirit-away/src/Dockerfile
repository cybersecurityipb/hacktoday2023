FROM ubuntu:lunar

EXPOSE 8000

RUN apt update && apt upgrade -y && apt update --fix-missing
RUN apt-get install -y socat

RUN mkdir /pwn
COPY flag.txt /pwn/flag.txt
COPY spirit /pwn/spirit
WORKDIR /pwn

RUN chown -R 755 /pwn
RUN chmod 700 /usr/bin/* /bin/* /tmp /dev/shm
RUN chmod 755 /usr/bin/env /bin/dash /bin/bash /bin/sh /bin/cat /usr/bin/id /bin/ls
RUN chmod +x /pwn/spirit

CMD socat TCP-LISTEN:8000,reuseaddr,fork EXEC:/pwn/spirit,su=nobody