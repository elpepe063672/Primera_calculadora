
import tkinter as tk#impoortamos la libreria de tkinter
import random
class JuegoClicker:
    def __init__(self):
        #Daño
        self.daño_max= 50
        self.daño_min = 5
        #Lista de enemigos
        self.lista_enemigos =["Dragon ancestral",
                                        "Rata gigante",
                                        "Golem de piedra",
                                        "Golem de lava",
                                        "Perro rabioso",
                                        "Lobo de las nieves",
                                        "Espiritu del agua"]
        self.enemigos= random.choice(self.lista_enemigos)
        #Ventana principal
        self.ventana= tk.Tk()
        self.ventana.title("¡Heroes Clicker")
        self.ventana.geometry("400x400")
        self.ventana.config(bg="#61656b")
        #Frame general
        self.recuadro_juego = tk.Frame(self.ventana, 
                                       bg="#68a4cc", 
                                       bd= 10, 
                                       relief="sunken")
        self.recuadro_juego.place(relx=0.5, 
                                  rely=0.5,
                                  relwidth=0.95, 
                                  relheight=0.95, 
                                  anchor="center")
        #Nombre monstruo
        self.nombre_m = tk.Label(self.recuadro_juego,
                                 text=(f"{self.enemigos}"),
                                 font=("Arial",12),)
        self.nombre_m.pack(pady=5)
        #Marco de la vida
        self.recuadro_vida = tk.Frame(self.recuadro_juego, 
                                      bg="#4d4a3f", 
                                      bd= 10, 
                                      relief="sunken")
        self.recuadro_vida.place(relx=0.5,
                                 rely=0.37,
                                 relheight=0.5,
                                 relwidth=0.7,
                                 anchor="center")
        #Barra de vida 
        self.barra_vida = tk.Frame(self.recuadro_juego,
                                   relief="groove",
                                   bg="#1a8017",
                                   bd=4)
        self.barra_vida.place(relx= 0.5,
                              rely= 0.7,
                              relwidth=0.85,
                              relheight=0.1,
                              anchor="center"
                              )
        #Imagen vida monstruo
        self.vida_max = random.randint(100, 1000)
        self.vida_actual= self.vida_max
        self.vida = tk.Label(self.barra_vida, 
                             text=f"Vida : {self.vida_actual}/{self.vida_max}", 
                             font=("Arial", 20, "bold"),
                             bg="#1a8017", 
                             fg="#FF0000")
        self.vida.pack(pady=1, padx=1)
        #Boton de ataque 
        self.boton_ataque = tk.Button(self.recuadro_juego, 
                                      text="ATACAR", 
                                      font=("Arial",15), 
                                      relief= "groove",
                                      activebackground= "#631f16",
                                      activeforeground="white",
                                      command= self.atacar)
        self.boton_ataque.place(relx=0.35, 
                                rely=0.87, 
                                relheight=0.1, 
                                relwidth=0.3, 
                                anchor="ne")
        #Narrador
        self.narrador= tk.Label(self.recuadro_juego, 
                                text=f"¡Un {self.enemigos} ha aparecido", 
                                font=("Arial",12))
        self.narrador.place(relx=0.5,
                            rely=0.8,
                            anchor="center")
        #Contador botin
        self.dinero_actual=0
        self.oro = tk.Label(self.recuadro_juego, 
                            text=f"MONEDERO: {self.dinero_actual}")
        self.oro.place(relx=0.51, 
                       rely=0.9,
                       anchor="center")
        #Boton de invocar nuevo mostruo
        self.invocar = tk.Button(self.recuadro_juego, 
                                 text="INVOCAR", 
                                 font=("Arial",15), 
                                 command=self.invocar_monstruo)
        #Boton para ir a la tienda 
        self.tienda = tk.Button(self.recuadro_juego, 
                                text="TIENDA", 
                                font=("Arial",15),
                                relief= "groove",
                                activebackground= "#631f16",
                                activeforeground="white", 
                                command=self.abrir_tienda)
        self.tienda.place(relx=0.67, 
                          rely=0.87, 
                          relheight=0.1, 
                          relwidth=0.3, 
                          anchor="nw")
        #Marco de la tienda 
        self.recuadro_tienda = tk.Frame(self.ventana, 
                                        bg="#382d23", 
                                        bd= 10, 
                                        relief="sunken")
        #Narrador tienda 
        self.narrador_tienda = tk.Label(self.recuadro_tienda, 
                                        text=("BIENVENIDO A LA TIENDA"), 
                                        font=("Times new roman",12),
                                        bg="#382d23", 
                                        fg="#FFFFFF")
        #Boton de regreso al mapa
        self.boton_regreso= tk.Button(self.recuadro_tienda, 
                                      text="REGRESAR", 
                                      font=("Arial",20), 
                                      command=self.regresar)
        #Ejecutamos el loop para que se emuestre la ventana 

        self.ventana.mainloop()
    def atacar(self):
        daño_recibido = random.randint(self.daño_min,self.daño_max)
        self.vida_actual = self.vida_actual - daño_recibido  
        if self.vida_actual  <= 0:
            self.vida.config(text=f"Vida : 0/{self.vida_max}")
            self.narrador.config(text="Has derrotado al monstruo ¡FELICIDADES!")
            self.boton_ataque.place_forget()
            self.invocar.place(relx=0.35, 
                                rely=0.87, 
                                relheight=0.1, 
                                relwidth=0.3, 
                                anchor="ne")
        else: 
            self.vida.config(text=f"Vida: {self.vida_actual}/{self.vida_max}")  
            self.narrador.config(text=f"Has hecho {daño_recibido} de daño al monstruo")
            self.dinero_actual = self.dinero_actual + random.randint(0,5)
            self.oro.config(text=f"MONEDERO {self.dinero_actual}")

    def invocar_monstruo(self):
        if self.vida_actual <= 0:
            self.invocar.config(state="normal")
            self.vida_max = random.randint(100, 1000)
            self.vida_actual= self.vida_max
            self.vida.config(text=f"Vida : {self.vida_actual}/{self.vida_max}")
            self.enemigos= random.choice(self.lista_enemigos)
            self.narrador.config(text=f"¡Un {self.enemigos} ha aparecido")
            self.nombre_m.config(text=f"Monstruo {self.enemigos}")
            self.invocar.place_forget()
            self.boton_ataque.place(relx=0.35, 
                                rely=0.87, 
                                relheight=0.1, 
                                relwidth=0.3, 
                                anchor="ne")
    def abrir_tienda(self):
        self.recuadro_juego.place_forget()
        self.recuadro_tienda.place(relx=0.5, 
                                   rely=0.5,
                                   relwidth=0.95, 
                                   relheight=0.95, 
                                   anchor="center")
        self.narrador_tienda.pack(pady=2)
        self.boton_regreso.place(relx=0.25, rely=0.8)
    def regresar(self):
        self.recuadro_tienda.place_forget()
        self.recuadro_juego.place(relx=0.5, 
                                  rely=0.5,
                                  relwidth=0.95, 
                                  relheight=0.95, 
                                  anchor="center")
        pass
    
        
JuegoClicker()
