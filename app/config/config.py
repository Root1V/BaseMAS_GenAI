import json
from typing import Any
from config.model_enum import ModelLLM

class ConfigLLM:
    _instance = None
    _config_data = None
    CONFIG_PATH = "app/config/config-ai.json"
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigLLM, cls).__new__(cls)
            cls._load_config()
            return cls._instance
    
    @classmethod
    def _load_config(cls):
        """Carga y devuelve las configuraciones  del archivo config-ai.json."""
        
        if cls._config_data is None:
            try:
                with open(cls.CONFIG_PATH, 'r') as config_file:
                    cls._config_data = json.load(config_file)
            except FileNotFoundError:
                print(f"Error: El archivo de configuración {cls.CONFIG_PATH} no se encontró.")
                cls._config_data = {}
            except json.JSONDecodeError:
                print(f"Error: El archivo {cls.CONFIG_PATH} no contiene un JSON válido.")
                cls._config_data = {}
    
    @staticmethod
    def get(model: ModelLLM, default: Any = None) -> Any:
        """Devuelve la configuración del modelo especificado por model_key."""

        if ConfigLLM._config_data is None:
            ConfigLLM._load_config()
        
        models = ConfigLLM._config_data.get('models', {})
        model_config = models.get(model.value, default)

        if model_config is None:
            raise ValueError(f"El modelo con la clave '{model.value}' no se encuentra en la configuración.")
        
        print("\nConfiguracion Model:\n", model_config)

        return model_config

