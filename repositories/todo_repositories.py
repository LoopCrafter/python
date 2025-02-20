import json
import os
from typing import List
from entities.task import Task

TODO_FILE = "todo_list.json"


class TaskRepository:

  def load_tasks(self) -> List[Task]:
    if (os.path.exists(TODO_FILE)):
      with open(TODO_FILE, "r") as file:
        tasks_data = json.load(file)
        return [Task(description=t) for t in tasks_data]
    return []

  def save_tasks(self, tasks: List[Task]):
    with open(TODO_FILE, "w") as file:
      json.dump([t.description for t in tasks], file, indent=4)
