from anthropic import Anthropic
from app.models.model_base import BaseLLM
from app.config.prompt_enum import AgentType
from app.config.config import ConfigLLM
from app.config.model_enum import ModelLLM
from app.config.prompt import PromptLLM


class AnthropicModel(BaseLLM):
    """
    Clase que representa un modelo de lenguaje basado en la API de Anthropic.
    Hereda de BaseLLM y proporciona métodos para generar texto, audio e imagen
    utilizando el modelo Claude.

    Attributes:
        config (dict): Configuración del modelo, incluyendo nombre, max_tokens y temperatura.
        client (Anthropic): Cliente para interactuar con la API de Anthropic.
        SYS_PROMPT (str): Prompt del sistema para el modelo.
        USER_PROMPT (str): Prompt del usuario para el modelo.
    """

    def __init__(
        self, type: AgentType, model: ModelLLM = ModelLLM.MODEL_CLAUDE
    ) -> None:
        """
        Inicializa una instancia del modelo Anthropic.

        Args:
            type (AgentType): Tipo de agente que determina el tipo de prompt a utilizar.
            model (ModelLLM, optional): Modelo a utilizar, por defecto es MODEL_CLAUDE.
        """
        super().__init__()
        self.config = ConfigLLM.get(model)
        self.client = Anthropic()
        self.SYS_PROMPT, self.USER_PROMPT = PromptLLM().get_prompts_type(type)

        print("\nSYSTEM: \n", self.SYS_PROMPT)
        print("\nUSER: \n", self.USER_PROMPT)

    def generate_text(self, prompt):
        """
        Genera texto utilizando el modelo Claude basado en el prompt proporcionado.

        Args:
            prompt (str): El texto de entrada para el modelo.

        Returns:
            str: Texto generado por el modelo como respuesta al prompt.
        """
        super().generate_text(prompt)
        print("CLAUDE LLM: ", prompt)

        response = self.client.messages.create(
            model=self.config["name"],
            max_tokens=self.config["max_tokens"],
            temperature=self.config["temperature"],
            system=self.SYS_PROMPT,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": self.USER_PROMPT.format(prompt)}
                    ],
                }
            ],
        )

        print(f"Respuesta {self.config['name']}:\n", response)

        return response.content[0].text

    def generate_audio(self, prompt):
        """
        Genera audio a partir del prompt proporcionado.

        Args:
            prompt (str): El texto de entrada para la generación de audio.
        """
        print("Generating audio with input:", prompt)
        # Lógica para generar audio aquí

    def generate_image(self, prompt):
        """
        Genera una imagen a partir del prompt proporcionado.

        Args:
            prompt (str): El texto de entrada para la generación de imagen.
        """
        print("Generating image with input:", prompt)
        # Lógica para generar imagen aquí
