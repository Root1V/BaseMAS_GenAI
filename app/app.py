from app.models.model_factory import LLMFactory
from app.config.model_enum import ModelLLM
from dotenv import load_dotenv


class App:
    """
    Clase principal que gestiona la creación y ejecución de modelos de lenguaje.

    Esta clase es responsable de instanciar varios modelos de lenguaje y generar
    texto basado en solicitudes específicas. Facilita la interacción con diferentes
    tipos de modelos de inteligencia artificial.
    """

    def __init__(self) -> None:
        """
        Inicializa una nueva instancia de la clase Main.

        Este constructor no requiere parámetros y no realiza ninguna acción
        adicional en la inicialización.
        """
        pass

    def run(self):
        """
        Ejecuta el proceso de generación de texto utilizando diferentes modelos de lenguaje.

        Este método crea instancias de varios modelos de lenguaje a través de la
        fábrica de modelos y genera respuestas basadas en solicitudes específicas.
        Luego, imprime las respuestas generadas por cada modelo en la consola.
        """

        gptModel = LLMFactory.create(ModelLLM.MODEL_GPT)
        # claudeModel = LLMFactory.create(
        #     model=ModelLLM.MODEL_CLAUDE, type=AgentType.PROGRAMMER
        # )
        # llamaModel = LLMFactory.create(
        #     model=ModelLLM.MODEL_LLAMA, type=AgentType.WRITER
        # )
        # geminiModel = LLMFactory.create(
        #     model=ModelLLM.MODEL_GEMINI, type=AgentType.DESIGNER
        # )
        # mixtralModel = LLMFactory.create(
        #     model=ModelLLM.MODEL_MIXTRAL, type=AgentType.ASISTANT
        # )

        responseGPT = gptModel.generate_text(
            "Dime los mejores escritores de ciencia ficcion"
        )
        # responseLlama = llamaModel.generate_text(
        #     "Escribe un poema como lo haria una AGI dedicado a la humanidad."
        # )
        # responseClaude = claudeModel.generate_text(
        #     "Dime cual seria la mejor estructura de una clase para agentes de IA que puedan ser multimodales y que puedan ejecutar codigo y dime como podria ejecutar codigo  "
        # )
        # responseGemini = geminiModel.generate_text(
        #     "Como podria aprender a tocar piano sin perder la inspiracion y la disciplina diaria"
        # )
        # responseMixtral = mixtralModel.generate_text(
        #     "cual seria la mejor estrategia para estructurar una aplicacion que genere un Sistema Multi-Agente potenciado por IA generativa"
        # )

        print("Model GPT ->\n", responseGPT)
        # print("Model CLAUDE ->\n", responseClaude)
        # print("Model LLAMA ->\n", responseLlama)
        # print("Model GEMINI ->\n", responseGemini)
        # print("Model MIXTRAL ->\n", responseMixtral)


if __name__ == "__main__":
    load_dotenv()

    app = App()
    app.run()

# "Dime como puedo crear una clase que me permita instanciar un modelo LLM, considerando que pueden haber varios proveedores de LLM"
