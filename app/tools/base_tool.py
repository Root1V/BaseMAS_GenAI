from abc import ABC, abstractmethod

class BaseTool(ABC):
    name: str
    description:str
    expected_output: str
    skill: object = None
    
    @abstractmethod
    def run(self, argument: str) -> str:
        return "Result"