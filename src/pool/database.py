"""
Responsible for all database related operations.
"""
from .base_classes import *

class Pool:
    def __init__(self, name:str, port:int=2048, polling_rate:float=1.0) -> None:
        """
        Creates a Pool. I
        """
        self._root_table = PoolDict()

    def on_change(self, path:tuple[str], before, after) -> None:
        """
        Called when a change is made to the database.
        This method should be modified when Pool is subclassed in order to
        listen to changes in the database.
        """
        pass
    

    
    