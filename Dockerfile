FROM mcr.microsoft.com/playwright/python:v1.32.1-jammy
#FROM python:3.10.6

RUN apt-get -yqq update && apt-get -yqq upgrade

RUN apt-get install -yqq python3 \
                         python3-pip \
                         software-properties-common \
                         wget \
                         unzip
ADD . ./

RUN pip install --user -r requirements.txt
RUN python -m pip install --upgrade pip

RUN python -m pytest tests

#RUN pip install --user -r requirements.txt
#RUN python -m playwright install
#RUN python -m playwright install-deps
#
#RUN python pytest
