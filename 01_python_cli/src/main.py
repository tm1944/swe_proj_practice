import sys
from src.taskManager import TaskManager


def exec_cmd(cmd: list[str], taskM: TaskManager)-> bool:
	
	match cmd[1].lower():
		case "add":
			task = taskM.make_task(' '.join(cmd[2:]))
			taskM.add_task(task)
			return True
		case "delete":
			taskM.remove_task(int(cmd[2]))
		case "complete":
			taskM.complete_task(int(cmd[2]))
		case "list":
			taskM.print_task_dict()
		case _:
			return False
	return False



def main():
	taskM = TaskManager()

	while True:
		user_input = input()
		args = user_input.split() #conver input to list
		if args[0] == "exit" or len(args) < 1:
			break
		else: 
			exec_cmd(args,taskM)

	
if __name__ == "__main__":
	main()