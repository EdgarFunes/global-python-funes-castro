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
    # Metodo constructor
    def __init__(self, base_nitrogenada, matriz) -> None:
        self.__base_nitrogenada = base_nitrogenada
        self.__matriz = matriz
        detector = Detector()
        self.__tiene_mutaciones = detector.detectar_mutantes(matriz)
    
    def crear_mutante() -> None:
        pass
    
class Radiacion(Mutador):
    base_nitrogenada = ""
    #! hay que utilizar estos atributos, segun sea necesario
    atributo_1 = ""
    atributo_2 = ""
    
    def __init__(self) -> None:
        super().__init__()
        pass
    
    def crear_mutante(base_nitrogenada, posicion_inicial, orientacion_de_la_mutacion):
        pass
    
class Virus(Mutador):
    base_nitrogenada = ""
    #! hay que utilizar estos atributos, segun sea necesario
    atributo_1 = ""
    atributo_2 = ""
    
    def __init__(self) -> None:
        super().__init__()
        
    def crear_mutante(base_nitrogenada, posicion_inicial) -> None:
        pass
    
class Sanador:
    #! hay que utilizar estos atributos, segun sea necesario
    atributo_1 = ""
    atributo_2 = ""
    
    def __init__(self) -> None:
        pass
    
    def sanar_mutantes(matriz):
        pass