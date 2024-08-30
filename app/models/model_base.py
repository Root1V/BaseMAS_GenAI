# Clase base para todos los agentes
from abc import ABC, abstractmethod

class BaseLLM(ABC):

    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def generate_text(self, prompt):
        print("Base LLM Text: ", prompt)

    @abstractmethod
    def generate_image(self, prompt):
        print("Base LLM Image: ", prompt)

    @abstractmethod
    def generate_audio(self, prompt):
        print("Base LLM Audio: ", prompt)
    