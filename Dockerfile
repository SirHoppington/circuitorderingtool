# Download base image
FROM ubuntu:20.04

#information about custom image

LABEL maintainer="nickhopgood@gmail.com"
LABEL version="0.1"
LABEL description="This is custom docker image for Flask with uwsgi and nginx."

# Disable Prompt During Packages Installation
ARG DEBIAN_FRONTEND=noninteractive

# Updata software repository
#RUN apt update

#Create a working directory for container to run

WORKDIR /usr/src/app

#COPY python requirements from Docker client

COPY requirements.txt ./

# Install python
RUN apt-get update \
  && apt-get install -y python3.6 python3-dev python3-distutils uuid-dev libcap-dev libpcre3-dev python3-pip gcc
RUN pip3 install --no-cache-dir -r requirements.txt

#COPY . .
#COPY . .
#COPY app.py .
#COPY wsgi.ini .

#CMD ["uwsgi", "wsgi.ini"]

## RUN commands or apps in container when it loads
#CMD ["/bin/bash"]

#CMD ["export", "FLASK_APP=app.py"]
#CMD ["flask", "run", "--host=0.0.0.0"]