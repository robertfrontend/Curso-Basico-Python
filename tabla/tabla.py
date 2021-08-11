def imprimir_mensaje(data, tipo):

    mensaje = ""
    if tipo == tipo: 
        mensaje = f"{tipo} x {data}"

    print(mensaje)

def imprimir_tabla(data):
    for i in range(1,12):
        imprimir_mensaje(data * i, data)


def preguntar_tabla():
    text_pregunta = """
        Tabla del 1
        Tabla del 2
        Tabla del 3
        Tabla del 4
        Tabla del 5
        Tabla del 6
        Tabla del 7
        Tabla del 8
        Tabla del 9
        Tabla del 10
        Tabla del 11
        Tabla del 12

        Seleciona la tabla que quieres imprimir:
    """
    tabla =  int(input(text_pregunta))
    print(f"Tabla del {tabla}")
    imprimir_tabla(tabla)


def run():
    preguntar_tabla()


if __name__ == '__main__':
    run()