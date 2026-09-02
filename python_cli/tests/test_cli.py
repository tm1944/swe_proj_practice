from src.taskManager import TaskManager
from src.task import Task


taskManager = TaskManager()
test_task = taskManager.make_task("Buy Milk")

def test_add_task():
	result = taskManager.add_task(test_task)
	assert result is True 

def test_remove_task():
	result = taskManager.remove_task(test_task.uid)
	assert result is True 

def test_complete_task():
	taskManager.add_task(test_task)
	result = taskManager.complete_task(test_task.uid)
	assert result is True 