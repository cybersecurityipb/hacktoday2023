FROM ubuntu:jammy

EXPOSE 5000

ARG binary
ENV binary=${binary}

# update
RUN apt-get update && apt-get upgrade -y && apt-get update --fix-missing
RUN apt-get install -y python3 socat
RUN apt-get install -y python3-pip
RUN python3 -m pip install pycryptodome


# copy file
RUN mkdir /challs
COPY $binary /challs/$binary
COPY flag.txt /challs/flag.txt
COPY password.txt /challs/password.txt
COPY spam.txt /challs/spam.txt
WORKDIR /challs


# securing flag
RUN chmod -R 755 /challs/
RUN chmod 744 /challs/flag.txt


# securing environment
RUN chmod 700  /tmp /dev/shm
RUN chmod 755 /usr/bin/env /usr/bin/python3 /bin/dash /bin/bash /bin/sh /bin/cat /usr/bin/groups /usr/bin/id /bin/ls


# Run Program
CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:/challs/$binary,su=nobody
