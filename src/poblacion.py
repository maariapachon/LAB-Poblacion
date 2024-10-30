from collections import namedtuple
import matplotlib.pyplot as plt
import csv


RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblacion(ruta_fichero):
    '''Lee el fichero de entrada y 
    devuelve una lista de tuplas de tipo RegistroPoblacion
    '''
    poblaciones = []
    with open(ruta_fichero, mode = 'r', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        next(lector) # Saltamos la cabecera del archivo
        for fila in lector:
            pais, codigo, anyo, censo = fila
            poblaciones.append(RegistroPoblacion(pais, codigo, int(anyo), int(censo)))
    return poblaciones

def calcula_paises(poblaciones):
    '''Toma una lista de tuplas de tipo RegistroPoblacion 
    ydelvuelve una lista ordenada alfabeticamente con 
    los nombres de los países para los que hay dato
    '''
    return sorted(set(registro.pais for registro in poblaciones))

def filtra_por_pais(poblaciones, nombre_o_codigo):
    '''Toma una lista de tuplas de tipo RegistroPoblacion, 
    y el nombre o código del país, y devuelve una lista 
    de tuplas con los datos del pais que se pasa 
    como parámetro (año y censo)
    '''
    return [registro for registro in poblaciones
            if registro.pais == nombre_o_codigo or registro.codigo == nombre_o_codigo]

def filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    '''Toma una lista de tuplas de tipo RegistroPoblacion, 
    un año y un conjunto de nombres de países, 
    y devuelve una lista de tuplas (nombre_pais, num_habitantes) 
    con los datos del año pasado como parámetro para los países 
    incluidos en el parámetro *paises*
    '''
    return[(registro.pais, registro.censo) for registro in poblaciones if registro.año == anyo and registro.pais in paises]

def muestra_evolucion_poblacion(poblaciones, nombre_o_codigo):
    '''Toma una lista de tuplas de tipo RegistroPoblacion 
    y el nombre o código de un país, y genera una gráfica 
    con la curva de evolución de la población del país dado como parámetro.
    '''
    datos = filtra_por_pais(poblaciones, nombre_o_codigo)
    if datos:
        lista_años = sorted(set(registro.año for registro in datos))
        lista_habitantes = [registro.censo for registro in sorted(datos, key=lambda x: x.año)]

        plt.title(f'Evolucion de la población de {nombre_o_codigo}')
        plt.plot(lista_años, lista_habitantes)
        plt.xlabel('Año')
        plt.ylabel('Población')
        plt.show()

def muestra_comparativa_paises_anyo(poblaciones, anyo, paises):
    '''Toma una lista de tuplas de tipo RegistroPoblacion, 
    un año y un conjunto de nombres de países y genera 
    una gráfica de barras con la población de esos países 
    en el año dado como parámetro. Los países se mostrarán en 
    el eje X en orden alfabético.
    '''
    datos = filtra_por_paises_y_anyo(poblaciones, anyo, paises)
    lista_paises = [registro[0] for registro in datos]
    lista_habitantes = [registro[1] for registro in datos]

    plt.title(f'Comparativa de poblacion en {anyo}')
    plt.bar(lista_paises, lista_habitantes)
    plt.xlabel('Países')
    plt.ylabel('Población')
    plt.show()