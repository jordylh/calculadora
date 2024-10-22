import customtkinter
from calculadora import Calculadora
import sys
import os
class MyFrame(customtkinter.CTkFrame):

    def sumar(self):
        num1=self.a.get()
        num2=self.b.get()
        cal=Calculadora()
        string="Resultado: "+str(cal.sumar(float(num1),float(num2)))
        self.label.configure(text=string)

    def restar(self):
        num1=self.a.get()
        num2=self.b.get()
        cal=Calculadora()
        string="Resultado: "+str(cal.restar(float(num1),float(num2)))
        self.label.configure(text=string)


    def limpiar(self):
        self.a.delete(0,'end')
        self.b.delete(0,'end')
        self.label.configure(text="Resultado:")


    def multiplicar(self):
        num1=self.a.get()
        num2=self.b.get()
        cal=Calculadora()
        string="Resultado: "+str(cal.multiplicar(float(num1),float(num2)))
        self.label.configure(text=string)


    def dividir(self):
        num1=self.a.get()
        num2=self.b.get()
        cal=Calculadora()
        string="Resultado: "+str(cal.dividir(float(num1),float(num2)))
        self.label.configure(text=string)

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.a = customtkinter.CTkEntry(self, placeholder_text="Ingrese un numero")
        self.a.grid(row=0,column=0,padx=20)

        self.b = customtkinter.CTkEntry(self, placeholder_text="Ingrese un numero")
        self.b.grid(row=0,column=1,padx=20)

        self.label = customtkinter.CTkLabel(self,text="Resultado:")
        self.label.grid(row=0, column=2, padx=20,pady=10)

        self.button1 = customtkinter.CTkButton(self, text="Sumar", command=self.sumar)
        self.button1.grid(row=1,column=0,padx=20,)

        self.button2 = customtkinter.CTkButton(self, text="Restar", command=self.restar)
        self.button2.grid(row=1,column=1,padx=20)

        self.button3 = customtkinter.CTkButton(self, text="Limpiar", command=self.limpiar)
        self.button3.grid(row=1,column=2,padx=20,)

        self.button4 = customtkinter.CTkButton(self, text="Multiplicar", command=self.multiplicar)
        self.button4.grid(row=3,column=0,padx=20,pady=10)

        self.button5 = customtkinter.CTkButton(self, text="Dividir", command=self.dividir)
        self.button5.grid(row=3,column=1,padx=20)


class App(customtkinter.CTk):

    def resource_path(self,relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    
    def __init__(self):
        super().__init__()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        window_height = 200
        window_width = 600

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.title("Calculadora")
        self._set_appearance_mode("dark")
        self.resizable(False,False)
        self.wm_iconbitmap(self.resource_path("res/calculadora.ico"))

app = App()
app.mainloop()