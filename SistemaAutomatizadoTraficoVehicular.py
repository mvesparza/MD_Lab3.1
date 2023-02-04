"""
Programa que que permite verificar el estado de tráfico de varias calles y lo regula en aquellas
que tienen. La regulación del tráfico tiene un costo, y se mantiene un
registro de la cantidad de regulaciones realizadas.

Autor: Marco Vinicio Esparza

Versión: v1.3
"""

def inicializar_estado_objetivo():
    """
    Proceso que crea un diccionario que representa el estado objetivo deseado para las calles.
    Parámetros:
    --------------
    No, recibe ningún parámetro de entrada

    Retorna:
    --------------
    Si, retorna un diccionario que representa el estado objetivo deseado para todas las calles.
    """
    # Inicializa un diccionario con las calles y su estado inicial en 0 (sin tráfico)
    estado_objetivo = {'Calle 1': '0', 'Calle 2': '0', 'Calle 3': '0', 'Calle 4': '0', 'Calle 5': '0', 'Calle 6': '0'}
    return estado_objetivo

def costo_inicial():
    """
    Proceso que se encarga de inicializar el costo total a 0.
    Parámetros:
    --------------
    No, recibe ningún parámetro de entrada

    Retorna:
    --------------
    Si, retorna una variable numérica entera (int) con el valor de 0, que representa el costo
    inicial.
    """
    # Inicializa el costo en 0
    costo = 0
    return costo

def ingresar_calle():
    """
    Proceso que se encarga de solicitar y recibir el nombre de una calle por parte del usuario.
    Parámetros:
    --------------
    No, recibe ningún parámetro de entrada

    Retorna:
    --------------
    Si, retorna una cadena de caracteres (string) con el nombre de la calle ingresada por el
    usuario a través de la entrada por teclado
    """
    # Solicita al usuario ingresar el nombre de la calle que desea verificar
    calle_input = input("Ingrese la calle que desea verificar: ")
    # Devuelve el nombre de la calle ingresado por el usuario
    return calle_input

def ingresar_estado_calle(calle):
    """
    Proceso que se encarga de solicitar y recibir el estado de una calle determinada por parte
    del usuario.
    Parámetros:
    --------------
    Si, recibe como parámetro de entrada una cadena de caracteres (string) con el nombre de la
    calle cuyo estado se desea verificar.

    Retorna:
    --------------
    Si, retorna una cadena de caracteres (string) con el estado de la calle ingresado por el
    usuario, que puede ser "0" o "1"
    """
    # Solicita al usuario ingresar el estado de la calle especificada (0 para sin tráfico y 1 para tráfico)
    estado_input = input("Ingrese el estado de la calle " + calle + " (0 para sin tráfico y 1 para tráfico): ")
    # Devuelve el estado de la calle ingresado por el usuario
    return estado_input

def verificar_calle(calle, estado_calle, estado_objetivo, costo):
    """
    Proceso que verifica el estado de la calle en cuestión y si está en tráfico (estado_calle = '1'),
    e incrementa el costo en una unidad.
    Parámetros:
    --------------
    Si, recibe 4 parámetros:
    calle: una string que representa el nombre de una calle.
    estado_calle: una string que representa el estado de tráfico en una calle, donde "0" indica
    sin tráfico y "1" indica con tráfico.
    estado_objetivo: un diccionario que asocia el nombre de una calle con su estado de tráfico.
    costo: un número que representa el costo actual de la regulación del tráfico.

    Retorna:
    --------------
    Si, retorna 2 valores:
    estado_objetivo: un diccionario que asocia el nombre de una calle con su estado de tráfico
    actualizado.
    costo: un número que representa el costo actualizado de la regulación del tráfico.
    """
    # Verifica si la calle tiene tráfico o no
    if estado_calle == '1':
        print("La calle " + calle + " tiene tráfico.")
        # Si la calle tiene tráfico, se actualiza el estado en el diccionario
        estado_objetivo[calle] = '0'
        # Se aumenta el costo en 1
        costo += 1
        print("Se está regulando el tráfico en la calle " + calle)
        print("Costo actual: " + str(costo))
    else:
        print("La calle " + calle + " no tiene tráfico.")
        print("No se requiere acción.")
        print("Costo actual: " + str(costo))
    # Se devuelve el estado actual y el costo actual
    return estado_objetivo, costo

if __name__ == '__main__':
    # inicializar el programa
    print("********* SISTEMA AUTOMATIZADO DE TRÁFICO VEHICULAR *********")
    # iniciar bucle para repetir el proceso las veces que el usuario quiera
    while(True):  

        # Inicializa el estado objetivo con valores iniciales
        estado_objetivo = inicializar_estado_objetivo()
        # Imprime el estado objetivo inicial
        print("Estado objetivo deseado: " + str(estado_objetivo))
        # Inicializa el costo a 0
        costo = costo_inicial()

        # Bandera para continuar o detener el ciclo
        continuar = True
        # Ciclo para ingresar y verificar estados de calles
        while continuar:
            # Ingresa el nombre de la calle
            calle = ingresar_calle()
            # Ingresa el estado de la calle
            estado_calle = ingresar_estado_calle(calle)
            # Verifica el estado de la calle y actualiza el costo
            estado_objetivo, costo = verificar_calle(calle, estado_calle, estado_objetivo, costo)

            # Pregunta al usuario si desea ingresar otra calle
            respuesta = input("¿Desea ingresar otra calle? (si/no) ")
            # Si la respuesta es no, detiene el ciclo
            if respuesta.lower() == "no":
                continuar = False
        
        # Imprime el estado objetivo final y el costo total
        print("Estado objetivo final: " + str(estado_objetivo))
        print("Medida de desempeño: " + str(costo))

        
        # preguntar si quiere volver a usar el programa  
        repetirProceso = input("¿Repetir proceso? (si/no): ")
        if repetirProceso.lower() != "si":
            print("********** FIN DEL PROCESO **********")
            # detener el bucle por completo
            break