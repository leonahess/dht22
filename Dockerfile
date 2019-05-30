FROM python:alpine
RUN apk add build-base

ADD smarthome_dht22.py .
ADD config.py .
ADD app ./app
ADD requirements.txt .

WORKDIR .

RUN pip3 install -r requirements.txt

CMD [ "python3", "smarthome_dht22.py" ]