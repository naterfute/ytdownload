FROM python:3.10-alpine

WORKDIR /app

RUN apk add --no-cache ffmpeg \
    && apk add --virtual build-deps gcc python3-dev musl-dev postgresql-dev \
    && pip install --upgrade pip
COPY ./assets/app.py ./assets/downloader.py ./assets/db.py ./requirements.txt ./config.yaml /app/

RUN pip install --trusted-host pypi.python.org -r requirements.txt \
    && apk --purge del build-deps

EXPOSE 5000

ENV NAME World

CMD ["python", "app.py"]