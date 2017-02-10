#ScrapyTest
Study project for scrapy.
Usage:
```shell
docker-compose build my-scrapy
docker-compose up -d phantomjs
docker-compose run my-scrapy /bin/sh
# in container
scrapy crawl author -o result.jl
```