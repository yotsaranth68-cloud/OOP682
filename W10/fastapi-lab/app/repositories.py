from abc import ABC, abstractmethod
from typing import List, Optional
from .models import Task, TaskCreate


class ITaskRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[Task]:
        pass

    @abstractmethod
    def create(self, task: TaskCreate) -> Task:
        pass

    @abstractmethod
    def get_by_id(self, task_id: int) -> Optional[Task]:
        pass

    @abstractmethod
    def update(self, task: Task) -> Task:
        pass

    @abstractmethod
    def get_by_title(self, title: str) -> Optional[Task]:
        pass


# ==========================
# In-Memory Repository
# ==========================
class InMemoryTaskRepository(ITaskRepository):
    def __init__(self):
        self.tasks = []
        self.current_id = 1

    def get_all(self) -> List[Task]:
        return self.tasks

    def create(self, task_in: TaskCreate) -> Task:
        task = Task(id=self.current_id, **task_in.dict())
        self.tasks.append(task)
        self.current_id += 1
        return task

    def get_by_id(self, task_id: int) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update(self, task: Task) -> Task:
        for i, t in enumerate(self.tasks):
            if t.id == task.id:
                self.tasks[i] = task
                return task
        return None

    def get_by_title(self, title: str) -> Optional[Task]:
        for task in self.tasks:
            if task.title == title:
                return task
        return None


# ==========================
# SQL Repository
# ==========================
from sqlalchemy.orm import Session
from . import models_orm

class SqlTaskRepository(ITaskRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Task]:
        return self.db.query(models_orm.Task).all()

    def create(self, task_in: TaskCreate) -> Task:
        db_task = models_orm.Task(**task_in.dict())
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task

    def get_by_id(self, task_id: int):
        return self.db.query(models_orm.Task).filter(models_orm.Task.id == task_id).first()

    def update(self, task):
        self.db.commit()
        self.db.refresh(task)
        return task

    # ✅ เพิ่ม
    def get_by_title(self, title: str):
        return self.db.query(models_orm.Task).filter(models_orm.Task.title == title).first()
