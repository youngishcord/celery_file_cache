import pydantic

from config import settings
from celery_utils.celery_model import create_celery
from celery_utils.models.test_models import TestTaskArg, TestTaskResult


app = create_celery()

@app.task(name="test.task", pydantic=True)
def test_task(arg: TestTaskArg) -> TestTaskResult:
    
    print(arg.text)
    
    return TestTaskResult(text=arg.text)
