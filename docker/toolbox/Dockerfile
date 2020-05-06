FROM python:3

MAINTAINER delanisGreg "gregdelanis@gmail.com"

# List packages here
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        file        \
        gcc         \
        libwww-perl && \
    apt-get autoremove -y && \
    apt-get clean
# Installing flask python
RUN apt-get install -qy python3
RUN apt-get install -qy python3-flask
# Upgrade pip
RUN pip install --upgrade pip

WORKDIR /usr/src/app

CMD [ "python", "app4.py" ]
