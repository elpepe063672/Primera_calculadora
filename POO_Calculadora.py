#Definimos los inputs que le vamos a pedir al usuario
#Lo hacemos fuera de la clase calculadora para poder usarlos en otra clase 
def pedir_numero():
    while True:
        numero = input("Numero: ")
        try:#Probamos esta linea, si no da error hace:
            return float(numero) #Detiene la funcion y nos da el valor actual 
        except: #Si salta algun error hace esta linea sin detener el codigo 
            print("Numero no valido, por favor ingrese otro numero")
def pedir_operacion():
    while True:
        operacion = input("Operacion: ")
        #Si no se usa un "in" antes de la lista te pedira todas y cada una de ellas para ser True 
        if operacion in ["+", "-","*","/","="]: 
            return operacion 
        else:
            print("Esta no es una operacion valida")
#Creamos la clase "Plano" de la calculadora 
class Calculadora:
    #Le damos los valores iniciales cuando inicie la calculadora 
    #Le damos a cada variable un self "llave" para que las operaciones cogan estos valores 
    def __init__(self):
        self.resultado = 0.0
        self.historial = []
    #Funcion separada para la memoria del historial
    def recibir_historial(self, numero_anterior, operacion, nuevo_num):
        linea = f"{numero_anterior} {operacion} {nuevo_num} = {self.resultado}"
        self.historial.append(linea)
    #Le decimos que use la "llave" para usar el resultado de la mochila 
    def suma(self, nuevo_num):
        numero_anterior = self.resultado
        self.resultado += nuevo_num
        self.recibir_historial(numero_anterior, "+", nuevo_num)#Guardamos la operacion en el historial
    def resta(self,nuevo_num):
        numero_anterior = self.resultado
        self.resultado -= nuevo_num
        self.recibir_historial(numero_anterior, "-", nuevo_num)
    def multiplicacion(self, nuevo_num):
        numero_anterior = self.resultado
        self.resultado *= nuevo_num
        self.recibir_historial(numero_anterior, "*", nuevo_num)
    def division(self, nuevo_num):
        if nuevo_num == 0:
            print("No se puede dividir por cero, ingreesa un numero valido")
        else:
            anterior_numero = self.resultado
            self.resultado /= nuevo_num
            self.recibir_historial(anterior_numero, "/", nuevo_num)
 
#Definimos nuestro primer objeto 
mi_calculadora = Calculadora()
#Iniciamos el programa de operaciones 
while True:
    primer_numero = pedir_numero()
    mi_calculadora.suma(primer_numero)#Sumamos el primer valor que le damos a el valor 0.0 de la calculadora 
    while True: 
        operacion = pedir_operacion()
        if operacion == "=":
            print("\n------HISTORIAL------")
            for linea in mi_calculadora.historial:
                print(linea)
            print("---------------------")
            print("Respuesta: ", mi_calculadora.resultado)
            break#Rompemos el bucle para terminar las operaciones 
        if operacion in ["+", "-","*","/"]:
            nuevo_num = pedir_numero()
            if operacion == "+":
                mi_calculadora.suma(nuevo_num)
            if operacion == "-":
                mi_calculadora.resta(nuevo_num)
            if operacion == "*":
                mi_calculadora.multiplicacion(nuevo_num)
            if operacion == "/":
                mi_calculadora.division(nuevo_num)
            print("Respuesta: ", mi_calculadora.resultado)
    if operacion == "=":
        break#Rompemos el ultimo bucle para terminar el programa
    