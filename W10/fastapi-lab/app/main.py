from fastapi import FastAPI, Depends
from typing import List
from .models import Task, TaskCreate
from .repositories import InMemoryTaskRepository, ITaskRepository
from .services import TaskService

app = FastAPI()

# Singleton Repository Instance
task_repo = InMemoryTaskRepository()

# Dependency Provider
def get_task_service():
    return TaskService(task_repo)

@app.get("/tasks", response_model=List[Task])
def read_tasks(service: TaskService = Depends(get_task_service)):
    return service.get_tasks()

@app.post("/tasks", response_model=Task)
def create_task(
    task: TaskCreate, 
    service: TaskService = Depends(get_task_service)
):
    return service.create_task(task)