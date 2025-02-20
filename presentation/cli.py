import click
from use_cases.todo_usecase import TodoUseCase
from repositories.todo_repositories import TaskRepository

repo = TaskRepository()
todo_use_case = TodoUseCase(repo)

@click.group()
def cli():
  pass

@click.group()
def todo():
  pass

@todo.command()
@click.argument("task")
def add(task):
  """ Add New Task """
  todo_use_case.add_task(task)

@todo.command()
@click.argument("index", type=int)
def remove(index):
  """ Remove a task by index """
  removed = todo_use_case.remove_task(index)
  if removed:
    click.echo(f"Task removed: {removed.description}")
  else:
    click.echo("Task not found.")

@todo.command()
def show():
  """ Show all tasks"""
  tasks = todo_use_case.get_taks()
  if tasks:
    click.echo("\n --- To-Do List ---")
    for i,task in enumerate(tasks):
      click.echo(f"{i + 1}. {task.description}")
  else:
    click.echo("No tasks found.")

cli.add_command(todo)