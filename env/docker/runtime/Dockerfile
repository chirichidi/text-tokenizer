FROM python:3-alpine

RUN apk update &&\
    apk upgrade &&\
    apk add --no-cache --virtual=build_deps g++ gfortran &&\
    pip install --no-cache-dir spacy
RUN python -m spacy download en_core_web_sm
RUN python -m spacy download es_core_news_sm
RUN python -m spacy download ja_core_news_sm
RUN apk del build_deps