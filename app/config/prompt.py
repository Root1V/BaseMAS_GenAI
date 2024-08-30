import os
from config.prompt_enum import PromptEnum, AgentType

class PromptLLM:

    PROMPT_DIR = "app/prompts/"
    
    def load_prompt(self, prompt: PromptEnum):
        """Carga y devuelve el contenido del prompt.txt de prompts."""

        prompt_path = os.path.join(self.PROMPT_DIR, prompt.value)
        if not os.path.exists(prompt_path):
            raise FileNotFoundError(f"El archivo {prompt_path} no existe.")
        
        with open(prompt_path, "r") as file:
            return file.read()

    def get_prompts_type(self, type: AgentType):
        """Devuelve los prompts correspondientes a un tipo de agente."""

        sys_prompt, user_prompt = type.value
        sys_content = self.load_prompt(sys_prompt)
        user_content = self.load_prompt(user_prompt)
        return sys_content, user_content
    