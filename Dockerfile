FROM --platform=arm64 python:3.9.19-slim-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD uvicorn main:app --reload --host=0.0.0.0