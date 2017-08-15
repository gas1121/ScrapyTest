FROM library/python
MAINTAINER gas1121 <jtdzhx@gmail.com>

# os setup
RUN apt-get update && apt-get -y install \
  python-lxml \
  build-essential \
  libssl-dev \
  libffi-dev \
  python-dev \
  libxml2-dev \
  libxslt1-dev \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /app
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD scrapy crawl quotes
