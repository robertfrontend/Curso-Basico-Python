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