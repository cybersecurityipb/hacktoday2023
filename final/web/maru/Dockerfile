FROM ubuntu:focal

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -y update && apt-get install -y python3.10
RUN apt install socat -y
RUN apt install python3-pip -y

RUN groupadd -r ctf && useradd -r -g ctf ctf
RUN mkdir /home/ctf
WORKDIR /home/ctf
COPY ./src ./src
WORKDIR /home/ctf/src
RUN pip3 install --upgrade pip
RUN pip3 install  --ignore-installed -r requirements.txt
# dont forget make flag in bunch of folder
COPY ./flag ./flag
# should be redacted
RUN chown -R root:ctf ./flag/u/n/e/e/d/,/r/e/v/s/h/e/l/l/s/,/f/o/r/,/t/h/i/s/some_fl_ag_8200f96c-bf71-488e-9526-d8c41cc5a407
RUN chmod -R 440 ./flag/u/n/e/e/d/,/r/e/v/s/h/e/l/l/s/,/f/o/r/,/t/h/i/s/some_fl_ag_8200f96c-bf71-488e-9526-d8c41cc5a407

USER ctf
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]