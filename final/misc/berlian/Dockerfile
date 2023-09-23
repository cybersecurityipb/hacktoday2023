FROM ubuntu:16.04

EXPOSE 5000

RUN apt update && apt upgrade -y && apt update --fix-missing
RUN apt install ruby socat bsdmainutils -y
RUN mkdir /ctf
RUN useradd -m ctf

WORKDIR /ctf

COPY app.rb .
COPY flag.txt .

RUN chmod 777 /ctf
RUN chmod 755 /ctf/app.rb
RUN chmod 766 /ctf/flag.txt

CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:/ctf/app.rb,su=ctf
