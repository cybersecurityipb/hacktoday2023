FROM ubuntu:lunar

EXPOSE 19010

RUN apt update && apt upgrade -y && apt update --fix-missing
RUN apt-get install python3 socat -y

RUN mkdir /ctf
COPY src/chall.py /ctf/chall.py
COPY src/email.py /ctf/email.py
COPY src/flag.txt /ctf/flag.txt
WORKDIR /ctf

RUN chown -R 755 /ctf/
RUN chmod 700 /usr/bin/* /bin/* /tmp /dev/shm
RUN chmod 755 /usr/bin/env /usr/bin/python3 /bin/dash /bin/bash /bin/sh /bin/cat /usr/bin/groups /usr/bin/id /bin/ls
RUN chmod +x /ctf/chall.py

CMD socat TCP-LISTEN:19010,reuseaddr,fork EXEC:/ctf/chall.py,su=nobody