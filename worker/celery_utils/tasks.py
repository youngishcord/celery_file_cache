
from dataclasses import dataclass
from .celery_model import Task


@dataclass
class Queues:
    file_cache: str = "cache_test"

@dataclass
class Tasks:
    test_task = Task("test.task").s().set(queue=Queues.file_cache)
    
    