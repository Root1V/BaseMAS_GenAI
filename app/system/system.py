from app.models.model_factory import LLMFactory
from app.config.model_enum import ModelLLM


class System:

    def __init__(self) -> None:
        self.llm = LLMFactory.create(ModelLLM.MODEL_GPT)

    def createName(self, prompt):
        prompt = f"Bajo este contexto {prompt}, crear un nombre para un agente de IA de  9 caracteres que mejor represente su rol. Responde solo con el nombre sin nada mas"

        name = self.llm.generate_text(prompt)
        return name
