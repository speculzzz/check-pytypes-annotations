FROM python:3.11-slim

RUN apt update && \
    apt upgrade && \
    apt install make

WORKDIR /challenges

COPY requirements.txt .

RUN python3 -m pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
