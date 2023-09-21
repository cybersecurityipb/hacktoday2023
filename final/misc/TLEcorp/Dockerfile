FROM ubuntu:lunar

EXPOSE 8000

RUN apt update && apt upgrade -y && apt update --fix-missing
RUN apt-get install -y socat

RUN mkdir /ctf
COPY source/chall /ctf/chall
WORKDIR /ctf

RUN chown -R 755 /ctf
RUN chmod +x /ctf/chall

CMD socat TCP-LISTEN:8000,reuseaddr,fork EXEC:/ctf/chall,su=nobody