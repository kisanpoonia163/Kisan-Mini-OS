from abc import ABC,abstractmethod

class Command(ABC):
    name:str = ""
    help:str = ""

    @abstractmethod
    def execute(self,args:list[str],context):
        pass