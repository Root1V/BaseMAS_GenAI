from models.model_factory import LLMFactory
from dotenv import load_dotenv
from config.model_enum import ModelLLM
from config.prompt_enum import AgentType

class Main:

    def __init__(self) -> None:
        pass

    def run(self):

        gptModel = LLMFactory.create(model=ModelLLM.MODEL_GPT, type=AgentType.ASISTANT)
        claudeModel = LLMFactory.create(model=ModelLLM.MODEL_CLAUDE, type=AgentType.PROGRAMMER)
        llamaModel = LLMFactory.create(model=ModelLLM.MODEL_LLAMA, type=AgentType.WRITER)
        geminiModel = LLMFactory.create(model=ModelLLM.MODEL_GEMINI, type=AgentType.DESIGNER)
        mixtralModel = LLMFactory.create(model=ModelLLM.MODEL_MIXTRAL, type=AgentType.ASISTANT)

        responseGPT = gptModel.generate_text("Dime los mejores escritores de ciencia ficcion")
        responseLlama = llamaModel.generate_text("Escribe un poema como lo haria una AGI dedicado a la humanidad.")
        responseClaude = claudeModel.generate_text("Dime cual seria la mejor estructura de una clase para agentes de IA que puedan ser multimodales y que puedan ejecutar codigo y dime como podria ejecutar codigo  ")
        responseGemini = geminiModel.generate_text("Como podria aprender a tocar piano sin perder la inspiracion y la disciplina diaria")
        responseMixtral = mixtralModel.generate_text("cual seria la mejor estrategia para estructurar una aplicacion que genere un Sistema Multi-Agente potenciado por IA generativa")

        print("Model GPT ->\n", responseGPT) 
        print("Model CLAUDE ->\n", responseClaude)
        print("Model LLAMA ->\n", responseLlama)
        print("Model GEMINI ->\n", responseGemini)
        print("Model MIXTRAL ->\n", responseMixtral)

if __name__ == "__main__":
    print("App:\n")

    load_dotenv()

    app = Main()
    app.run()

# "Dime como puedo crear una clase que me permita instanciar un modelo LLM, considerando que pueden haber varios proveedores de LLM"