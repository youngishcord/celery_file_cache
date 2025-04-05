import code
import time
from config import settings

from celery.result import AsyncResult

from celery_utils.celery_model import create_celery
from celery_utils.tasks import Tasks
from celery_utils.models.test_models import TestTaskArg

celery_app = create_celery()


while True:
    task: AsyncResult = Tasks.test_task.apply_async(args=[TestTaskArg(text="Это тестовое сообщение в задачу").model_dump()])
    task.get()
    print("task sended")
    time.sleep(5)
