from python:3.10

RUN apt-get update

COPY ./requirements.txt ./requirements.txt
COPY ./prod_requirements.txt ./prod_requirements.txt

RUN pip3 install --upgrade pip && pip3 install -r requirements.txt
RUN pip3 install gunicorn
RUN pip3 install -r prod_requirements.txt

COPY ./ ./
