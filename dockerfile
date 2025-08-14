FROM python:alpine
WORKDIR /app

RUN apk add py3-pip

COPY ./requirements.txt ./

RUN pip install -r ./requirements.txt
COPY ./bot ./bot
COPY ./main.py ./main.py
COPY ./docker-start.sh ./docker-start.sh

VOLUME /etc/ip-bot/

ENTRYPOINT [ "./docker-start.sh" ]