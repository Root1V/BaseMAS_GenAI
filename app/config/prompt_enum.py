from enum import Enum

class PromptEnum(Enum):
    ASISTANT_SYS = "asistant_sys.txt"
    ASISTANT_USER = "asistant_user.txt"
    WRITER_SYS = "writter_sys.txt"
    WRITER_USER = "writter_user.txt"
    DESIGNER_SYS = "designer_sys.txt"
    DESIGNER_USER = "designer_user.txt"
    PROGRAMMER_SYS = "programmer_sys.txt"
    PROGRAMMER_USER = "programmer_user.txt"

class AgentType(Enum):
    ASISTANT = (PromptEnum.ASISTANT_SYS, PromptEnum.ASISTANT_USER)
    WRITER = (PromptEnum.WRITER_SYS, PromptEnum.WRITER_USER)
    DESIGNER = (PromptEnum.DESIGNER_SYS, PromptEnum.DESIGNER_USER)
    PROGRAMMER = (PromptEnum.PROGRAMMER_SYS, PromptEnum.PROGRAMMER_USER)
