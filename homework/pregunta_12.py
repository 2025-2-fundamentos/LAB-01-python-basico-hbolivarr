"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    columns = {}

    with open("files/input/data.csv", "r") as file:
        for line in file:
            parts = line.strip().split("\t")
            key = parts[0]
            values = parts[4].strip().split(",")
            total = 0

            for value in values:
                value = int(value.split(":")[1])
                total += value
            
            if key in columns:
                columns[key] += total
            else:
                columns[key] = total
    
    return dict(sorted(columns.items()))

if __name__ == "__main__":
    print(pregunta_12())