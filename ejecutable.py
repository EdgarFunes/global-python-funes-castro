from clases import Detector, Mutador, Radiacion, Virus

# Imprime el arreglo que se envie por parametro
def imprimir_secuencia(array):
    print("Secuencia ingresada:")
    for x in array:
        print("  ".join(x))

# Secuencia a utilizar
matriz = [
    "TTTTCG",
    "TCTTGA",
    "CACGAT",
    "TAGCTA",
    "GACGGA",
    "TACAAA"
]
imprimir_secuencia(matriz)

detector = Detector()

detector.verificar_base_nitrogenada(matriz)
if detector.detectar_mutantes(matriz):
    print("Mutante detectado")
else:
    print("No se detectaron mutaciones")
    
    print("Mutante detectado" if detector.detectar_mutantes(matriz) else "No se detectaron mutantes")

print("")

# Aqui podemos ver las bases nitrogenadas repetidas
simbolos = detector.get_simbolos_mutante()
print(simbolos)
print("")

# De esta forma se pueden obtener las posiciones de las mutaciones
# matriz[posicion[0]][posicion[1]] mostraria el valor de la celda
# posicion[0] o posicion[1] mostrarian el valor de filas y columnas de cada mutacion
print("Todas las mutaciones encontradas y almacenadas")
posiciones = detector.get_posiciones_repetidas()
for repeticion in posiciones:
    print(repeticion)
    for posicion in repeticion:
        print(matriz[posicion[0]][posicion[1]], end=", ")
    print("\n")


mutador = Mutador("T", matriz)

radiacion= Radiacion(["A","C","G","T"],matriz)
posicion_inicial=(1,1)
radiacion.crear_mutante(["A","C","G","T"], posicion_inicial, "H")

