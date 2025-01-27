from abc import ABC, abstractmethod
from app.config.config import ConfigLLM
from app.config.prompt import PromptLLM
from app.config.prompt_enum import AgentType


class BaseLLM(ABC):
    """
    Clase base para todos los agentes de modelos de lenguaje (LLM).

    Esta clase define la interfaz para la generación de texto, imágenes y audio.
    Las subclases deben implementar los métodos abstractos para proporcionar
    funcionalidades específicas de generación de contenido.
    """

    def __init__(self) -> None:
        """
        Inicializa una instancia de la clase BaseLLM.

        Este constructor llama al constructor de la clase base.
        """
        super().__init__()
        self.SYS_PROMPT = None
        self.USER_PROMPT = None
        self.getPrompts(AgentType.DEFAULT)

    def getConfig(self, model):
        self.config = ConfigLLM.get(model)

    def getPrompts(self, type):
        self.SYS_PROMPT, self.USER_PROMPT = PromptLLM().get_prompts_type(type)

    @abstractmethod
    def generate_text(self, prompt):
        """
        Genera texto basado en el prompt proporcionado.

        Args:
            prompt (str): El texto de entrada que se utilizará como base para
            la generación del texto.

        Raises:
            NotImplementedError: Si la subclase no implementa este método.
        """
        print("Base LLM Text: ", prompt)

    @abstractmethod
    def generate_image(self, prompt):
        """
        Genera una imagen basada en el prompt proporcionado.

        Args:
            prompt (str): El texto de entrada que se utilizará como base para
            la generación de la imagen.

        Raises:
            NotImplementedError: Si la subclase no implementa este método.
        """
        print("Base LLM Image: ", prompt)

    @abstractmethod
    def generate_audio(self, prompt):
        """
        Genera audio basado en el prompt proporcionado.

        Args:
            prompt (str): El texto de entrada que se utilizará como base para
            la generación del audio.

        Raises:
            NotImplementedError: Si la subclase no implementa este método.
        """
        print("Base LLM Audio: ", prompt)
