from openai import OpenAI
from app.models.model_base import BaseLLM
from app.config.prompt_enum import AgentType
from app.config.config import ConfigLLM
from app.config.model_enum import ModelLLM
from app.config.prompt import PromptLLM


class OpenAIModel(BaseLLM):
    """
    Clase que representa un modelo de OpenAI, extendiendo la funcionalidad
    de un modelo de lenguaje base. Se encarga de configurar el cliente de OpenAI
    y gestionar la generación de texto, audio e imágenes.
    """

    def __init__(self, type: AgentType, model: ModelLLM = ModelLLM.MODEL_GPT) -> None:
        """
        Inicializa el modelo de OpenAI con un tipo de agente y un modelo específico.

        Args:
            type (AgentType): Tipo de agente que define el comportamiento del modelo.
            model (ModelLLM, opcional): Modelo de lenguaje a utilizar, por defecto es MODEL_GPT.
        """
        super().__init__()
        self.config = ConfigLLM.get(model)
        self.client = OpenAI()
        self.SYS_PROMPT, self.USER_PROMPT = PromptLLM().get_prompts_type(type)

        print("\nSYSTEM: \n", self.SYS_PROMPT)
        print("\nUSER: \n", self.USER_PROMPT)

    def generate_text(self, prompt):
        """
        Genera texto utilizando el modelo de OpenAI basado en el prompt proporcionado.

        Este método envía el prompt al modelo y retorna la respuesta generada.

        Args:
            prompt (str): El texto de entrada que se utilizará para generar la respuesta.

        Returns:
            str: El contenido del mensaje generado por el modelo.
        """
        super().generate_text(prompt)
        print("GPT LLM: ", prompt)

        response = self.client.chat.completions.create(
            model=self.config["name"],
            max_tokens=self.config["max_tokens"],
            temperature=self.config["temperature"],
            messages=[
                {"role": "system", "content": self.SYS_PROMPT},
                {"role": "user", "content": self.USER_PROMPT.format(prompt)},
            ],
        )
        print(f"Respuesta {self.config['name']}:\n", response)

        return response.choices[0].message.content

    def generate_audio(self, prompt):
        """
        Genera audio a partir del prompt proporcionado.

        Este método es un placeholder para la implementación de la generación de audio.

        Args:
            prompt (str): El texto de entrada que se utilizará para generar el audio.
        """
        # Implementación para generar audio
        print("Generating audio with input:", prompt)
        # Lógica para generar audio aquí

    def generate_image(self, prompt):
        """
        Genera una imagen a partir del prompt proporcionado.

        Este método es un placeholder para la implementación de la generación de imágenes.

        Args:
            prompt (str): El texto de entrada que se utilizará para generar la imagen.
        """
        # Implementación para generar imagen
        print("Generating image with input:", prompt)
        # Lógica para generar imagen aquí
