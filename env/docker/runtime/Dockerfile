FROM ubuntu:latest

# apt init
ENV LANG=C.UTF-8
ENV TZ=Asia/Seoul
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y --no-install-recommends tzdata g++ git curl

# java stuff
RUN apt-get install -y openjdk-8-jdk

# python stuff
RUN apt-get install -y python3-pip python3-dev
RUN cd /usr/local/bin && \
    ln -s /usr/bin/python3 python && \
    ln -s /usr/bin/pip3 pip && \
    pip3 install --upgrade pip

# apt cleanse
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# timezone
RUN ln -sf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# workspace
RUN mkdir -p /workspace
WORKDIR /workspace

# install konlpy
RUN pip install konlpy
RUN cd /workspace && \
    curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh | bash -s

# Install spaCy
RUN pip install -U pip setuptools wheel && \
    pip install -U spacy && \
    python -m spacy download en_core_web_trf && \
    python -m spacy download ja_core_news_lg && \
    python -m spacy download es_dep_news_trf

# entry
ENTRYPOINT ["python"]