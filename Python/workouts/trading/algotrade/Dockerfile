FROM python:3.10.0-slim-buster

WORKDIR /usr/scr/algotrade

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat

RUN pip install --upgrade pip
COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/scr/algotrade/entrypoint.sh
RUN chmod +x /usr/scr/algotrade/entrypoint.sh
COPY . .

ENTRYPOINT ["/usr/scr/algotrade/entrypoint.sh"]