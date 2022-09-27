
#!/usr/bin/env python

import re 



def validar_id(id: str) -> bool:

    """
    Valida si la cadena de texto que nos pasan por parametro 
    denominada `id` pasa las siguientes pruebas:
        - tiene que tener 10 caracteres
        - un minimo de 3 numeros
        - un minimo de 2 mayusculas
        - No se permiten caracteres extraños 

    """

    if len(id) != 10:
        return False

    numeros = len(re.findall('\d',id))
    if numeros < 3:
        return False
    
    mayusculas = len(re.findall('[A-Z]',id))
    if mayusculas < 2:
        return False

    minusculas = len(re.findall('[a-z]',id))
   
    #por ultimo validamos que no existan caracteres extraños
    return numeros + mayusculas + minusculas == 10


def main():
    
    ids = [
        'ASD123457lop1',
        'pepe234PEP',
        'Python123x',
        'PyThon123x',
        'PyTh.n123x',
        'PyThon123xxx',
    ]
    
    for id in ids:
        print(f"{id} \t-> {validar_id(id)}")




if __name__ == "__main__":
    main()



