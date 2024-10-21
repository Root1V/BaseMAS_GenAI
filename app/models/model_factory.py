from app.models.model_base import BaseLLM
from app.models.model_openai import OpenAIModel
from app.models.model_groq import GroqModel
from app.models.model_anthropic import AnthropicModel
from app.models.model_google import GoogleModel
from app.config.model_enum import ModelLLM


class LLMFactory:
    """
    Clase responsable de la creación de instancias de modelos de lenguaje (LLM)
    basados en el tipo de modelo y el tipo de agente especificados.

    Esta fábrica permite la instancia de diferentes modelos de LLM, facilitando
    la integración y el uso de múltiples proveedores de modelos en una aplicación.
    """

    @staticmethod
    def create(model: ModelLLM) -> BaseLLM:
        """
        Crea una instancia de un modelo de lenguaje basado en el tipo de modelo
        y el tipo de agente proporcionados.

        Args:
            model (ModelLLM): El tipo de modelo de lenguaje que se desea crear.

        Returns:
            BaseLLM: Una instancia del modelo de lenguaje correspondiente.

        Raises:
            ValueError: Si el modelo proporcionado no es compatible o no está
            soportado por la fábrica.
        """
        if model == ModelLLM.MODEL_GPT:
            return OpenAIModel(model)
        elif model in (ModelLLM.MODEL_LLAMA, ModelLLM.MODEL_MIXTRAL):
            return GroqModel(model)
        elif model == ModelLLM.MODEL_CLAUDE:
            return AnthropicModel(model)
        elif model == ModelLLM.MODEL_GEMINI:
            return GoogleModel(model)
        else:
            raise ValueError(f"Unsupported provider: {model.value}")
