FROM python:3.8-slim

EXPOSE 10000

WORKDIR /home

COPY . /home

RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update && pip3 install --upgrade pip

RUN pip3 install --upgrade pip

RUN pip3 install --trusted-host pypi.python.org -r /home/requirements.txt

CMD python3 /home/service.py
