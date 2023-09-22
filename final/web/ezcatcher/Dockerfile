FROM python:3.10-slim-buster

RUN groupadd -r nobody
# RUN apt-get update -y \
#     && apt-get install python3 -y \
#     && apt install pip -y
    
WORKDIR /app    
COPY ./app /app
RUN pip3 install  --ignore-installed -r requirements.txt

COPY flag /flag-12893u9n1e981.txt
RUN chmod -R 747 /app
RUN chown -R root:nobody /flag-12893u9n1e981.txt
RUN chmod 444 /flag-12893u9n1e981.txt

USER nobody
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]