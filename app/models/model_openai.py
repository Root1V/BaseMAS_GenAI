from openai import OpenAI
from models.model_base import BaseLLM
from config.prompt_enum import AgentType
from config.config import ConfigLLM
from config.model_enum import ModelLLM
from config.prompt import PromptLLM

class OpenAIModel(BaseLLM):
    def __init__(self, type: AgentType, model: ModelLLM = ModelLLM.MODEL_GPT) -> None:
        super().__init__()
        self.config= ConfigLLM.get(model)
        self.client = OpenAI()
        self.SYS_PROMPT, self.USER_PROMPT  = PromptLLM().get_prompts_type(type)

        print("\nSYSTEM: \n", self.SYS_PROMPT)
        print("\nUSER: \n", self.USER_PROMPT)

    
    def generate_text(self, prompt):
        
        super().generate_text(prompt)
        print("GPT LLM: ", prompt)

        response = self.client.chat.completions.create(
            model=self.config["name"],
            max_tokens=self.config["max_tokens"],
            temperature=self.config["temperature"],
            messages=[
                {
                    "role": "system",
                    "content": self.SYS_PROMPT
                },
                {
                    "role": "user",
                    "content": self.USER_PROMPT.format(prompt)
                }
            ]
        )
        print(f"Respuesta {self.config['name']}:\n", response)

        return response.choices[0].message.content

    def generate_audio(self, prompt):
        # Implementación para generar audio
        print("Generating audio with input:", prompt)
        # Lógica para generar audio aquí

    def generate_image(self, prompt):
        # Implementación para generar imagen
        print("Generating image with input:", prompt)
        # Lógica para generar imagen aquí