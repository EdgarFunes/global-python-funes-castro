import traceback, random
class Detector:   
    # Metodo constructor
    def __init__(self, base_nitrogenada = ["A", "C", "G", "T"]):
        self.__base_nitrogenada = base_nitrogenada # Base nitrogenada a usar
        self.__simbolos_mutante = [] # Arreglo con los simbolos mutantes encontrados
        self.__posiciones_repetidos = [] # Arreglo con las posiciones repetidas, no se puede modificar desde afuera de la clase
    
    # Comprueba que la matriz corresponda a la base nitrogenada
    def verificar_base_nitrogenada(self, matriz):
        try:
            for fila in matriz:
                for letra in fila:
                    if letra not in self.__base_nitrogenada:
                        raise Exception("Se encuentra un elemento no permitido en la matriz")
        except Exception as e:
            print(e)
            
    
    # Detecta si hay un mutante
    def detectar_mutantes(self, matriz) -> bool:
        #! Guardamos en variables para evitar lazy evaluation
        horizontal = self.__detectar_horizontal(matriz)
        vertical = self.__detectar_vertical(matriz)
        diagonal = self.__detectar_diagonal(matriz)
        return horizontal or vertical or diagonal
    
    # Busca en todas las filas si hay repeticiones
    def __detectar_horizontal(self, matriz) -> bool:
        controlador = False
        for i in range(0, len(matriz)):
            if self.__detectar_repeticion(matriz[i], i, -1): controlador = True
        return controlador
    
    # Busca en todas las columnas si hay repeticiones
    def __detectar_vertical(self, matriz) -> bool:
        controlador = False
        for columna in range(len(matriz[0])):  # Itera por cada columna
            secuencia = [fila[columna] for fila in matriz]  # Construye la columna
            if self.__detectar_repeticion(secuencia, -1, columna): controlador = True
        return controlador
    
    # Busca en todas las diagonales si hay repeticiones
    def __detectar_diagonal(self, matriz) -> bool:
        return self.__recorrer_diagonales(matriz)
    
    # Detecta si se repite una base nitrogenada en la secuencia recibida y almacena las repeticiones en memoria
    def __detectar_repeticion(self, secuencia, fila, columna, direccion = "NONE") -> bool:
        controlador = False
        contador = 1 
        repeticiones_minimas = 4
        posiciones = []
        
        for i in range(0, len(secuencia)-1):
            if secuencia[i] == secuencia[i+1]:
                contador += 1
                # Para Horizontal y Vertical
                if direccion == "NONE":
                    posiciones.append([i, columna] if fila < 0 else [fila, i])
                # Para diagonales
                else:
                    posiciones.append([fila-i, columna+i] if direccion == "ASC" else [fila+i, columna+i])
            else:
                contador = 1
                posiciones.clear()
            if contador >= repeticiones_minimas:
                controlador = True
                # Para Horizontal y Vertical
                if direccion == "NONE":
                    posiciones.append([i+1, columna] if fila < 0 else [fila, i+1])
                # Para diagonales
                else:
                    posiciones.append([fila-i-1, columna+i+1] if direccion == "ASC" else [fila+i+1, columna+i+1])
                self.__posiciones_repetidos.append(posiciones.copy())
                self.__simbolos_mutante.append(secuencia[i])
                break 
        return controlador
    
    # Recorre todas las diagonales con 4 o mas elementos
    def __recorrer_diagonales(self, matriz) -> bool:
        controlador = False
        n = len(matriz)

    # Recorre desde esquina inferior izquierda
        for i in range(2, -1, -1):
            diagonal = ""
            for j in range(0, n-i):
                diagonal += (matriz[5-j][i+j])
            if self.__detectar_repeticion(diagonal, 5, i, "ASC"): controlador = True
            
        for i in range(4, 2, -1): 
            diagonal = ""
            for j in range(0, n-(n-i)+1):    
                diagonal += (matriz[i-j][j])
            if self.__detectar_repeticion(diagonal, i, 0, "ASC"): controlador = True
            
        # Recorre desde la esquina superior izquierda
        for i in range(0, 3):
            diagonal = ""
            for j in range(0, n-i):
                diagonal += (matriz[i+j][j])
            if self.__detectar_repeticion(diagonal, i, 0, "DESC"): controlador = True
            
        for i in range(1, 3):
            diagonal = ""
            for j in range(0, n-i):
                diagonal += (matriz[j][i+j])
            if self.__detectar_repeticion(diagonal, 0, i, "DESC"): controlador = True
                
        return controlador
    
    # Getters
    def get_posiciones_repetidas(self):
        return self.__posiciones_repetidos
    
    def get_simbolos_mutante(self):
        return self.__simbolos_mutante
            
    
class Mutador: 
    # Método constructor
    def __init__(self, base_nitrogenada, matriz) -> None:
        self._base_nitrogenada = base_nitrogenada  # Atributo protegido
        self._matriz = matriz  # Cambiado a protegido
        detector = Detector()
        self._tiene_mutaciones = detector.detectar_mutantes(matriz)
    
    def crear_mutante() -> None:
        pass

class Radiacion(Mutador):
    def __init__(self, base_nitrogenada, matriz, direccion="H", simbolo_mutante=None):
        super().__init__(base_nitrogenada, matriz)
        self.direccion = direccion # de la mutacion
        self.simbolo_mutante = simbolo_mutante if simbolo_mutante else base_nitrogenada[0]
    
    def crear_mutante(self, base_nitrogenada, posicion_inicial, orientacion_de_la_mutacion):

        try:
            #validamos la orientacion
            if orientacion_de_la_mutacion not in ["H","V"]:
                raise ValueError("La orientacion de la mutacion debe ser 'H' o 'V'")
                                
            fila, columna = posicion_inicial
            #validamos posicion inicial
            if fila < 0 or columna < 0 or fila >= len(self._matriz) or columna >= len(self._matriz[0]):
                raise IndexError("La posisicion inicial esta fuera de los limitesde la matriz")

                #Creamos el mutante horizontal o vertical segun la orientacin
            if orientacion_de_la_mutacion == "H":
                if columna + 3 < len(self._matriz[0]):
                    for i in range(4):
                        self._matriz[fila][columna + i] = base_nitrogenada
                else:
                    raise IndexError("No hay suficiente espacio para la matriz horizontal")
            elif orientacion_de_la_mutacion == "V":
                if fila + 3 < len(self._matriz):
                    for i in range(4):
                        self._matriz[fila + i][columna]= base_nitrogenada
                else:
                    raise IndexError("No hay suficiente espaciop para la mutacion vertical")     

            return self._matriz #Devolvemos la matriz modificada  

        except Exception as e:
            print(f"Error al crear el mutante: {e}")
            traceback.print_exc()
            return None

class Virus(Mutador):

    def __init__(self, base_nitrogenada, matriz, direccion="ASC", simbolo_mutante=None):
        super().__init__(base_nitrogenada,matriz)
        self.direccion=direccion # Direccion de la mutacion, "ASC" o "DESC"
        self.simbolo_mutante= simbolo_mutante if simbolo_mutante else base_nitrogenada[0] # Base por defecto
        
    def crear_mutante(self,base_nitrogenada, posicion_inicial):
        try:
            fila, columna = posicion_inicial

            #Validos posiscion inicial
            if fila < 0 or columna < 0 or fila >= len(self._matriz) or columna >= len(self._matriz[0]):
                raise IndexError("La posicion inicial esta fuera de los limites de la matriz")

            #Creamos el mutante diagonal ascendente o descendente segun la orientacion  
            if self.direccion == "ASC":
                if fila - 3 >= 0 and columna + 3 < len(self._matriz[0]):
                    for i in range(4):
                        self._matriz[fila - i][columna + i]= base_nitrogenada
                else:
                    raise IndexError("No hay suficiente espacio para la mutacion diagonal ascendente")
            elif self.direccion == "DESC":       
                if fila + 3 < len(self._matriz) and columna + 3 < len(self._matriz[0]):
                    for i in range(4):
                        self._matriz[fila + i][columna + i]= base_nitrogenada
                else:
                    raise IndexError("No hay suficiente espacio para la mutacion diagonal descendente")
            
            return self._matriz #Devolvemos la matriz modificada
        
        except Exception as e:
            print(f"Error al crear mutante: {e}")
            return None
class Sanador:
    
    def __init__(self, base_nitrogenada=["A","C","G","T"]):
        self.base_nitrogenada=base_nitrogenada
        self.detector=Detector(base_nitrogenada)
    
    def sanar_mutantes(self,matriz):
        
        try:
            #Comprobamos si hay mutaciones en la matriz
            if self.detector.detectar_mutantes(matriz):
                print("Mutacion detectada, se generara uno sin mutaciones")

                #Generamos uno nuevo sin mutaciones
                nuevo_adn=self.__generar_adn_sin_mutaciones(len(matriz), len(matriz[0]))
                return nuevo_adn #DEvolvemos el nuevo adn sin mutaciones

            else:
                print("No se detectaron mutaciones en el adn")
                return matriz #Si no hay mutaciones retornamos la matriz original
        
        except Exception as e:
            print(f"Error al sanr mutantes: {e}")
            return None
    
    def __generar_adn_sin_mutaciones(self,filas,columnas):
        #Generamos un nuevo adn aleatori con las bases nitrogenadas validas
        return [[random.choice(self.base_nitrogenada) for _ in range(columnas)] for _ in range(filas)]