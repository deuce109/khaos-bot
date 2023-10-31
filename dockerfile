FROM python:3.10
WORKDIR /app

ARG bot_token

RUN apt-get update && apt-get install -y python3-pip

COPY ./requirements.txt ./

RUN pip install -r ./requirements.txt
COPY ./ ./

ENV DISCORD_BOT_SECRET=${bot_token}

ENTRYPOINT [ "python", "main.py" ]