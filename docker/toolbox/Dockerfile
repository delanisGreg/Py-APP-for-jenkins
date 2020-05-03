FROM ubuntu:18.04

MAINTANER delanisGreg "gregdelanis@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

RUN apk add --no-cache curl wget busybox-extras netcat-opensbd python py-pip
RUN pip install awscli

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app4.py" ]
