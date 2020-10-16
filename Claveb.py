import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la suma de 3 numeros
2+4+6 = 12
"""


# start-->
def suma(numero1, numero2, numero3):
    result = numero1 + numero2 + numero3
    return result


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros impares del 1 al 1000
"""


# start-->
def sumaImpares():
    suma = 0
    inicial = 1
    while inicial < 1000:
        suma = suma + inicial
        result = suma
        inicial += 2
    result = suma
    return result


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el perimetro, area y el volumen de un esfera
radio = 12 m
perimetro: 2*pi*r
area: 4*pi*r^2
volumen: (4/3)*pi*r^3
"""


# start-->
def definicionEsfera(radio):
    result = radio
    return result


def obtenerPerimetro():
    result = 2 * math.pi * (definicionEsfera())
    return result


def obtenerArea():
    result = 4 * math.pi * (definicionEsfera() ** 2)
    return result


def obtenerVolumen():
    result = (4 / 3) * math.pi * (definicionEsfera() ** 3)
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Esfera:
    def __init__(self, radio):
        self.radio = radio

    def definicionEsfera(self):
        result = self.radio
        return result

    def obtenerPerimetro(self):
        result = 2 * math.pi * (self.radio)
        return result

    def obtenerArea(self):
        result = 4 * math.pi * (self.radio ** 2)
        return result

    def obtenerVolumen(self):
        result = (4 / 3) * math.pi * (self.radio ** 3)
        return result


"""
***************************************************************
@@ ejercicio 5 @@
Banco
Cliente
    nombre
    lugar
    numero de cuenta
    transaccion - retiro o abono
    monto
"""





class Banco:
    def procesar(Cliente):
        print("Desea abonar o retirar")
        resp=input()
        if resp == "abonar"
        

    def abonosSanSalvador(self):
        if "San Salvador" in clientes:
            
        return 0

    def abonosBalYRod(self):

       if "balbino" and "rodrigo" in clientes:

        return 0


class Cliente:
    def __init__(self, nombre, departamento, numero):
        self.nombre = nombre
        self.departamento = departamento
        self.numero = numero
    def ObtenerNombre(self):
        return self.nombre
    def ObtenerDepartamento(self):
        return self.departamento
    def ObtenerNombre(self):
        return self.numero
    def Obtenercliente(self):
       return self.nombre + self.departamento + self.numero


    


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return ""
