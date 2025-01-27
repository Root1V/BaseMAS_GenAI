from app.app import App
from app.agents.base_agent import Agent


def main():
    """
    Punto de entrada principal para la aplicación. Inicializa y ejecuta la instancia de Main.
    """
    print("START AUTONOMOUS SYSTEMS MULTI AGENT:\n")

    # app = App()
    # app.run()

    agent = Agent(goal="Tu objetivo es crear una APP WEB")
    agent.run()


if __name__ == "__main__":
    main()
