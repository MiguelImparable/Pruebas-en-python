def Exercise_27():
    # Estructura de Conjuntos

    # No se permiten duplicados
    # Permiten todo tipo de datos
    # No importa el orden

    # Creacion de conjuntos
    set_countries = {'Col', 'Mex', 'Vol', 'H'}
    set_from_string = set('Hoola')
    set_from_numbers = {2, 3, 4, 5, 'H'}
    # _____________________________________________________________
    # Añadir
    set_countries.add('Per')
    set_countries.update({'Ecu', 'Ven'})
    # _____________________________________________________________
    # Remover
    set_countries.remove('Ven')  # Si no existe arroja error
    set_countries.discard('Per')
    # _____________________________________________________________
    # Limpiar
    set_from_numbers.clear()
    # _____________________________________________________________
    # Unir
    set_Str_Cts = set_countries.union(set_from_numbers)
    set_ALL = set_countries | set_from_string | set_from_numbers
    # _____________________________________________________________
    # Interseccionar
    set_Str_Cts_I = set_countries.intersection(set_from_string)
    set_ALL_I = set_countries & set_from_numbers & set_from_string
    # Recuerda que si interseccionamos mas de 2 es porque deben
    # tener elementos en comun entre si
    # _____________________________________________________________
    # Diferencia Simetrica
    set_Str_Cts_SY = set_countries.symmetric_difference(set_from_string)
    set_ALL_SY = set_countries ^ set_from_numbers ^ set_from_string
    # _____________________________________________________________
    # Imprimir
    print('Col' in set_countries)
    print(set_Str_Cts_I)
    print(set_ALL_I)


if __name__ == "__main__":
    Exercise_27()
