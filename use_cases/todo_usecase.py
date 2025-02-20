from typing import List
from entities.task import Task
from repositories.todo_repositories import TaskRepository


class TodoUseCase:

  def __init__(self, repository: TaskRepository):
    self.repository = repository

  def add_task(self, task: str):
    """ Add New Task """
    tasks = self.repository.load_tasks()
    tasks.append(Task(description=task))
    self.repository.save_tasks(tasks)

  def remove_task(self, index: int):
    """ Remove Task """
    tasks = self.repository.load_tasks()
    if index >= 0 & index < len(tasks):
      removed_task = tasks.pop(index)
      self.repository.save_tasks(tasks)
      return removed_task

  def get_taks(self) -> List[Task]:
    """ Get Tasks """
    return self.repository.load_tasks()
