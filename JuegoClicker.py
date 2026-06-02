
import tkinter as tk#impoortamos la libreria de tkinter
import random
class JuegoClicker:
    def __init__(self):
        #Lista de enemigos
        self.enemigos = random.choice(["Dragon ancestral","Rata gigante","Golem de piedra","Golem de lava", "Perro rabioso", "Lobo de las nieves","Espiritu del agua"])
        #Ventana principal
        self.ventana= tk.Tk()
        self.ventana.title("¡Heroes Clicker")
        self.ventana.geometry("400x400")
        #Marco de la vida
        self.recuadro_vida = tk.Frame(self.ventana, bg="#4d4a3f", bd= 4, relief="sunken")
        self.recuadro_vida.pack(pady=10)
        #Imagen vida monstruo
        self.vida_max = random.randint(100, 1000)
        self.vida_actual= self.vida_max
        self.vida = tk.Label(self.recuadro_vida, text=f"Vida = {self.vida_actual}/{self.vida_max}", font=("Arial", 20, "bold"),bg="#4d4a3f", fg="#5c9442")
        self.vida.pack(pady=15, padx=15)
        #Boton de ataque 
        self.boton_ataque = tk.Button(self.ventana, text="Atacar", font=("Arial",20),command= self.atacar)
        self.boton_ataque.pack(pady=10)
        #Narrador
        self.narrador= tk.Label(self.ventana, text=f"¡Un {self.enemigos} ha aparecido", font=("Arial",12))
        self.narrador.pack(pady=10, padx=20)
        #Contador botin
        self.dinero_actual=0
        self.oro = tk.Label(self.ventana, text= f"Tienes {self.dinero_actual} cantidad de oro")
        self.oro.pack(pady=5)
        #Boton de invocar nuevo mostruo
        self.invocar = tk.Button(self.ventana, text="INVOCAR", font=("Arial",20), command=self.invocar_monstruo)
        #Ejecutamos el loop para que s emuestre la ventana 
        self.ventana.mainloop()
    def atacar(self):
        daño_recibido = random.randint(5,50)
        self.vida_actual = self.vida_actual - daño_recibido  
        if self.vida_actual  <= 0:
            self.vida.config(text=f"Vida = 0/{self.vida_max}")
            self.narrador.config(text="Has derrotado al monstruo ¡FELICIDADES!")
            self.boton_ataque.config(state="disabled") 
            self.invocar.pack(pady=5)
        else: 
            self.vida.config(text=f"Vida: {self.vida_actual}/{self.vida_max}")  
            self.narrador.config(text=f"Has hecho {daño_recibido} de daño al monstruo")
            self.dinero_actual = self.dinero_actual + random.randint(1,5)
            self.oro.config(text= f"Tienes {self.dinero_actual} cantidad de oro")

    def invocar_monstruo(self):
        if self.vida_actual <= 0:
            self.invocar.config(state="normal")
            self.vida_max = random.randint(100, 1000)
            self.vida_actual= self.vida_max
            self.enemigos = random.choice(["Dragon ancestral","Rata gigante","Golem de piedra","Golem de lava", "Perro rabioso", "Lobo de las nieves","Espiritu del agua"])
            self.vida.config(text=f"Vida = {self.vida_actual}/{self.vida_max}")
            self.narrador.config(text=f"¡Un {self.enemigos} ha aparecido")
            self.boton_ataque.config(state="normal")
            self.invocar.pack_forget()
        else:
            self.invocar.config(state="disabled")
JuegoClicker()
