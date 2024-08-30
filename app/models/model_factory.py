from models.model_base import BaseLLM
from models.model_openai import OpenAIModel
from models.model_groq import GroqModel
from models.model_anthropic import AnthropicModel
from models.model_google import GoogleModel
from config.prompt_enum import AgentType
from config.model_enum import ModelLLM

class LLMFactory:

    @staticmethod
    def create(model: ModelLLM, type: AgentType) -> BaseLLM:

        if model == ModelLLM.MODEL_GPT:
            return OpenAIModel(type, model)
        elif model == ModelLLM.MODEL_LLAMA or ModelLLM.MODEL_MIXTRAL:
            return GroqModel(type, model)
        elif model == ModelLLM.MODEL_CLAUDE:
            return AnthropicModel(type, model)
        elif model == ModelLLM.MODEL_GEMINI:
            return GoogleModel(type, model)
        else:
            raise ValueError(f"Unsupported provider: {model.value}")

