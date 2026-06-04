import random
class Aparcamiento:
    def __init__(self):
        self.aforo = 2
        self.lista_coches =[]

    def ingresar_coche(self,matricula):
        if len(self.lista_coches) < self.aforo:
            self.lista_coches.append(matricula)
            print(f"Su coche con matricula {matricula} a sido estacionado con exito")
        else:
            print(f"Aforo limitado.Su coche con matricula {matricula} no a podido estacionarse ")
    
    def  sacar_coche(self,matricula):
        if matricula in self.lista_coches:
            self.lista_coches.remove(matricula)
            print(f"Su coche con matricula {matricula} a sido sacado con exito")
    def mirar_aforo(self):
        print(f"Coches dentro:{len(self.lista_coches)} de {self.aforo}")

class SalaCine:
    def __init__(self):
        self.asiento_reservados = []
    
    def reservar_asiento(self,fila,columna):
        if (fila,columna) not in self.asiento_reservados:
            asiento = (fila,columna)
            self.asiento_reservados.append(asiento)
            print("Tu asiento a sido reservado exitosamente")
        else:
            print(f"Lo siento el asiento fila:{fila}, columna:{columna} ya a sido reservado")
    def mapa_asientos(self):
        for fila in range (3):
            for columna in range (3):
                if (fila,columna) not in self.asiento_reservados:
                    print("[0]" , end= "")
                else:
                    print("[x]", end="")
            print()

def procesar_lista(lista_datos):
    for calculo in (lista_datos):
        try:
            respuesta = 100 / int(calculo)
            print("la respuesta es:", respuesta)
        except ZeroDivisionError:
            print("No se puede dividir por 0")
        except ValueError:
            print("No se pueden dividir palabras")

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def ladrar(self):
        print("¡Guau!, mi nombre es", self.nombre, "y tengo", self.edad, "años")
mi_perro = Perro("Doby", "4")
perro_vecino = Perro("Spike", "3")

class CuentaBancaria:
    def __init__(self,):
        self.saldo =  0
    def ingresas(self,cantidad):
        self.saldo = self.saldo + cantidad
    def mostrar_saldo(self):
        print( "Tienes", self.saldo, "euros en tu cuenta")
    
class Personaje:
    def __init__(self,nombre):
        self.nombre = nombre
        self.vida = 100
    def recibir_daño(self,daño):
        self.vida = self.vida - daño
    def comprobar_vida(self):
        if self.vida > 0:
            print(f"{self.nombre} sigue en combate con {self.vida} puntos de vida ")
        else:
            self.vida=0
            print(f"{self.nombre} a caido en combate con {self.vida} puntos de vida")
#--------EJERCICIO CLASS--------
#---------BOMBILLA---------
class Bombilla:
    def __init__(self):
        self.encendida = False
    def encender(self):
        self.encendida = True
    def apagar(self):
        self.encendida = False
    def comprobar_estado(self):
        if self.encendida:
            print("La habitacion esta iluminada")
        else:
            print("La habitacion esta a oscuras")
#--------EJERCICIO LAMBDA--------
#--------TECLADO--------
def crear_teclado():
    teclado = []#Creamos una lista vacia para guardar nuestras funciones temporales 
    for numero in range(1,5):#Creamos un bucle para asignar cada boton 
        #Guardamos el numero del bucle en la variable n como copia de seguridad y le decimos que lo imprima, esta es nuestra funcion 
        teclado.append(lambda n=numero: print(f"Has pulsado el numero {n}"))#Cada vez que se ejecuta el bucle se añade la funcion temporal a la lista 
        #como si guardaramos una variable cualquiera
    return teclado#Extraemos el valor de esa lista, en este caso cuatro funciones distintas      
    
mis_botones = crear_teclado()#Ejecutamos la funcion que hemos definido
#Ahora mismo la lista se veria asi: mis_botones = [ Accion_1, Accion_2, Accion_3, Accion_4 ]
"""for boton in mis_botones:#Creamos otro bucle para ejecutar la lista 
    boton()#Llamamos a cada posicion de la lista y la imprimimos """

#--------EJERCICIO LAMBDA--------
#--------HECHIZOS DE MAGO--------
def libro_de_hechizos():
    libro = []
    for nivel in range(1,5):
        libro.append(lambda n=nivel: print(f"El nivel del hechizo es {n}"))
    return libro

mi_libro = libro_de_hechizos()
"""for hechizo in mi_libro:
    hechizo()"""

#--------EJERCICIO LAMBDA--------
#--------PROTOCOLOS DE SEGURIDAD--------
def protocolos_segurudad():
    protocolo= []
    for fase in range (1,4):
        protocolo.append(lambda p=fase: print(f"La fase numero {p} del protocolo de seguridad se esta ejecutando"))
    return protocolo
mi_protocolo = protocolos_segurudad()
"""for numero in mi_protocolo:
    numero()"""
nombre = random.choice (["hola", "tres", "marico"])

print(nombre)
