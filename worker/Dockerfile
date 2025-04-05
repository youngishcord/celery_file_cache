FROM python:3.12

WORKDIR /usr/src/app

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["celery", "-A", "main", "worker", "-E", "--loglevel=INFO", "-n", "cache_test", "-Q", "cache_test"]