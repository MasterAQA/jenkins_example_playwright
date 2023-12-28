FROM python:3.10-slim

RUN apt-get -yqq update && apt-get -yqq upgrade

RUN apt-get install -yqq python3 \
                         python3-pip \
                         software-properties-common \
                         wget \
                         unzip
ADD . ./

RUN pip3 install -r ../requirements.txt
RUN python -m playwright install
RUN python -m playwright install-deps

WORKDIR /usr/src/
RUN touch .env