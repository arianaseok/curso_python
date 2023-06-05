import csv
#Crear un diccionario que permita almacenar la información del archivo convertido.
def cargar_diccionario():
    """
    Esta funcion se encarga de importar los datos de un archivo csv en la variable "archivo",
    y la funcion devuelve un diccionario con los datos presentes en "archivo".
    Autor/a: Fernandez Laura, Daniela.
    """
    archivo = open(r"/home/arianaseok/Escritorio/Clase 13/recursosPython.csv", "r")
    # Inicializo variables
    dni = 0
    nombre = 1
    apellido = 2
    email = 3
    f_nacimiento = 4
    lugar_r = 5
    
    # Inicializo un diccionario vacio
    datos_personales = {"DNI": [],
            "Nombre": [],
            "Apellido": [],
            "Email": [],
            "Fecha de nacimiento": [],
            "Lugar de residencia": []
            }

    lista_datos = [dato.split(",") for dato in archivo]

    for dato in range(1,len(lista_datos)):
        datos_personales["DNI"].append(lista_datos[dato][dni])
        datos_personales["Nombre"].append(lista_datos[dato][nombre])
        datos_personales["Apellido"].append(lista_datos[dato][apellido])
        datos_personales["Email"].append(lista_datos[dato][email])
        datos_personales["Fecha de nacimiento"].append(lista_datos[dato][f_nacimiento])
        datos_personales["Lugar de residencia"].append(lista_datos[dato][lugar_r].replace("\n",""))
    
    archivo.close()
    return datos_personales

def palabra_sin_tilde(palabra):
    """
    La funcion recibe un parametro de tipo str.
    Y retorna la variable sin tilde.
    Autor/a: Fernandez Laura, Daniela.
    """
    vocales_con_tilde= "áéíóú"
    vocales = "aeiou"
    for posicion in range(len(vocales)):
        palabra = palabra.replace(vocales_con_tilde[posicion], vocales[posicion])
    return palabra

def mostrar_resultados(posiciones, datos_personales):
    """
    La funcion recibe dos parametros, el primero es una variable de tipo
    list, y la segunda es un diccionario inicializado.
    La funcion muestra por pantalla los resultados.
    Autor/a: Fernandez Laura, Daniela.
    """
    i = 0
    while (i < len(posiciones)):
        print("-------------------------------------------------")
        print("DATOS:\n")
        for datos, info in datos_personales.items():
            print(f"- {datos}: {info[posiciones[i]]}")
        print("-------------------------------------------------\n")
        i+= 1

def cargar_posiciones(datos_personales, dato_buscar, clave):
    """
    La funcion recibe 3 parametros: 1 diccionario inicializado y dos
    variables de tipo str.
    La funcion devuelve una lista con componentes de tipo int.
    Autor/a: Fernandez Laura, Daniela.
    """
    posiciones = [indice for indice, dato in enumerate(datos_personales[clave])\
                        if dato == dato_buscar]
    return posiciones

# Realizar un filtro que permita visualizar los datos de las personas cuyo apellido es "Gómez".
def filtrar_apellido(datos_personales):
    """
    La funcion recibe por parametro un diccionario ya inicializado.
    La funcion muestra por pantalla los datos de dicho apellido.
    Autor/a: Fernandez Laura, Daniela.
    """
    print("Buscador de personas dependiendo de su apellido")
    persona_a_buscar = input("\nIngrese el apellido de la persona a buscar: ").capitalize()
    persona_a_buscar = palabra_sin_tilde(persona_a_buscar)
    clave = 'Apellido'
    if (persona_a_buscar in datos_personales['Apellido']):
        posiciones = cargar_posiciones(datos_personales, persona_a_buscar, clave)
        mostrar_resultados(posiciones, datos_personales)
    else:
        print("No se ha encontrado personas con el dato ingresado.\n")
        print("---------------------------------------------------")

def buscar_posicion_provincia(datos_personales):
    """
    La funcion recibe por parametro un diccionario ya inicializado.
    La funcion retorna una lista con componentes de tipo int.
    Autor/a: Fernandez Laura, Daniela.
    """
    print("\nCarga de datos al archivo Datos.csv dependiendo de la provincia ingresada")
    persona_a_buscar = input("\nIngrese el nombre provincia: ").title()
    persona_a_buscar = palabra_sin_tilde(persona_a_buscar)
    clave = 'Lugar de residencia'
    if (persona_a_buscar in datos_personales['Lugar de residencia']):
        posiciones = cargar_posiciones(datos_personales, persona_a_buscar, clave)
    else:
        print("\nNo se ha encontrado personas con el dato ingresado.")
    return posiciones

def cargar_datos(datos_personales, posiciones):
    """
    La funcion recibe dos parametros: un diccionario ya inicializado y una lista.
    La funcion retorna una lista de listas.
    Autor/a: Fernandez Laura, Daniela.
    """
    personas = [["DNI", "Nombre", "Apellido", "Email", "Fecha de nacimiento", "Lugar de residencia"]]
    i = 0
    while(i < len(posiciones)):
        persona = [datos_personales["DNI"][posiciones[i]], 
                    datos_personales["Nombre"][posiciones[i]], 
                    datos_personales["Apellido"][posiciones[i]],
                    datos_personales["Email"][posiciones[i]],
                    datos_personales["Fecha de nacimiento"][posiciones[i]],
                    datos_personales["Lugar de residencia"][posiciones[i]]]
        personas.append(persona)
        i += 1
    return personas

# Generar un archivo csv que permita guardar los datos de las personas que viven en "Córdoba" o en "Santa Fe".
def cargar_csv(personas):
    """
    La funcion recibe un parametro el cual es de tipo list.
    La funcion crea un archivo csv y carga los datos de la lista recibida por parametro.
    Autor/a: Fernandez Laura, Daniela.
    """
    # Vamos a crear un archivo
    datos = open(r"/home/arianaseok/Escritorio/Clase 13/Datos.csv", "w")
    writer = csv.writer(datos)
    writer.writerows(personas)
    print("\nCarga Exitosa!")


# Bloque Principal
def main():
    datos_personales = cargar_diccionario()
    filtrar_apellido(datos_personales)
    posiciones = buscar_posicion_provincia(datos_personales)
    personas = cargar_datos(datos_personales, posiciones)
    cargar_csv(personas)

main()
