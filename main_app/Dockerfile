FROM python:3.12

WORKDIR /usr/src/app

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# CMD ["celery", "-A", "worker_1", "worker", "-E", "--loglevel=INFO"]
CMD ["python", "-u","main.py"]