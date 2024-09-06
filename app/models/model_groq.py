from groq import Groq
from app.models.model_base import BaseLLM
from app.config.prompt_enum import AgentType
from app.config.config import ConfigLLM
from app.config.model_enum import ModelLLM
from app.config.prompt import PromptLLM


class GroqModel(BaseLLM):
    """
    Clase que representa un modelo de lenguaje Groq, heredando de BaseLLM.

    Esta clase permite la generación de texto, audio e imágenes utilizando el modelo
    especificado y proporciona prompts configurados según el tipo de agente.
    """

    def __init__(self, type: AgentType, model: ModelLLM = ModelLLM.MODEL_LLAMA) -> None:
        """
        Inicializa el modelo Groq con la configuración adecuada y los prompts.

        Args:
            type (AgentType): Tipo de agente que define el comportamiento del modelo.
            model (ModelLLM, opcional): El modelo a utilizar, por defecto es MODEL_LLAMA.
        """
        super().__init__()
        self.config = ConfigLLM.get(model)
        self.client = Groq()
        self.SYS_PROMPT, self.USER_PROMPT = PromptLLM().get_prompts_type(type)

        print("\nSYSTEM: \n", self.SYS_PROMPT)
        print("\nUSER: \n", self.USER_PROMPT)

    def generate_text(self, prompt):
        """
        Genera texto a partir de un prompt dado utilizando el modelo Groq.

        Args:
            prompt (str): El texto de entrada para generar la respuesta.

        Returns:
            str: La respuesta generada por el modelo.
        """
        super().generate_text(prompt)
        print("LLAMA LLM: ", prompt)

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
        message = response.choices[0].message.content

        return message

    def generate_audio(self, prompt):
        """
        Genera audio a partir de un prompt dado.

        Args:
            prompt (str): El texto de entrada para generar el audio.

        Returns:
            None: Esta función no devuelve ningún valor.
        """
        # Implementación para generar audio
        print("Generating audio with input:", prompt)
        # Lógica para generar audio aquí

    def generate_image(self, prompt):
        """
        Genera una imagen a partir de un prompt dado.

        Args:
            prompt (str): El texto de entrada para generar la imagen.

        Returns:
            None: Esta función no devuelve ningún valor.
        """
        # Implementación para generar imagen
        print("Generating image with input:", prompt)
        # Lógica para generar imagen aquí
