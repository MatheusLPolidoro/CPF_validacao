from tkinter import *
from AnaliseCPF import NumeroCPF
import os

pasta_app = os.path.dirname(__file__) + "\\images\\"

def format_cpf(event = None):
    
    text = numero_cpf.get().replace(".", "").replace("-", "")[:11]
    new_text = ""

    if event.keysym.lower() == "backspace": return
    
    for index in range(len(text)):
        
        if not text[index] in "0123456789": continue
        if index in [2, 5]: new_text += text[index] + "."
        elif index == 8: new_text += text[index] + "-"
        else: new_text += text[index]

    numero_cpf.delete(0, "end")
    numero_cpf.insert(0, new_text)

def main():
    cpf = NumeroCPF(numero_cpf.get())
    cpf.gerar_digitos_verificadores() 
    img['file'] = pasta_app + "valido.png" if cpf.confirmar_digitos_verificadores() == True else pasta_app + "invalido.png"
    cpf.mostrar_resultado()

janela = Tk()
janela.title("Validar CPF")
janela.geometry("400x150")
janela.configure(background="#dde")
Label(janela, text="Informe o número do CPF que deseja confirmar:",background="#dde", foreground="#005", anchor=W, font="family=Arial").place(x = 10, y = 10, width = 350, height = 20)
numero_cpf = Entry(janela, font="family=Arial")
numero_cpf.bind("<KeyRelease>", format_cpf)
numero_cpf.place(x = 15, y = 40, width=150, height=30)
img = PhotoImage(file = pasta_app + "image.png")
Label(janela, image = img, background="#dde").place(x = 250, y = 35)
Button(janela, text = "Enviar", command = main).place(x = 15, y = 80, width = 150, height = 30)
janela.mainloop()




