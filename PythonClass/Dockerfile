# docker build -t python-class .
# docker run -it --rm --name my-python-class -v "$PWD":/app -w /app python-class:latest
FROM ubuntu:latest
MAINTAINER Emad Najeeb "enajeeb@apple.com"
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev
#COPY requirements.txt /app/requirements.txt
#WORKDIR /app
#RUN pip3 install -r requirements.txt
#COPY . /app
#ENTRYPOINT ["python3", "app.py"]
