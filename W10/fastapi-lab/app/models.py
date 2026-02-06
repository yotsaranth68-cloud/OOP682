from pydantic import BaseModel
from typing import Optional

# Base Model (Shared properties)
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

# Model for Creation (Input)
class TaskCreate(TaskBase):
    pass

# Model for Reading (Output - includes ID)
class Task(TaskBase):
    id: int

    class Config:
        from_attributes = True