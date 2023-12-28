FROM python:3.10-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python -m pip install --upgrade playwright
RUN python -m pip install-deps --upgrade playwright

WORKDIR /usr/src/
RUN touch .env