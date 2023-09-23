FROM ubuntu:lunar

EXPOSE 5001

RUN useradd -m ctf

RUN apt update --fix-missing
RUN apt-get install -y socat

RUN mkdir /pwn
COPY debug.txt /pwn/debug.txt
COPY flag-random_taext_nono_linz_is_here_ulala.txt /flag-random_taext_nono_linz_is_here_ulala.txt
COPY release/nono /pwn/nono
WORKDIR /pwn

RUN chown -R 755 /pwn
RUN chmod 700 /usr/bin/* /bin/* /tmp /dev/shm
RUN chmod 755 /usr/bin/env /bin/dash /bin/bash /bin/sh /bin/cat /usr/bin/id /bin/ls
RUN chmod +x /pwn/nono


USER ctf
CMD ["/pwn/nono"]
