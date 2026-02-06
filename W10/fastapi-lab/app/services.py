from fastapi import HTTPException
from .repositories import ITaskRepository
from .models import TaskCreate

class TaskService:
    def __init__(self, repo: ITaskRepository):
        self.repo = repo

    def get_tasks(self):
        return self.repo.get_all()

    def create_task(self, task_in: TaskCreate):
        # ✅ Validation: ห้ามชื่อซ้ำ
        existing = self.repo.get_by_title(task_in.title)
        if existing:
            raise HTTPException(status_code=400, detail="Task title already exists")

        return self.repo.create(task_in)

    def mark_complete(self, task_id: int):
        task = self.repo.get_by_id(task_id)
        if not task:
            return None

        task.completed = True
        return self.repo.update(task)
