from enum import Enum


class PromptEnum(Enum):
    """
    Enum que representa los diferentes archivos de configuración para cada tipo de agente.

    Cada miembro de esta enumeración corresponde a un archivo específico que contiene
    información o configuraciones para los agentes en el sistema.
    """

    ASISTANT_SYS = "asistant_sys.txt"
    ASISTANT_USER = "asistant_user.txt"
    WRITER_SYS = "writter_sys.txt"
    WRITER_USER = "writter_user.txt"
    DESIGNER_SYS = "designer_sys.txt"
    DESIGNER_USER = "designer_user.txt"
    PROGRAMMER_SYS = "programmer_sys.txt"
    PROGRAMMER_USER = "programmer_user.txt"


class AgentType(Enum):
    """
    Enum que representa los diferentes tipos de agentes y sus archivos de configuración asociados.

    Cada miembro de esta enumeración agrupa los archivos de configuración del sistema y del usuario
    para cada tipo de agente, facilitando su acceso y gestión en el sistema.
    """

    ASISTANT = (PromptEnum.ASISTANT_SYS, PromptEnum.ASISTANT_USER)
    WRITER = (PromptEnum.WRITER_SYS, PromptEnum.WRITER_USER)
    DESIGNER = (PromptEnum.DESIGNER_SYS, PromptEnum.DESIGNER_USER)
    PROGRAMMER = (PromptEnum.PROGRAMMER_SYS, PromptEnum.PROGRAMMER_USER)
