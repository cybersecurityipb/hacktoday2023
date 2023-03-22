FROM ubuntu:focal

EXPOSE 5000

ARG binary
ENV binary=${binary}

# update
RUN apt update && apt upgrade -y && apt update --fix-missing
RUN apt-get install python3 python3-pip socat -y
RUN pip3 install pycryptodome


# copy file
RUN mkdir /challs
COPY $binary /challs/$binary
COPY flag.txt /challs/flag.txt
COPY secret.py /challs/secret.py
WORKDIR /challs


# securing flag
RUN chmod -R 755 /challs/
RUN chmod 744 /challs/flag.txt


# securing environment
RUN chmod 700  /tmp /dev/shm
RUN chmod 755 /usr/bin/env /usr/bin/python3 /bin/dash /bin/bash /bin/sh /bin/cat /usr/bin/groups /usr/bin/id /bin/ls


# Run Program
CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:/challs/$binary,su=nobody
