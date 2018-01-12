FROM ubuntu:16.04

RUN apt-get -y update

RUN ["/bin/bash", "-c", "debconf-set-selections <<< 'mysql-server mysql-server/root_password password password'"]
RUN ["/bin/bash", "-c", "debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password password'"]

RUN apt-get -y install \
  git \
  wget \
  python-dev \
  python-virtualenv \
  mysql-server

WORKDIR /root

ENV PRODUCT listener

RUN wget https://bootstrap.pypa.io/get-pip.py \
  && python get-pip.py

WORKDIR eventAnalysis

RUN virtualenv ${PRODUCT}

WORKDIR ${PRODUCT}

RUN bin/pip install --upgrade pip && \
    bin/pip install requests[security]

COPY ./requirements.txt .
RUN bin/pip install -r requirements.txt

COPY ./listener.py .
COPY ./initDB.sh .
COPY ./createDB.txt .
COPY ./startup.sh .

EXPOSE 8080


RUN /bin/bash ./initDB.sh


#ENTRYPOINT ["bin/python", "listener.py"]

ENTRYPOINT ["/bin/bash", "startup.sh"]
#ENTRYPOINT  ["./startup.sh"]

