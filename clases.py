class Detector:
    #! hay que utilizar estos atributos, segun sea necesario
    atributo_1 = "" 
    atributo_2 = ""
    
    # Metodo contrstructor
    def __init__(self):
        pass
    
    # Detecta si hay un mutante horizontal, vertical o diagonal. Retorna True o False
    def detectar_mutantes(matriz) -> bool:
        pass
    
class Mutador:
    base_nitrogenada = ""
    #! hay que utilizar estos atributos, segun sea necesario
    atributo_1 = ""
    atributo_2 = ""
    
    # Metodo constructor
    def __init__(self) -> None:
        pass
    
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