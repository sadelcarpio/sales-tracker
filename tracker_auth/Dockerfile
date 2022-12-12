FROM python:3.10-slim-buster

COPY . /app
WORKDIR /app

RUN apt-get update && apt-get install -y \
    dos2unix \
    libpq-dev \
    gcc && apt-get clean

RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["sh", "-c", "uvicorn main:app --port=${PORT} --host=0.0.0.0 --reload"]