def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }

    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

    poblacion_paises = {
        'Argentina': 444435,
        'Brasil': 2200123,
        'RepublicaDominicana': 113435
    }

    # print(poblacion_paises['Bolivia'])

    # imprimir llaves
    # for pais in poblacion_paises.keys():
    #     print(pais)

    # imprimir valores
    # for pais in poblacion_paises.values():
    #     print(pais)

    # imprimir valores y llaves
    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + 'M habitantes')


if __name__ == '__main__':
    run()
