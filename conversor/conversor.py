def convertidor_moneda(moneda, tipo):
    tipo = tipo.capitalize()

    print(f"Elegiste peso {tipo}")

    pesos = input(f"Cuantos pesos {tipo} tienes?: ")
    pesos = float(pesos)

    valor_dolar = moneda

    dolares = pesos / valor_dolar

    dolares = round(dolares, 2)
    dolares = str(dolares)

    print(f"Tienes $ {dolares} dolares")

menu = """
Bienvenido al conversor de monedas 🚀

1 - Pesos colmbianos
2 - Pesos dominicanos
3 - Pesos mexicanos

Elige una opcion: """

opcion = int(input(menu))


if opcion == 1:
    convertidor_moneda(3875, "colmbianos")

elif opcion == 2:
    convertidor_moneda(56.25, "dominicanos")

elif opcion == 3:
    convertidor_moneda(24, "mexicanos")

else:
    print("Ingresa una ocpion correcta por favor")



# def convertidor_moneda(moneda):
#     pass



# tipo =  input("Peso - dolar: 1 || Dolar - Peso: 2  ?")
# tipo = int(tipo)

# if tipo == 1:
#     print('peso dominicano a dolar')

#     pesos = input("Cuantos pesos Dominicanos tienes?: ")
#     pesos = float(pesos)

#     valor_dolar = 56.25
#     dolares = pesos / valor_dolar
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print(f"Tienes $ {dolares} dolares")

# if tipo == 2: 
#     print('dolar a peso dominicano')
#     # preguntar cuantos dolares tiene al usuario
#     dolar = input("Cuantos dolares tienes?: ")
#     dolar = float(dolar)

#     # valor del peso dominicano
#     valor_peso = 56.25
#     # operacion de conversion
#     pesos = dolar * valor_peso

#     # redondear valor
#     pesos = round(pesos, 2)

#     # convertir a string
#     pesos = str(pesos)

#     print(f"Tienes $ {pesos} pesos dominicanos")
