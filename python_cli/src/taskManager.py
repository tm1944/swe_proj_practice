from src.task import Task
from src.storage import Storage

class TaskManager:
	def __init__(self):
		self.storage = Storage()
		self.task_dict = self.storage.load_data()



	def make_task(self,name:str)-> Task:
		task = Task(name=name)
		return task

	def add_task(self, task: Task)-> bool:
		try:
			self.task_dict[task._next_UID] = task
			self.storage.save_data(self.task_dict)
			return True
		except Exception as e:
			print(e)
			return False

	def remove_task(self,taskID: int)-> bool:
		try:
			del self.task_dict[taskID] 
			Task.next_UID_on_DELETE()
			self.storage.save_data(self.task_dict)
			return True
		except:
			return False

	def complete_task(self,taskID: int)-> bool:
		try:
			self.task_dict[taskID].status = 'completed'
			self.storage.save_data(self.task_dict)
			return True
		except:
			return False

	def print_task_dict(self):
		print(self.task_dict)