FROM ubuntu:focal

EXPOSE 5000

# update
RUN apt update && apt upgrade -y && apt update --fix-missing
RUN apt-get install python3 socat -y
RUN apt-get install -y python3-pip
RUN python3 -m pip install numpy
RUN python3 -m pip install z3-solver


# copy file
RUN mkdir /challs
COPY server.py /challs/server.py
COPY flag.txt /challs/flag.txt
WORKDIR /challs


# securing flag
RUN chmod -R 755 /challs/
RUN chmod 744 /challs/flag.txt
RUN chmod +x /challs/server.py


# securing environment
RUN chmod 700  /tmp /dev/shm
RUN chmod 755 /usr/bin/env /usr/bin/python3 /bin/dash /bin/bash /bin/sh /bin/cat /usr/bin/groups /usr/bin/id /bin/ls


# Run Program
CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:/challs/server.py,su=nobody