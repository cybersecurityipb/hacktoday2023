FROM ubuntu:lunar

EXPOSE 8000

RUN apt update && apt upgrade -y && apt update --fix-missing
RUN apt-get install -y socat

RUN mkdir /ctf
COPY server /ctf/server
WORKDIR /ctf

RUN chown -R 755 /ctf
RUN chmod +x /ctf/server

CMD socat TCP-LISTEN:8000,reuseaddr,fork EXEC:/ctf/server,su=nobody