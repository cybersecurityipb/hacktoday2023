FROM ubuntu:focal

RUN apt-get -y update && apt-get install -y python3.10
RUN apt install socat 

COPY ./src /src
COPY flag.txt /some_fl_ag_8200f96c-bf71-488e-9526-d8c41cc5a407
WORKDIR /src

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
