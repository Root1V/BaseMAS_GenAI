from app.models.model_base import BaseLLM
from app.models.model_openai import OpenAIModel
from app.models.model_groq import GroqModel
from app.models.model_anthropic import AnthropicModel
from app.models.model_google import GoogleModel
from app.config.prompt_enum import AgentType
from app.config.model_enum import ModelLLM


class LLMFactory:

    @staticmethod
    def create(model: ModelLLM, type: AgentType) -> BaseLLM:

        if model == ModelLLM.MODEL_GPT:
            return OpenAIModel(type, model)
        elif model in (ModelLLM.MODEL_LLAMA, ModelLLM.MODEL_MIXTRAL):
            return GroqModel(type, model)
        elif model == ModelLLM.MODEL_CLAUDE:
            return AnthropicModel(type, model)
        elif model == ModelLLM.MODEL_GEMINI:
            return GoogleModel(type, model)
        else:
            raise ValueError(f"Unsupported provider: {model.value}")
