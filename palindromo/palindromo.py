def palindromo(palabra):

    palabra = palabra.replace(' ','') # reemplazar los espacios en blancos
    palabra = palabra.lower() # convertir el texto a minuscula
    palabra_invertida = palabra[::-1]  # invertir la palabra

    # validar si la palabra es palindromo
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    
    if es_palindromo == True:
        print("Es palindromo")
    else:
        print("No es palindromo")

if __name__ == '__main__':
    run()