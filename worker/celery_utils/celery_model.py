from celery import Celery
from celery import Task as BaseTask

from .celery_conf import CelerySettings


def create_celery():
    app = Celery("api_client")
    app.config_from_object(CelerySettings().model_dump())
    return app


class Task(BaseTask):
    def __init__(self, name, *args, **kwargs):
        super(BaseTask, self).__init__(*args, **kwargs)
        self.name = name
