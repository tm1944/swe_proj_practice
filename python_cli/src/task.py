from dataclasses import dataclass, field
from typing import ClassVar



@dataclass
class Task:
	_next_UID: ClassVar[int] = 0


	uid: int = field(init=False)
	name: str
	status: str = "pending"


	def __post_init__(self):
		Task._next_UID+=1
		self.uid = Task._next_UID

	def next_UID_on_DELETE():
		Task._next_UID-=1