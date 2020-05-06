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
RUN pip3 install --upgrade pip3

WORKDIR /usr/src/app
ADD app4.py app4.py
CMD [ "python", "app4.py" ]
