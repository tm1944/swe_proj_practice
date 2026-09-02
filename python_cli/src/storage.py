import os
import json
from src.task import Task
from dataclasses import asdict


class Storage:
	def __init__(self):
		pass



	def load_data(self)->dict:
		if not os.path.exists("data.json"):
			return {}

		with open("data.json", encoding="utf-8") as file:
			content = file.read()

		if not content.strip():
			return {}

		raw_tasks = json.loads(content)
		task_dict = {}

		for uid_text, task_data in raw_tasks.items():
			task = Task(
				name=task_data["name"],
				status=task_data["status"],
			)
			task.uid = int(uid_text)
			task_dict[task.uid] = task

		Task._next_UID = max(task_dict, default=0)

		return task_dict

	def save_data(self,task_list: dict[int,Task]):
		with open('data.json','w',encoding='utf-8')as file:
			 json.dump(
            {str(uid): asdict(task) for uid, task in task_list.items()},
            file,
            indent=2,)
