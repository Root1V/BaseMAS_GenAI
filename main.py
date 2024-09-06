from app.main import Main


def main():
    """
    Punto de entrada principal para la aplicación. Inicializa y ejecuta la instancia de Main.
    """
    print("START AUTONOMOUS SYSTEMS MULTI AGENT:\n")

    app = Main()
    app.run()


if __name__ == "__main__":
    main()
