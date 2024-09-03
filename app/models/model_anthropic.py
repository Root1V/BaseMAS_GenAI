from anthropic import Anthropic
from app.models.model_base import BaseLLM
from app.config.prompt_enum import AgentType
from app.config.config import ConfigLLM
from app.config.model_enum import ModelLLM
from app.config.prompt import PromptLLM


class AnthropicModel(BaseLLM):
    def __init__(
        self, type: AgentType, model: ModelLLM = ModelLLM.MODEL_CLAUDE
    ) -> None:
        super().__init__()
        self.config = ConfigLLM.get(model)
        self.client = Anthropic()
        self.SYS_PROMPT, self.USER_PROMPT = PromptLLM().get_prompts_type(type)

        print("\nSYSTEM: \n", self.SYS_PROMPT)
        print("\nUSER: \n", self.USER_PROMPT)

    def generate_text(self, prompt):

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
        # Implementación para generar audio
        print("Generating audio with input:", prompt)
        # Lógica para generar audio aquí

    def generate_image(self, prompt):
        # Implementación para generar imagen
        print("Generating image with input:", prompt)
        # Lógica para generar imagen aquí
