from typing import Optional, List
from app.models.model_factory import LLMFactory
from app.config.model_enum import ModelLLM
from app.config.prompt_enum import AgentType
from app.system.system import System


class Agent:
    """
    Clase base para todos los agentes.

    Esta clase proporciona una estructura común y métodos básicos que son
    compartidos por todos los tipos de agentes en el sistema. Los agentes
    pueden ser utilizados para realizar diversas tareas dentro de un
    entorno específico, facilitando la extensión y personalización de su
    comportamiento.
    """

    def __init__(
        self,
        engine=ModelLLM.MODEL_GPT,
        role=AgentType.ASISTANT,
        name: str = "default",
        goal: str = None,
        signal: str = "END",
        memory: bool = False,
        max_iteration: int = 20,
        master: bool = False,
        avatar: str = "default",
    ) -> None:

        self.role = engine
        self.role = role
        self.goal = goal
        self.signal = signal
        self.memory = memory
        self.max_iteration = max_iteration
        self.master = master
        self.avatar = avatar

        self.messages = []
        self.tools = []
        self.llm = LLMFactory.create(engine)
        self.llm.getPrompts(role)

        if name == "default":
            self.name = System().createName(self.llm.SYS_PROMPT)

    def create(self):

        print(f"Imprimor nombre: {self.name}")
