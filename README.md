Namespace BaseMAS
=================
CONFIG: .env
    OPENAI_API_KEY=
    GROQ_API_KEY=
    ANTHROPIC_API_KEY=
    GEMINI_API_KEY=


RUN:
    > python app.py

Sub-modules
-----------
* BaseMAS.app
* BaseMAS.test


Module BaseMAS.app.tools.tool_web_search
========================================


Module BaseMAS.app.util.helpers
===============================


Module BaseMAS.app.config.model_enum
====================================

Classes
-------

`ModelLLM(value, names=None, *, module=None, qualname=None, type=None, start=1)`
:   An enumeration.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `MODEL_CLAUDE`
    :

    `MODEL_DALLE`
    :

    `MODEL_EMBEDDING_ADA`
    :

    `MODEL_EMBEDDING_GMI`
    :

    `MODEL_EMBEDDING_LLA`
    :

    `MODEL_EMBEDDING_MIX`
    :

    `MODEL_GEMINI`
    :

    `MODEL_GPT`
    :

    `MODEL_LLAMA`
    :

    `MODEL_MIXTRAL`
    :

    `MODEL_WHISPER`
    :


Module BaseMAS.app.config.prompt_enum
=====================================

Classes
-------

`AgentType(value, names=None, *, module=None, qualname=None, type=None, start=1)`
:   An enumeration.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `ASISTANT`
    :

    `DESIGNER`
    :

    `PROGRAMMER`
    :

    `WRITER`
    :

`PromptEnum(value, names=None, *, module=None, qualname=None, type=None, start=1)`
:   An enumeration.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `ASISTANT_SYS`
    :

    `ASISTANT_USER`
    :

    `DESIGNER_SYS`
    :

    `DESIGNER_USER`
    :

    `PROGRAMMER_SYS`
    :

    `PROGRAMMER_USER`
    :

    `WRITER_SYS`
    :

    `WRITER_USER`
    :


Module BaseMAS.app.config.prompt
================================

Classes
-------

`PromptLLM()`
:

    ### Class variables

    `PROMPT_DIR`
    :

    ### Methods

    `get_prompts_type(self, type: app.config.prompt_enum.AgentType)`
    :   Devuelve los prompts correspondientes a un tipo de agente.

    `load_prompt(self, prompt: app.config.prompt_enum.PromptEnum)`
    :   Carga y devuelve el contenido del prompt.txt de prompts.


Module BaseMAS.app.config.config
================================

Classes
-------

`ConfigLLM()`
:

    ### Class variables

    `CONFIG_PATH`
    :

    ### Static methods

    `get(model: app.config.model_enum.ModelLLM, default: Any = None) ‑> Any`
    :   Devuelve la configuración del modelo especificado por model_key.


Module BaseMAS.app.agents.audio_agent
=====================================


Module BaseMAS.app.agents.image_agent
=====================================


Module BaseMAS.app.agents.multi_modal_agent
===========================================


Module BaseMAS.app.agents.text_agent
====================================


Module BaseMAS.app.agents.base_agent
====================================


Module BaseMAS.app.models.model_openai
======================================

Classes
-------

`OpenAIModel(type: app.config.prompt_enum.AgentType, model: app.config.model_enum.ModelLLM = ModelLLM.MODEL_GPT)`
:   Helper class that provides a standard way to create an ABC using
    inheritance.

    ### Ancestors (in MRO)

    * app.models.model_base.BaseLLM
    * abc.ABC

    ### Methods

    `generate_audio(self, prompt)`
    :

    `generate_image(self, prompt)`
    :

    `generate_text(self, prompt)`
    :


Module BaseMAS.app.models.model_base
====================================

Classes
-------

`BaseLLM()`
:   Helper class that provides a standard way to create an ABC using
    inheritance.

    ### Ancestors (in MRO)

    * abc.ABC

    ### Methods

    `generate_audio(self, prompt)`
    :

    `generate_image(self, prompt)`
    :

    `generate_text(self, prompt)`
    :


Module BaseMAS.app.models.model_groq
====================================

Classes
-------

`GroqModel(type: app.config.prompt_enum.AgentType, model: app.config.model_enum.ModelLLM = ModelLLM.MODEL_LLAMA)`
:   Helper class that provides a standard way to create an ABC using
    inheritance.

    ### Ancestors (in MRO)

    * app.models.model_base.BaseLLM
    * abc.ABC

    ### Methods

    `generate_audio(self, prompt)`
    :

    `generate_image(self, prompt)`
    :

    `generate_text(self, prompt)`
    :


Module BaseMAS.app.models.model_factory
=======================================

Classes
-------

`LLMFactory()`
:

    ### Static methods

    `create(model: app.config.model_enum.ModelLLM, type: app.config.prompt_enum.AgentType) ‑> app.models.model_base.BaseLLM`
    :


Module BaseMAS.app.models.model_anthropic
=========================================

Classes
-------

`AnthropicModel(type: app.config.prompt_enum.AgentType, model: app.config.model_enum.ModelLLM = ModelLLM.MODEL_CLAUDE)`
:   Helper class that provides a standard way to create an ABC using
    inheritance.

    ### Ancestors (in MRO)

    * app.models.model_base.BaseLLM
    * abc.ABC

    ### Methods

    `generate_audio(self, prompt)`
    :

    `generate_image(self, prompt)`
    :

    `generate_text(self, prompt)`
    :


Module BaseMAS.app.models.model_google
======================================

Classes
-------

`GoogleModel(type: app.config.prompt_enum.AgentType, model: app.config.model_enum.ModelLLM = ModelLLM.MODEL_GEMINI)`
:   Helper class that provides a standard way to create an ABC using
    inheritance.

    ### Ancestors (in MRO)

    * app.models.model_base.BaseLLM
    * abc.ABC

    ### Methods

    `generate_audio(self, prompt)`
    :

    `generate_image(self, prompt)`
    :

    `generate_text(self, prompt)`
    :


Module BaseMAS.app.main
=======================

Classes
-------

`Main()`
:

    ### Methods

    `run(self)`
    :
