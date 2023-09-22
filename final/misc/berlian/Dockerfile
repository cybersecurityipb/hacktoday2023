FROM ubuntu:latest

EXPOSE 5000

RUN apt update && apt upgrade -y && apt update --fix-missing
RUN apt install ruby socat -y
RUN mkdir /ctf

WORKDIR /ctf

COPY app.rb .
COPY flag.txt .

RUN chmod -R 755 /ctf
RUN chmod +x /ctf/app.rb
RUN chmod 766 /ctf/flag.txt

CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:/ctf/app.rb
