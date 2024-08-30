import sys
import os

from app.main import Main

if __name__ == "__main__":
    print("App:\n")

    app = Main()
    app.run()



from abc import ABC, abstractmethod

class AgenteMultimodal(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
        self.modulos = {}
        
    @abstractmethod
    def procesar_entrada(self, tipo_entrada, datos):
        pass
    
    @abstractmethod
    def generar_salida(self, tipo_salida):
        pass
    
    def agregar_modulo(self, nombre_modulo, modulo):
        self.modulos[nombre_modulo] = modulo
    
    def ejecutar_codigo(self, codigo):
        try:            
            exec(codigo)
        except Exception as e:
            print(f"Error al ejecutar el código: {e}")
        
class AgenteConversacional(AgenteMultimodal):
    
    def procesar_entrada(self, tipo_entrada, datos):
        if tipo_entrada == "texto":
            return self.modulos["procesamiento_lenguaje"].procesar(datos)
        elif tipo_entrada == "voz":
            return self.modulos["reconocimiento_voz"].procesar(datos)
    
    def generar_salida(self, tipo_salida):
        if tipo_salida == "texto":
            return self.modulos["generacion_texto"].generar()
        elif tipo_salida == "voz":
            return self.modulos["sintesis_voz"].generar()
        
class AgenteVisual(AgenteMultimodal):
    
    def procesar_entrada(self, tipo_entrada, datos):
        if tipo_entrada == "imagen":
            return self.modulos["vision_computacional"].procesar(datos)
        elif tipo_entrada == "video":
            return self.modulos["procesamiento_video"].procesar(datos)
        
    def generar_salida(self, tipo_salida):
        if tipo_salida == "imagen":
            return self.modulos["generacion_imagen"].generar()
        elif tipo_salida == "video":
            return self.modulos["generacion_video"].generar()
    
    
agente_conversacional = AgenteConversacional("Asistente")
agente_conversacional.agregar_modulo("procesamiento_lenguaje", ModuloProcesamientoLenguaje())
agente_conversacional.agregar_modulo("reconocimiento_voz", ModuloReconocimientoVoz())
agente_conversacional.agregar_modulo("generacion_texto", ModuloGeneracionTexto())
agente_conversacional.agregar_modulo("sintesis_voz", ModuloSintesisVoz())
agente_visual = AgenteVisual("Analizador de imágenes") 
agente_visual.agregar_modulo("Desarrollo", ExeceCode() )
agente_visual.ejecutar_codigo("codigo")