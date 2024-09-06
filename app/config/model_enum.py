from enum import Enum


class ModelLLM(Enum):
    """
    Enum que representa diferentes modelos de lenguaje disponibles.

    Cada miembro de esta enumeración corresponde a un modelo de lenguaje específico,
    facilitando la referencia y uso de estos modelos en otras partes del código.
    """

    MODEL_GPT = "model_OAI_GPT_4"
    MODEL_CLAUDE = "model_ANT_CLAUDE_SONNET"
    MODEL_GEMINI = "model_GOG_GEMINI_P"
    MODEL_LLAMA = "model_META_LLAMA_3"
    MODEL_MIXTRAL = "model_MIXTRAL_8X7B"
    MODEL_DALLE = "model_CLD_SONNET"
    MODEL_WHISPER = "model_CLD_SONNET"
    MODEL_EMBEDDING_ADA = "model_EMBEDDING_1"
    MODEL_EMBEDDING_LLA = "model_CLD_SONNET"
    MODEL_EMBEDDING_MIX = "model_CLD_SONNET"
    MODEL_EMBEDDING_GMI = "model_CLD_SONNET"
