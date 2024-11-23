from funciones import mostrar_mensaje, imprimir_secuencia, ingresar_matriz, detectar_mutaciones, mutar_adn, sanar_adn
import traceback

mostrar_mensaje("Programa ADN")
matriz = ingresar_matriz()
imprimir_secuencia(matriz)
opcion = -1      
while opcion != 0:
    print("------------------------------", end="")
    try:
        opcion = int(input("""
          Que desea hacer?
          1) Detectar mutaciones
          2) Mutar el ADN
          3) Sanar el ADN
          4) Mostrar ADN
          0) Salir
          Escoja una opcion: """))
        if type(opcion) != int:
            raise TypeError("Debe ingresar un numero")
        elif not opcion in [1,2,3,0,4]:
            raise TypeError("Debe ingresar un numero entre 0 y 3")
        else:
            if opcion == 0: break
            #codigo

            if opcion == 1:
                detectar_mutaciones(matriz)
            elif opcion == 2:
                nueva_matriz = mutar_adn(matriz)
                if nueva_matriz: matriz = nueva_matriz
            elif opcion == 3:
                matriz = sanar_adn(matriz)
            elif opcion == 4:
                imprimir_secuencia(matriz)
            else:
                raise TypeError("Debe ingresar un numero")
            
            #codigo
    except TypeError as e:
        mostrar_mensaje(e)
        #traceback.print_exc()
    except ValueError:
        mostrar_mensaje("Debe ingresar un numero")
    except Exception as e:
        print(e)
        #traceback.print_exc()
        
print("Saliendo del programa....")