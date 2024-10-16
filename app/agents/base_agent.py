from typing import Optional, List

class Agent():
    """
    Clase base para todos los agentes.

    Esta clase proporciona una estructura común y métodos básicos que son
    compartidos por todos los tipos de agentes en el sistema. Los agentes
    pueden ser utilizados para realizar diversas tareas dentro de un
    entorno específico, facilitando la extensión y personalización de su
    comportamiento.
    """
    role: str = 'Assistant'
    name: str = 'Elysia'  
    goal: Optional[str] = None
    tools: List[object] = []  
    signal: Optional[str] = None
    llm: object = None
    memory: bool = False
    planning: bool = False
    max_iteration: int = 20
    master: bool = False
    endSignal: str = "END"

    def __init__(self) -> None:
        pass
    
