from clases import Detector, Radiacion, Virus, Sanador

# Imprime el arreglo que se envie por parametro
def imprimir_secuencia(array):
    print("Secuencia ingresada:")
    for x in array:
        print("  ".join(x))
        
def verificar_secuencia(matriz, secuencia = {"A", "C", "G", "T"}):
    caracteres_validos = {"A", "C", "G", "T"}
    return all(letra in caracteres_validos for letra in matriz)

def modificar_matriz(matriz):
    return [list(fila) for fila in matriz]

def modificar_matriz_inversa(matriz_inversa):
    return ["".join(fila) for fila in matriz_inversa]

def mostrar_mensaje(mensaje):
    print("------------------------------")
    print(mensaje)
    print("------------------------------")

def verificar_letra(letra, arreglo = ["A","C","G","T","X"]):
    return letra in arreglo

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
        mostrar_mensaje("Mutaciones encontradas")
        posiciones = detector.get_posiciones_repetidas()
        for repeticion in posiciones:
            print(f"{repeticion}: {matriz[repeticion[0][0]][repeticion[0][1]]}")
    else:
        mostrar_mensaje("No se encontraron mutaciones")


def mutar_adn(matriz) -> None:
    #Pedir al usuario que escoja una radiacion o virus    
    mostrar_mensaje("Mutar ADN")
    try:
        opcion_de_la_mutacion = int(input("""
          Elegir que tipo de mutacion desea realir
          1)Mutacion horizontal(Radiacion)
          2)Mutacion verticañ(Radiacion)
          3)Mutacion ascendente(Virus)
          4)Mutacion descendente(Virus)
          Elija una opcion del 1 al 4: 
          """))
        if opcion_de_la_mutacion not in [1,2,3,4]:
            print("Opcion incorrecta, elegir entre el 1 y el 4")
            return
        
        fila= int(input("Ingrese la fila de inicio de la mutacion (0-5):"))
        columna=int(input("Ingrese la columna de inicio de la mutacion (0-5):"))

        #Para la mutacion radiacion(horizontal o vertical)
        if opcion_de_la_mutacion == 1 or opcion_de_la_mutacion == 2 :
            direccion="H" if opcion_de_la_mutacion == 1 else "V"
            simbolo= input("Ingrese el simbolo para la mutacion (X por defecto):")
            if not verificar_letra(simbolo): raise Exception("Solo se pueden ingresar: A, C, G o T")
            simbolo=simbolo if simbolo else "X"
            radiacion=Radiacion(["A","C","G","T"],modificar_matriz(matriz),direccion,simbolo)
            nueva_matriz=radiacion.crear_mutante(simbolo,(fila,columna),direccion)
            if nueva_matriz:
                mostrar_mensaje("Mutacion realizada, ADN mutado")
                imprimir_secuencia(nueva_matriz)
                return modificar_matriz_inversa(nueva_matriz)
            else:
                return []

        #Para la mutacion Virus(Diagonal ascendente o descendente)
        elif opcion_de_la_mutacion == 3 or opcion_de_la_mutacion == 4:
            direccion="ASC" if opcion_de_la_mutacion==3 else "DESC"
            simbolo=input("Ingrese el simbolo para la mutacion(Y por defecto):")
            if not verificar_letra(simbolo): raise Exception("Solo se pueden ingresar: A, C, G o T")
            simbolo=simbolo if simbolo else "Y"
            virus=Virus(["A","C","G","T"],modificar_matriz(matriz),direccion,simbolo)
            nueva_matriz=virus.crear_mutante(simbolo,(fila,columna))
            if nueva_matriz:
                mostrar_mensaje("Mutacion realizada, ADN mutado")
                imprimir_secuencia(nueva_matriz)
                return modificar_matriz_inversa(nueva_matriz)
            else:
                return []


    except ValueError:
        mostrar_mensaje("Opcion incorrecta, agurese de ingresar un numero")
    except Exception as e:
        mostrar_mensaje(f"Error al mutar: {e}")

def sanar_adn(matriz) -> None:
    mostrar_mensaje("verificando mutaciones...")
    sanador=Sanador(["A","C","G","T"])
    matriz_sanada=sanador.sanar_mutantes(matriz)
    
    

    if matriz_sanada:
        print("ADN sanado, hay nueva secuencia:")
        imprimir_secuencia(matriz_sanada)
        return(matriz_sanada)
    else:
        print("No se detectaron mutaciones, el ADN esta limpio")
        return matriz