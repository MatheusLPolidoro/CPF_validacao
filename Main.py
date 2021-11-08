from tkinter import *
from AnaliseCPF import NumeroCPF
import os

pasta_app = os.path.dirname(__file__) + "\\images\\"


def format_cpf(event=None):

    text = numero_cpf.get().replace(".", "").replace("-", "")[:11]
    new_text = ""

    if event.keysym.lower() == "backspace":
        return

    for index in range(len(text)):
        if not text[index] in "0123456789":
            continue
        if index in [2, 5]:
            new_text += text[index] + "."
        elif index == 8:
            new_text += text[index] + "-"
        else:
            new_text += text[index]

    numero_cpf.delete(0, "end")
    numero_cpf.insert(0, new_text)


def main():
    cpf = NumeroCPF(numero_cpf.get())
    cpf.gerar_digitos_verificadores()
    if cpf.confirmar_digitos_verificadores() == True:
        img['file'] = pasta_app + "valido.png"
        lb_mensagem['text'] = 'Válido'
        lb_mensagem['fg'] = 'green'
        regiao = cpf.consultar_regiao()[0]
        img_mapa['file'] = pasta_app + "mapa_" + regiao + ".png"
    else:
        img['file'] = pasta_app + "invalido.png"
        lb_mensagem['text'] = 'Inválido'
        lb_mensagem['fg'] = 'red'
        img_mapa['file'] = pasta_app + "mapa_inicial.png"
    cpf.mostrar_resultado()


janela = Tk()
janela.title("Validar CPF")
janela.geometry("550x650")
janela.configure(background="#dde")
janela.iconbitmap(pasta_app + 'icone.ico')
Label(janela, text="Informe o número do CPF que deseja confirmar:", background="#dde",
      foreground="#005", anchor=W, font="family=Arial").place(x=10, y=10, width=350, height=20)
numero_cpf = Entry(janela, font="family=Arial")
numero_cpf.bind("<KeyRelease>", format_cpf)
numero_cpf.place(x=15, y=40, width=150, height=30)
img = PhotoImage(file=pasta_app + "image.png")
img_mapa = PhotoImage(file=pasta_app + "mapa_inicial.png")

Label(janela, image=img, background="#dde").place(x=450, y=35)
Label(janela, image=img_mapa, background="#dde").place(x=10, y=130)
lb_mensagem = Label(janela, text='', background="#dde", foreground="#005", anchor=CENTER,
                    font="family=Arial 18")
lb_mensagem.place(x=438, y=100, width=88)
Button(janela, text="Enviar", command=main).place(
    x=15, y=80, width=150, height=30)
janela.mainloop()
