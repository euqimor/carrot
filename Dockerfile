FROM python:3.6-alpine

WORKDIR /app

ADD . /app

RUN apk update \
    && apk add python3-dev \
    && apk add zlib-dev \
    && apk add musl-dev \
    && apk add gcc \
    && apk add jpeg-dev \
    && apk add freetype-dev \
    && apk add lcms2-dev \
    && apk add openjpeg-dev \
    && apk add tiff-dev \
    && apk add tk-dev \
    && apk add tcl-dev

RUN pip install -r requirements.txt

CMD ["carrot-web.py"]
