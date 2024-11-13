# Imprime el arreglo que se envie por parametro
def imprimir_secuencia(array):
    print("Secuencia ingresada:")
    for x in array:
        print("  ".join(x))

# Secuencia a utilizar
matriz = ["AGATCA", "GATTCA", "CAACAT", "GAGCTA", "ATTGCG", "CTGTTC"]
imprimir_secuencia(matriz)


