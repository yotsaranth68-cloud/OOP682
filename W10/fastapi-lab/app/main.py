from fastapi import FastAPI, Depends
from typing import List
from .models import Task, TaskCreate
from .repositories import InMemoryTaskRepository, ITaskRepository, SqlTaskRepository
from .services import TaskService
from .database import SessionLocal
from sqlalchemy.orm import Session
from .database import engine
from . import models_orm

models_orm.Base.metadata.create_all(bind=engine)
app = FastAPI()

# Singleton Repository Instance
task_repo = InMemoryTaskRepository()


def get_db():
    db = SessionLocal()  # เปิดประตูบ้านของจริงแล้ว
    try:
        yield db
    finally:
        db.close()  # ปิดประตูทุกครั้งหลังใช้งานเสร็จ


def get_task_service(db: Session = Depends(get_db)):
    repo = SqlTaskRepository(db)
    return TaskService(repo)


@app.get("/tasks", response_model=List[Task])
def read_tasks(service: TaskService = Depends(get_task_service)):
    return service.get_tasks()


@app.post("/tasks", response_model=Task)
def create_task(task: TaskCreate, service: TaskService = Depends(get_task_service)):
    return service.create_task(task)