import google.generativeai as gai
from app.models.model_base import BaseLLM
from app.config.prompt_enum import AgentType
from app.config.config import ConfigLLM
from app.config.model_enum import ModelLLM
from app.config.prompt import PromptLLM
import os


class GoogleModel(BaseLLM):
    def __init__(
        self, type: AgentType, model: ModelLLM = ModelLLM.MODEL_GEMINI
    ) -> None:
        super().__init__()
        gai.configure(api_key=os.environ["GEMINI_API_KEY"])

        self.config = ConfigLLM.get(model)
        self.client = gai.GenerativeModel(self.config["name"])
        self.SYS_PROMPT, self.USER_PROMPT = PromptLLM().get_prompts_type(type)

        print("\nSYSTEM: \n", self.SYS_PROMPT)
        print("\nUSER: \n", self.USER_PROMPT)

    def generate_text(self, prompt):

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
        # Implementación para generar audio
        print("Generating audio with input:", prompt)
        # Lógica para generar audio aquí

    def generate_image(self, prompt):
        # Implementación para generar imagen
        print("Generating image with input:", prompt)
        # Lógica para generar imagen aquí
