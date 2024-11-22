from clases import Detector, Mutador, Radiacion, Virus, Sanador



# Secuencia a utilizar
# matriz = [
#     "TTTTCG", "TCTTGA", "CACGAT", "TAGCTA", "GACGGA", "TACAAA"
# ]
# matriz_convertida = [
#     ["T", "T", "T", "T", "C", "G"],
#     ["T", "C", "T", "T", "G", "A"],
#     ["C", "A", "C", "G", "A", "T"],
#     ["T", "A", "G", "C", "T", "A"],
#     ["G", "A", "C", "G", "G", "A"],
#     ["T", "A", "C", "A", "A", "A"]
# ]
# imprimir_secuencia(matriz)

# detector = Detector()

# detector.verificar_base_nitrogenada(matriz)
# if detector.detectar_mutantes(matriz):
#     print("Mutante detectado")
# else:
#     print("No se detectaron mutaciones")
    
#     print("Mutante detectado" if detector.detectar_mutantes(matriz) else "No se detectaron mutantes")

# print("")

# # Aqui podemos ver las bases nitrogenadas repetidas
# simbolos = detector.get_simbolos_mutante()
# print(simbolos)
# print("")

# # De esta forma se pueden obtener las posiciones de las mutaciones
# # matriz[posicion[0]][posicion[1]] mostraria el valor de la celda
# # posicion[0] o posicion[1] mostrarian el valor de filas y columnas de cada mutacion
# print("Todas las mutaciones encontradas y almacenadas")
# posiciones = detector.get_posiciones_repetidas()
# for repeticion in posiciones:
#     print(repeticion)
#     for posicion in repeticion:
#         print(matriz[posicion[0]][posicion[1]], end=", ")
#     print("\n")


# mutador = Mutador("T", matriz)

# # radiacion= Radiacion(["A","C","G","T"],matriz)
# # posicion_inicial=(1,1)
# # radiacion.crear_mutante(["A","C","G","T"], posicion_inicial, "H")
# base_nitrogenada = ["A","C","G","T"]

# radiacion = Radiacion(base_nitrogenada, matriz_convertida)

# # crear mutante utiliza los parametros:

# radiacion.crear_mutante("A", [0, 0], "V") # base nitrogenada, posicion, direccion
# # radiacion.getAll()

# imprimir_secuencia(radiacion._matriz)

# virus = Virus(base_nitrogenada, matriz_convertida)
# virus.crear_mutante("T", [5, 0])
# imprimir_secuencia(virus._matriz)

# sanador = Sanador()
# imprimir_secuencia(sanador.sanar_mutantes(matriz_convertida))


#  -------------------------- Funciones--------------------------------

# Imprime el arreglo que se envie por parametro
def imprimir_secuencia(array):
    print("Secuencia ingresada:")
    for x in array:
        print("  ".join(x))
        
def verificar_secuencia(matriz):
    caracteres_validos = {"A", "C", "G", "T"}
    return all(letra in caracteres_validos for letra in matriz)


#Ingresar la matriz de ADN
def ingresar_matriz():
    matriz = []
    contador = 1
    while len(matriz) < 6:
        print()
        entrada = input(f"Ingrese la secuencia {contador} del ADN:")
        # Verficar matriz
        if not verificar_secuencia(entrada):
            print("Solo puede ingresar las bases: A, C, G y T", end="\n")
        elif len(entrada) != 6:
            print("La secuencia debe tener 6 caracteres", end="\n")
        else:
            matriz.append(entrada)
            contador += 1
    print("Matriz de ADN ingresada exitosamente")
    return matriz
 
def detectar_mutaciones(matriz) -> None:
    detector = Detector(matriz)
    if detector.detectar_mutantes(matriz):
        print("------------------------------")
        print("Hay mutaciones en: ")
        posiciones = detector.get_posiciones_repetidas()
        for repeticion in posiciones:
            print(f"{repeticion}: {matriz[repeticion[0][0]][repeticion[0][1]]}")


def mutar_adn(matriz) -> None:
    #Pedir al usuario que escoja una radiacion o virus
    pass

def sanar_adn() -> None:
    pass



# --------------------------Main---------------------------------
print("------------------------------")
print("Programa ADN")

#matriz = ingresar_matriz()
matriz = [
    "TTTTCG", "TCTTGA", "CACGAT", "TAGCTA", "GACGGA", "TACAAA"
]
opcion = -1
        
while opcion != 0:
    print("------------------------------", end="")
    try:
        opcion = int(input("""
          Que desea hacer?
          1) Detectar mutaciones
          2) Mutar el ADN
          3) Sanar el ADN
          0) Salir
          Escoja una opcion: """))
        if type(opcion) != int:
            raise TypeError("Debe ingresar un numero")
        elif not opcion in [1,2,3,0]:
            raise TypeError("Debe ingresar un numero entre 0 y 3")
        else:
            if opcion == 0: break
            #codigo

            if opcion == 1:
                detectar_mutaciones(matriz)
            elif opcion == 2:
                mutar_adn(matriz)
            elif opcion == 3:
                sanar_adn(matriz)
            else:
                raise TypeError("Debe ingresar un numero")
            
            #codigo
    except TypeError as e:
        print("------------------------------")
        print(e)
    except ValueError:
        print("------------------------------")
        print("Debe ingresar un numero")
        
print("Saliendo del programa....")
    
#imprimir_secuencia(matriz)



