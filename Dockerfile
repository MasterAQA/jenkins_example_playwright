FROM python:3.10-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y \
    ttf-unifont \
    xfonts-cyrillic \
    ttf-ubuntu-font-family \
    libenchant1c2a \
    libicu66 \
    libjpeg-turbo8 \
    libvpx6 \
    libwebp6

COPY . .

RUN python -m playwright install
RUN python -m playwright install-deps

WORKDIR /usr/src/
RUN touch .env