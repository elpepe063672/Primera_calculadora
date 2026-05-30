import tkinter as tk #Entramos en la libreria para coger nuestra ventana    
class InterfazVentana: 
    def __init__(self, ventana):
        #Definimos la ventana y el titulo
        self.ventana = ventana
        self.ventana.title("CALCULADORA")
        #--------PANTALLA--------
        self.pantalla = tk.Entry(ventana, font=("Arial", 20), justify ="center")
        self.pantalla.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky="ew")#Usamos la caractetisica sticky para que se estire hacia donde queramos 
        #Le damos un tamaño fijo a la ventana 
        self.ventana.geometry("410x280")
        #Haecmos que cada columna de la ventana tenga "peso" para repartir el espacio equitativamente 
        self.ventana.grid_columnconfigure(0, weight=1)
        self.ventana.grid_columnconfigure(1, weight=1)
        self.ventana.grid_columnconfigure(2, weight=1)
        self.ventana.grid_columnconfigure(3, weight=1)
        #Definimos los botones que se van a mostrar y los conectamos al programa
        #Botones del 0-9
        #--------FILA 1--------
        self.boton_1 = tk.Button(ventana, text= "1", font=("Arial",18), width=5, command=lambda: self.pulsar_boton("1")) 
        self.boton_1.grid(row=3, column=0, padx=1, pady=1)
        self.boton_2 = tk.Button(ventana, text= "2", font=("Arial",18), width=5, command=lambda: self.pulsar_boton("2"))
        self.boton_2.grid(row=3, column=1, padx=1, pady=1)
        self.boton_3 = tk.Button(ventana, text= "3", font=("Arial",18), width=5, command=lambda: self.pulsar_boton("3")) 
        self.boton_3.grid(row=3, column=2, padx=1, pady=1)  
        #--------FILA 2--------
        self.boton_4 = tk.Button(ventana, text= "4", font=("Arial",18), width=5, command=lambda: self.pulsar_boton("4")) 
        self.boton_4.grid(row=2, column=0, padx=1, pady=1)
        self.boton_5 = tk.Button(ventana, text= "5", font=("Arial",18), width=5, command=lambda: self.pulsar_boton("5")) 
        self.boton_5.grid(row=2, column=1, padx=1, pady=1)
        self.boton_6 = tk.Button(ventana, text= "6", font=("Arial",18), width=5, command=lambda: self.pulsar_boton("6")) 
        self.boton_6.grid(row=2, column=2, padx=1, pady=1)  
        #--------FILA 3--------
        self.boton_7 = tk.Button(ventana, text="7", font=("Arial",18), width=5, command=lambda: self.pulsar_boton("7"))
        self.boton_7.grid(row=1, column=0, padx=1, pady=1)
        self.boton_8 = tk.Button(ventana, text="8", font=("Arial",18), width=5, command=lambda: self.pulsar_boton("8"))
        self.boton_8.grid(row=1, column=1, padx=1, pady=1)
        self.boton_9 = tk.Button(ventana, text= "9", font=("Arial",18), width=5, command=lambda: self.pulsar_boton("9")) 
        self.boton_9.grid(row=1, column=2, padx=1, pady=1)
        #--------FILA 4--------
        self.boton_0 = tk.Button(ventana, text= "0", font=("Arial",18), width=5, command=lambda: self.pulsar_boton("0")) 
        self.boton_0.grid(row=4, column=1, padx=1, pady=1)
        self.boton_igual = tk.Button(ventana, text= "=", font=("Arial",18), width=5, command=self.calcular)
        self.boton_igual.grid(row=4, column=2, padx=1, pady=1)
        self.boton_c = tk.Button(ventana, text="C", font=("Arial",18), width=5, command=self.limpiar)
        self.boton_c.grid(row=4, column=0, padx=1, pady=1)
        #--------OPERACIONES--------
        self.boton_menos = tk.Button(ventana, text="-", font=("Arial",18), width=5, command=lambda: self.pulsar_boton("-"))
        self.boton_menos.grid(row=4, column=3, padx=1, pady=1)
        self.boton_mas = tk.Button(ventana, text="+", font=("Arial",18), width=5, command=lambda: self.pulsar_boton("+"))
        self.boton_mas.grid(row=3, column=3, padx=1, pady=1)
        self.boton_por = tk.Button(ventana, text="*", font=("Arial",18), width=5, command=lambda: self.pulsar_boton("*"))
        self.boton_por.grid(row=1, column=3, padx=1, pady=1)
        self.boton_entre = tk.Button(ventana, text="/", font=("Arial",18), width=5, command=lambda: self.pulsar_boton("/"))
        self.boton_entre.grid(row=2, column=3, padx=1, pady=1)
    def pulsar_boton(self,valor):
        self.pantalla.insert(tk.END, valor)
    def limpiar(self):
        self.pantalla.delete(0,tk.END)
    def calcular(self):
        try:
            ecuacion = self.pantalla.get()
            resultado= eval(ecuacion)
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(tk.END, resultado)#El .insert() tiene que recibir dos valores, donde y que en ese orden 
        except ZeroDivisionError:
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(tk.END, "Error:No se puede dividir por 0")
        except:
            self.pantalla.delete(0,tk.END)
            self.pantalla.insert(tk.END, "Error:Operacion inexistente ")
#Llamamos a la ventana de la interfaz y la metemos en un bucle 
raiz = tk.Tk()
app = InterfazVentana(raiz)
raiz.mainloop()
"""
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
"""