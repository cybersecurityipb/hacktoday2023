FROM ubuntu:latest

RUN apt-get update && apt-get install -y socat
RUN groupadd -r ctf && useradd -r -g ctf ctf

WORKDIR /CTF
COPY flag.txt /CTF/flag.txt
COPY absen /CTF/absen

RUN chown -R ctf:ctf /CTF && \
    chmod 500 /CTF && \
    chmod 440 /CTF/flag.txt && \
    chmod 550 /CTF/absen

USER ctf 

CMD ["socat", "TCP-LISTEN:8000,reuseaddr,fork","EXEC:/CTF/absen,stderr"]

# docker build -t absen
# docker run -d -p 8000:8000 -it