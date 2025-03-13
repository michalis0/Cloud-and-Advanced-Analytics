# app/Dockerfile

FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

COPY ./main.py ./
COPY ./requirements.txt ./

RUN pip3 install -r requirements.txt


ENTRYPOINT ["python"]
CMD ["main.py"]
