FROM ubuntu:16.04

RUN apt-get -y update

RUN apt-get -y install \
  git \
  wget \
  python-dev \
  python-virtualenv

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
COPY ./listener.py .

RUN bin/pip install -r requirements.txt


EXPOSE 5000

ENTRYPOINT ["bin/python", "listener.py"]



