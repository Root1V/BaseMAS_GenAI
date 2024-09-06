import google.generativeai as gai
from app.models.model_base import BaseLLM
from app.config.prompt_enum import AgentType
from app.config.config import ConfigLLM
from app.config.model_enum import ModelLLM
from app.config.prompt import PromptLLM
import os


class GoogleModel(BaseLLM):
    """
    Clase que representa un modelo de lenguaje generativo de Google.

    Esta clase extiende la funcionalidad de BaseLLM para interactuar con el modelo generativo de Google,
    configurando el cliente y los prompts necesarios para la generación de texto, audio e imagen.
    """

    def __init__(
        self, type: AgentType, model: ModelLLM = ModelLLM.MODEL_GEMINI
    ) -> None:
        """
        Inicializa una instancia de GoogleModel.

        Configura la API de Google y establece los prompts del sistema y del usuario basados en el tipo de agente.

        Args:
            type (AgentType): El tipo de agente que determina el comportamiento del modelo.
            model (ModelLLM, opcional): El modelo a utilizar, por defecto es MODEL_GEMINI.
        """
        super().__init__()
        gai.configure(api_key=os.environ["GEMINI_API_KEY"])

        self.config = ConfigLLM.get(model)
        self.client = gai.GenerativeModel(self.config["name"])
        self.SYS_PROMPT, self.USER_PROMPT = PromptLLM().get_prompts_type(type)

        print("\nSYSTEM: \n", self.SYS_PROMPT)
        print("\nUSER: \n", self.USER_PROMPT)

    def generate_text(self, prompt):
        """
        Genera texto utilizando el modelo generativo de Google.

        Combina el prompt del sistema y el prompt del usuario para crear un prompt completo que se envía al modelo.

        Args:
            prompt (str): El texto de entrada proporcionado por el usuario para la generación de texto.

        Returns:
            str: El texto generado por el modelo.
        """
        super().generate_text(prompt)
        print("GEMINI LLM: ", prompt)

        promptComplete = f"{self.SYS_PROMPT}\n\nUser: {self.USER_PROMPT.format(prompt)}"

        response = self.client.generate_content(
            promptComplete,
            generation_config=gai.GenerationConfig(
                max_output_tokens=1000, temperature=0.1
            ),
        )

        print(f"Respuesta {self.config['name']}:\n", response)

        return response.text

    def generate_audio(self, prompt):
        """
        Genera audio a partir del texto proporcionado.

        Este método está destinado a implementar la lógica para la generación de audio.
        Actualmente solo imprime el prompt de entrada.

        Args:
            prompt (str): El texto de entrada para la generación de audio.
        """
        print("Generating audio with input:", prompt)
        # Lógica para generar audio aquí

    def generate_image(self, prompt):
        """
        Genera una imagen a partir del texto proporcionado.

        Este método está destinado a implementar la lógica para la generación de imágenes.
        Actualmente solo imprime el prompt de entrada.

        Args:
            prompt (str): El texto de entrada para la generación de imagen.
        """
        print("Generating image with input:", prompt)
        # Lógica para generar imagen aquí
