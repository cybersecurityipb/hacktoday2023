FROM ubuntu:focal

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -y update && apt-get install -y python3.10 curl socat python3-pip

RUN groupadd -r ctf && useradd -r -g ctf ctf
RUN mkdir /home/ctf
WORKDIR /home/ctf
COPY ./src ./src
WORKDIR /home/ctf/src
RUN curl -L https://bit.ly/451ZXYY > random.py
RUN pip3 install --upgrade pip
RUN pip3 install  --ignore-installed -r requirements.txt

COPY ./flag ./flag

RUN chown -R root:ctf ./flag/u/n/e/e/d/,/r/e/v/s/h/e/l/l/s/,/f/o/r/,/t/h/i/s/some_fl_ag_8200f96c-bf71-488e-9526-d8c41cc5a407
RUN chmod -R 440 ./flag/u/n/e/e/d/,/r/e/v/s/h/e/l/l/s/,/f/o/r/,/t/h/i/s/some_fl_ag_8200f96c-bf71-488e-9526-d8c41cc5a407

USER ctf
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
