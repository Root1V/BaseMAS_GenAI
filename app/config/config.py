import json
from typing import Any
from app.config.model_enum import ModelLLM


class ConfigLLM:
    """
    Clase singleton para gestionar la configuración de modelos de lenguaje.

    Esta clase carga la configuración desde un archivo JSON y proporciona
    métodos para acceder a la configuración de modelos específicos.
    """

    _instance = None
    _config_data = None
    CONFIG_PATH = "app/config/config-ai.json"

    def __new__(cls):
        """
        Crea una nueva instancia de ConfigLLM si no existe, o devuelve la instancia existente.

        Returns:
            ConfigLLM: La instancia única de la clase.
        """
        if cls._instance is None:
            cls._instance = super(ConfigLLM, cls).__new__(cls)
            cls._load_config()
            return cls._instance

    @classmethod
    def _load_config(cls):
        """Carga y devuelve las configuraciones del archivo config-ai.json.

        Este método se encarga de abrir el archivo de configuración y cargar
        su contenido en formato JSON. Maneja excepciones en caso de que el
        archivo no exista o contenga un JSON inválido.
        """
        if cls._config_data is None:
            try:
                with open(cls.CONFIG_PATH, "r") as config_file:
                    cls._config_data = json.load(config_file)
            except FileNotFoundError:
                print(
                    f"Error: El archivo de configuración {cls.CONFIG_PATH} no se encontró."
                )
                cls._config_data = {}
            except json.JSONDecodeError:
                print(
                    f"Error: El archivo {cls.CONFIG_PATH} no contiene un JSON válido."
                )
                cls._config_data = {}

    @staticmethod
    def get(model: ModelLLM, default: Any = None) -> Any:
        """Devuelve la configuración del modelo especificado por model_key.

        Args:
            model (ModelLLM): El modelo para el cual se desea obtener la configuración.
            default (Any, optional): Valor por defecto a devolver si no se encuentra la configuración.

        Returns:
            Any: La configuración del modelo solicitado.

        Raises:
            ValueError: Si el modelo no se encuentra en la configuración.
        """
        if ConfigLLM._config_data is None:
            ConfigLLM._load_config()

        models = ConfigLLM._config_data.get("models", {})
        model_config = models.get(model.value, default)

        if model_config is None:
            raise ValueError(
                f"El modelo con la clave '{model.value}' no se encuentra en la configuración."
            )

        print("\nConfiguracion Model:\n", model_config)

        return model_config
