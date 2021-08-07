def calculadora(type_opearcion):
    input_1 = input("Ingrese el primer numero: ")
    input_2 = input("Ingrese el segundo numero: ")

    # eliminar los espacios en blancos
    input_1 = input_1.replace(' ', '')
    input_2 = input_2.replace(' ', '')


    # validar de que sea tipo numerico
    if input_1.isnumeric() and input_2.isnumeric():
        input_1 = int(input_1)
        input_2 = int(input_2)

        if type_opearcion == 1:
            resultado =  input_1 + input_2
            lanzar_resultado('suma', resultado)


        if type_opearcion == 2:
            resultado =  input_1 - input_2
            lanzar_resultado('resta', resultado)


        if type_opearcion == 3:
            resultado =  input_1 * input_2
            lanzar_resultado('multiplicacion', resultado)

        if type_opearcion == 4:
            resultado = input_1 / input_2
            lanzar_resultado('division', resultado)

    else: 
        print('Ingrese los valores correctamente')
        run()
        return


def lanzar_resultado(tipo, resultado):
    print(f"El resultado de la {tipo} es: {resultado}")


def run():

    type_text = """
    Elige el tipo de operacion:
    1 - Suma
    2 - Resta
    3 - Multiplicacion
    4 - Division
    """

    tipo_operacion = int(input(type_text))

    calculadora(tipo_operacion)




if __name__ == '__main__':
    run()