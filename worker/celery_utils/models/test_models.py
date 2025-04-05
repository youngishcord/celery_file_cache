from pydantic import BaseModel

class TestTaskArg(BaseModel):
    text: str
    
class TestTaskResult(BaseModel):
    text: str
    