# main.py

def saludo(nombre: str) -> str:
    """
    Retorna un saludo personalizado.
    """
    return f"Hola, {nombre}!"

if __name__ == "__main__":
    mensaje = saludo("Mundo")
    print(mensaje)
