import os
from app.config.prompt_enum import PromptEnum, AgentType


class PromptLLM:
    """
    Clase que maneja la carga de prompts desde archivos de texto.

    Esta clase permite cargar prompts específicos según su enumeración y tipo de agente, facilitando la gestión de
    contenido en aplicaciones que requieren interacción con modelos de lenguaje.
    """

    PROMPT_DIR = "app/prompts/"

    def load_prompt(self, prompt: PromptEnum):
        """Carga y devuelve el contenido del archivo de prompt correspondiente.

        Args:
            prompt (PromptEnum): El enumerado que representa el prompt a cargar.

        Returns:
            str: El contenido del archivo de prompt.

        Raises:
            FileNotFoundError: Si el archivo de prompt no existe en la ruta especificada.
        """
        prompt_path = os.path.join(self.PROMPT_DIR, prompt.value)
        if not os.path.exists(prompt_path):
            raise FileNotFoundError(f"El archivo {prompt_path} no existe.")

        with open(prompt_path, "r") as file:
            return file.read()

    def get_prompts_type(self, type: AgentType):
        """Devuelve los prompts correspondientes a un tipo de agente.

        Args:
            type (AgentType): El tipo de agente para el cual se obtienen los prompts.

        Returns:
            tuple: Una tupla que contiene el contenido del prompt del sistema y del usuario.
        """
        sys_prompt, user_prompt = type.value
        sys_content = self.load_prompt(sys_prompt)
        user_content = self.load_prompt(user_prompt)
        return sys_content, user_content
