# operadores + / * - % igual que javascript

# variable
numero1 = '10'
numero2 = '5'
numero_decimal = 2.5


# convertir texto a numero
numero1 = int(numero1)
numero2 = int(numero2)
print(numero1 + numero2)



# decimal normal
print(numero_decimal, 'numero decimal')

#convertir decial a string
numero_decimal = str(numero_decimal)
print(numero_decimal + 'hola wortld', 'numero decimal a texto')


print("-----operadores logicos------")

# operadores logicos and
# and evalua todas las variables que contengan el valor de verdadero
# or es estudiante (o) trabaja , devolvera true porque alguna de las dos es true
# not es negaciona un valor, es como ! en javascript
es_estudiante = True
trabaja = False

print(es_estudiante and trabaja)
print(es_estudiante or trabaja)
print(not trabaja)


print("-----operadores de comparacion------")
# == igual a que
# != diferente de
# > mayor que
# < menor que
# >= mayor o igual que
# <= menor o igual que



# variable.upper() = 'todos los caracteres en MAYÚSCULAS'
# variable.capitalize() = 'solo la primera en MAYÚSCULA'
# variable.lower() = 'todos los caracteres en minúscula'
# variable.strip() = 'eliminar espacios basura del string'
# variable.replace('caractera a cambiar', 'caracter por poner') = remplazar caracter


# FUNCIONES BILT IN
# aquellas que son propias del lenguaje y que no tenemos que crearlas, solo invocarlas.

# len()
# print()
# input()




# Trabajando con texto: slices19/32


# Explicación:
# Los slices, traducidos al español como “rebanadas”, nos permiten dividir los caracteres de un string de múltiples formas. A continuación, un ejemplo de estos:

# nombre = "Francisco"
# nombre
# "Francisco"
# nombre[0 : 3) //Arranca desde el primer índice hasta llegar antes del 3° índice.
# "Fra"
# nombre[:3] //Va desde el principio hasta antes de llegar del 3° índice. Cómo no hay ningún parámetro en el primer lugar, se interpreta que arranca desde el principio.
# "Fra"
# nombre[1:7] //Arranca desde el índice 1 hasta llegar antes del 7.
# "rancis"
# nombre[1:7:2] //Arranca desde el índice 1 hasta llegar antes del 7, pero pasos de 2 en 2, ya que eso es lo que nos indica el 3! parámetro, el cual es 2.
# nombre[1::3] //Arranca desde el índice 1 hasta el final del string (al no haber ningún 2° parámetro, significa que va hasta el final), pero en pasos de 3 en 3.
# "rcc"
# nombre[::-1]  //Al no haber parámetro en los 2 primeros lugares, se interpreta que se arranca desde el inicio hasta el final, pero en pasos de 1 en 1 con la palabra al revés, porque es -1.
# "ocsicnarF"
