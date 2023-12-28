FROM python:3.10-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python -m playwright install
RUN python -m playwright install-deps

WORKDIR /usr/src/
RUN touch .env