from presentation.cli import cli
from use_cases.todo_usecase import TodoUseCase
from repositories.todo_repositories import TaskRepository

def create_application():
  repo = TaskRepository()
  todo_service  = TodoUseCase(repo)
  return todo_service

if __name__ == "__main__":
  service = create_application()
  cli(service)
