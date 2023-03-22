
from random import choice

# base classes for set, tuple, list, dict
class PoolSet(set):
    ...

class PoolTuple(tuple):
    ...

class PoolList(list):
    ...

class PoolDict(dict):
    def __init__(self, name:str=..., *args, **kwargs) -> None:
        self.name = name
        super().__init__(*args, **kwargs)

