Project BaseMAS: Multi Agent Systems
=================

## Configuración

Antes de ejecutar la aplicación, asegúrate de configurar las siguientes variables de entorno:

file: `.env`

```bash
    OPENAI_API_KEY=
    GROQ_API_KEY=
    ANTHROPIC_API_KEY=
    GEMINI_API_KEY=
```

## Ejecución

Para ejecutar la aplicación, simplemente usa el siguiente comando:

```bash
python app.py
```

Namespace BaseMAS
=================

Sub-modules
-----------
* BaseMAS.app
* BaseMAS.main
* BaseMAS.test


Module BaseMAS.app.app
======================

Classes
-------

`App()`
:   Clase principal que gestiona la creación y ejecución de modelos de lenguaje.

    Esta clase es responsable de instanciar varios modelos de lenguaje y generar
    texto basado en solicitudes específicas. Facilita la interacción con diferentes
    tipos de modelos de inteligencia artificial.

    Inicializa una nueva instancia de la clase Main.

    Este constructor no requiere parámetros y no realiza ninguna acción
    adicional en la inicialización.

    ### Methods

    `run(self)`
    :   Ejecuta el proceso de generación de texto utilizando diferentes modelos de lenguaje.

        Este método crea instancias de varios modelos de lenguaje a través de la
        fábrica de modelos y genera respuestas basadas en solicitudes específicas.
        Luego, imprime las respuestas generadas por cada modelo en la consola.


Module BaseMAS.app.tools.tool_web_search
========================================


Module BaseMAS.app.util.helpers
===============================


Module BaseMAS.app.config.model_enum
====================================

Classes
-------

`ModelLLM(value, names=None, *, module=None, qualname=None, type=None, start=1)`
:   Enum que representa diferentes modelos de lenguaje disponibles.

    Cada miembro de esta enumeración corresponde a un modelo de lenguaje específico,
    facilitando la referencia y uso de estos modelos en otras partes del código.

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
:   Enum que representa los diferentes tipos de agentes y sus archivos de configuración asociados.

    Cada miembro de esta enumeración agrupa los archivos de configuración del sistema y del usuario
    para cada tipo de agente, facilitando su acceso y gestión en el sistema.

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
:   Enum que representa los diferentes archivos de configuración para cada tipo de agente.

    Cada miembro de esta enumeración corresponde a un archivo específico que contiene
    información o configuraciones para los agentes en el sistema.

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
:   Clase que maneja la carga de prompts desde archivos de texto.

    Esta clase permite cargar prompts específicos según su enumeración y tipo de agente, facilitando la gestión de
    contenido en aplicaciones que requieren interacción con modelos de lenguaje.

    ### Class variables

    `PROMPT_DIR`
    :

    ### Methods

    `get_prompts_type(self, type: app.config.prompt_enum.AgentType)`
    :   Devuelve los prompts correspondientes a un tipo de agente.

        Args:
            type (AgentType): El tipo de agente para el cual se obtienen los prompts.

        Returns:
            tuple: Una tupla que contiene el contenido del prompt del sistema y del usuario.

    `load_prompt(self, prompt: app.config.prompt_enum.PromptEnum)`
    :   Carga y devuelve el contenido del archivo de prompt correspondiente.

        Args:
            prompt (PromptEnum): El enumerado que representa el prompt a cargar.

        Returns:
            str: El contenido del archivo de prompt.

        Raises:
            FileNotFoundError: Si el archivo de prompt no existe en la ruta especificada.


Module BaseMAS.app.config.config
================================

Classes
-------

`ConfigLLM()`
:   Clase singleton para gestionar la configuración de modelos de lenguaje.

    Esta clase carga la configuración desde un archivo JSON y proporciona
    métodos para acceder a la configuración de modelos específicos.

    ### Class variables

    `CONFIG_PATH`
    :

    ### Static methods

    `get(model: app.config.model_enum.ModelLLM, default: Any = None) ‑> Any`
    :   Devuelve la configuración del modelo especificado por model_key.

        Args:
            model (ModelLLM): El modelo para el cual se desea obtener la configuración.
            default (Any, optional): Valor por defecto a devolver si no se encuentra la configuración.

        Returns:
            Any: La configuración del modelo solicitado.

        Raises:
            ValueError: Si el modelo no se encuentra en la configuración.


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

Classes
-------

`Agente()`
:   Clase base para todos los agentes.

    Esta clase proporciona una estructura común y métodos básicos que son
    compartidos por todos los tipos de agentes en el sistema. Los agentes
    pueden ser utilizados para realizar diversas tareas dentro de un
    entorno específico, facilitando la extensión y personalización de su
    comportamiento.


Module BaseMAS.app.models.model_openai
======================================

Classes
-------

`OpenAIModel(type: app.config.prompt_enum.AgentType, model: app.config.model_enum.ModelLLM = ModelLLM.MODEL_GPT)`
:   Clase que representa un modelo de OpenAI, extendiendo la funcionalidad
    de un modelo de lenguaje base. Se encarga de configurar el cliente de OpenAI
    y gestionar la generación de texto, audio e imágenes.

    Inicializa el modelo de OpenAI con un tipo de agente y un modelo específico.

    Args:
        type (AgentType): Tipo de agente que define el comportamiento del modelo.
        model (ModelLLM, opcional): Modelo de lenguaje a utilizar, por defecto es MODEL_GPT.

    ### Ancestors (in MRO)

    * app.models.model_base.BaseLLM
    * abc.ABC

    ### Methods

    `generate_audio(self, prompt)`
    :   Genera audio a partir del prompt proporcionado.

        Este método es un placeholder para la implementación de la generación de audio.

        Args:
            prompt (str): El texto de entrada que se utilizará para generar el audio.

    `generate_image(self, prompt)`
    :   Genera una imagen a partir del prompt proporcionado.

        Este método es un placeholder para la implementación de la generación de imágenes.

        Args:
            prompt (str): El texto de entrada que se utilizará para generar la imagen.

    `generate_text(self, prompt)`
    :   Genera texto utilizando el modelo de OpenAI basado en el prompt proporcionado.

        Este método envía el prompt al modelo y retorna la respuesta generada.

        Args:
            prompt (str): El texto de entrada que se utilizará para generar la respuesta.

        Returns:
            str: El contenido del mensaje generado por el modelo.


Module BaseMAS.app.models.model_base
====================================

Classes
-------

`BaseLLM()`
:   Clase base para todos los agentes de modelos de lenguaje (LLM).

    Esta clase define la interfaz para la generación de texto, imágenes y audio.
    Las subclases deben implementar los métodos abstractos para proporcionar
    funcionalidades específicas de generación de contenido.

    Inicializa una instancia de la clase BaseLLM.

    Este constructor llama al constructor de la clase base.

    ### Ancestors (in MRO)

    * abc.ABC

    ### Methods

    `generate_audio(self, prompt)`
    :   Genera audio basado en el prompt proporcionado.

        Args:
            prompt (str): El texto de entrada que se utilizará como base para
            la generación del audio.

        Raises:
            NotImplementedError: Si la subclase no implementa este método.

    `generate_image(self, prompt)`
    :   Genera una imagen basada en el prompt proporcionado.

        Args:
            prompt (str): El texto de entrada que se utilizará como base para
            la generación de la imagen.

        Raises:
            NotImplementedError: Si la subclase no implementa este método.

    `generate_text(self, prompt)`
    :   Genera texto basado en el prompt proporcionado.

        Args:
            prompt (str): El texto de entrada que se utilizará como base para
            la generación del texto.

        Raises:
            NotImplementedError: Si la subclase no implementa este método.


Module BaseMAS.app.models.model_groq
====================================

Classes
-------

`GroqModel(type: app.config.prompt_enum.AgentType, model: app.config.model_enum.ModelLLM = ModelLLM.MODEL_LLAMA)`
:   Clase que representa un modelo de lenguaje Groq, heredando de BaseLLM.

    Esta clase permite la generación de texto, audio e imágenes utilizando el modelo
    especificado y proporciona prompts configurados según el tipo de agente.

    Inicializa el modelo Groq con la configuración adecuada y los prompts.

    Args:
        type (AgentType): Tipo de agente que define el comportamiento del modelo.
        model (ModelLLM, opcional): El modelo a utilizar, por defecto es MODEL_LLAMA.

    ### Ancestors (in MRO)

    * app.models.model_base.BaseLLM
    * abc.ABC

    ### Methods

    `generate_audio(self, prompt)`
    :   Genera audio a partir de un prompt dado.

        Args:
            prompt (str): El texto de entrada para generar el audio.

        Returns:
            None: Esta función no devuelve ningún valor.

    `generate_image(self, prompt)`
    :   Genera una imagen a partir de un prompt dado.

        Args:
            prompt (str): El texto de entrada para generar la imagen.

        Returns:
            None: Esta función no devuelve ningún valor.

    `generate_text(self, prompt)`
    :   Genera texto a partir de un prompt dado utilizando el modelo Groq.

        Args:
            prompt (str): El texto de entrada para generar la respuesta.

        Returns:
            str: La respuesta generada por el modelo.


Module BaseMAS.app.models.model_factory
=======================================

Classes
-------

`LLMFactory()`
:   Clase responsable de la creación de instancias de modelos de lenguaje (LLM)
    basados en el tipo de modelo y el tipo de agente especificados.

    Esta fábrica permite la instancia de diferentes modelos de LLM, facilitando
    la integración y el uso de múltiples proveedores de modelos en una aplicación.

    ### Static methods

    `create(model: app.config.model_enum.ModelLLM, type: app.config.prompt_enum.AgentType) ‑> app.models.model_base.BaseLLM`
    :   Crea una instancia de un modelo de lenguaje basado en el tipo de modelo
        y el tipo de agente proporcionados.

        Args:
            model (ModelLLM): El tipo de modelo de lenguaje que se desea crear.
            type (AgentType): El tipo de agente que se utilizará con el modelo.

        Returns:
            BaseLLM: Una instancia del modelo de lenguaje correspondiente.

        Raises:
            ValueError: Si el modelo proporcionado no es compatible o no está
            soportado por la fábrica.


Module BaseMAS.app.models.model_anthropic
=========================================

Classes
-------

`AnthropicModel(type: app.config.prompt_enum.AgentType, model: app.config.model_enum.ModelLLM = ModelLLM.MODEL_CLAUDE)`
:   Clase que representa un modelo de lenguaje basado en la API de Anthropic.
    Hereda de BaseLLM y proporciona métodos para generar texto, audio e imagen
    utilizando el modelo Claude.

    Attributes:
        config (dict): Configuración del modelo, incluyendo nombre, max_tokens y temperatura.
        client (Anthropic): Cliente para interactuar con la API de Anthropic.
        SYS_PROMPT (str): Prompt del sistema para el modelo.
        USER_PROMPT (str): Prompt del usuario para el modelo.

    Inicializa una instancia del modelo Anthropic.

    Args:
        type (AgentType): Tipo de agente que determina el tipo de prompt a utilizar.
        model (ModelLLM, optional): Modelo a utilizar, por defecto es MODEL_CLAUDE.

    ### Ancestors (in MRO)

    * app.models.model_base.BaseLLM
    * abc.ABC

    ### Methods

    `generate_audio(self, prompt)`
    :   Genera audio a partir del prompt proporcionado.

        Args:
            prompt (str): El texto de entrada para la generación de audio.

    `generate_image(self, prompt)`
    :   Genera una imagen a partir del prompt proporcionado.

        Args:
            prompt (str): El texto de entrada para la generación de imagen.

    `generate_text(self, prompt)`
    :   Genera texto utilizando el modelo Claude basado en el prompt proporcionado.

        Args:
            prompt (str): El texto de entrada para el modelo.

        Returns:
            str: Texto generado por el modelo como respuesta al prompt.


Module BaseMAS.app.models.model_google
======================================

Classes
-------

`GoogleModel(type: app.config.prompt_enum.AgentType, model: app.config.model_enum.ModelLLM = ModelLLM.MODEL_GEMINI)`
:   Clase que representa un modelo de lenguaje generativo de Google.

    Esta clase extiende la funcionalidad de BaseLLM para interactuar con el modelo generativo de Google,
    configurando el cliente y los prompts necesarios para la generación de texto, audio e imagen.

    Inicializa una instancia de GoogleModel.

    Configura la API de Google y establece los prompts del sistema y del usuario basados en el tipo de agente.

    Args:
        type (AgentType): El tipo de agente que determina el comportamiento del modelo.
        model (ModelLLM, opcional): El modelo a utilizar, por defecto es MODEL_GEMINI.

    ### Ancestors (in MRO)

    * app.models.model_base.BaseLLM
    * abc.ABC

    ### Methods

    `generate_audio(self, prompt)`
    :   Genera audio a partir del texto proporcionado.

        Este método está destinado a implementar la lógica para la generación de audio.
        Actualmente solo imprime el prompt de entrada.

        Args:
            prompt (str): El texto de entrada para la generación de audio.

    `generate_image(self, prompt)`
    :   Genera una imagen a partir del texto proporcionado.

        Este método está destinado a implementar la lógica para la generación de imágenes.
        Actualmente solo imprime el prompt de entrada.

        Args:
            prompt (str): El texto de entrada para la generación de imagen.

    `generate_text(self, prompt)`
    :   Genera texto utilizando el modelo generativo de Google.

        Combina el prompt del sistema y el prompt del usuario para crear un prompt completo que se envía al modelo.

        Args:
            prompt (str): El texto de entrada proporcionado por el usuario para la generación de texto.

        Returns:
            str: El texto generado por el modelo.


Module BaseMAS.main
===================

Functions
---------

`main()`
:   Punto de entrada principal para la aplicación. Inicializa y ejecuta la instancia de Main.
