from typing import Union
from pydantic import BaseModel

class tasksCreate(BaseModel):
    id: int
    title: str
    description: str
    status: bool 

class tasks(tasksCreate):
    id: int
    title: str
    description: str
    status: bool

class tasksUpdate(tasksCreate): 
    id: int
    title: Union[str, None]
    description: Union[str, None] 
    status: Union[str, None]

class tasksDelete(BaseModel):
    id: int
    title: str
    description: str
    status: bool