from tkinter import *

# definindo configurações da janela
janela = Tk()
janela.title("Calculadora Python")
janela.geometry("400x405")
janela.config(bg="#1f1f1e")

# criação dos frames do visor
frame_tela = Frame(janela, width=400, height=100, bg="#38576b")
frame_tela.grid(row=0, column=0)

# criação dos frames do corpo da calculadora
frame_corpo = Frame(janela, width=400, height=305)
frame_corpo.grid(row=1, column=0)

# criação do visor
valor_texto = StringVar()

app_visor = Label(frame_tela, textvariable=valor_texto, width=20, height=3, padx=7, relief=FLAT, anchor="e",
                  justify=RIGHT, font="Ivy 24", bg="#38576b", fg="#feffff")
app_visor.place(x=0, y=0)


# coletando dados
valores_calculadora = ''


def entrada_dados(valor):
    global valores_calculadora
    valores_calculadora += str(valor)
    valor_texto.set(valores_calculadora)


# botão calcular
def calcula_dados():
    global valores_calculadora
    resultado = eval(valores_calculadora)
    valor_texto.set(resultado)
    valores_calculadora = ''


# botão limpar
def limpar_tela():
    global valores_calculadora
    valores_calculadora = ''
    valor_texto.set('')


# criação dos botões
# linha 1
btnC = Button(frame_corpo, command=limpar_tela, text="C", width=15, height=2, bg="#ECEFF1",
              font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE)
btnC.place(x=0, y=0)

btnPorcentagem = Button(frame_corpo, command=lambda: entrada_dados("%"), text="%", width=10, height=2, bg="#ECEFF1",
                        font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE)
btnPorcentagem.place(x=165, y=0)

btnDivisao = Button(frame_corpo, command=lambda: entrada_dados("/"), text="/", width=10, height=2, bg="#FFAB40",
                    fg="#feffff", font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE)
btnDivisao.place(x=280, y=0)


# linha 2
btn7 = Button(frame_corpo, command=lambda: entrada_dados("7"), text="7", width=8, height=2, bg="#ECEFF1",
              font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE)
btn7.place(x=-2, y=61)

btn8 = Button(frame_corpo, command=lambda: entrada_dados("8"), text="8", width=8, height=2, bg="#ECEFF1",
              font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE)
btn8.place(x=94, y=61)

btn9 = Button(frame_corpo, command=lambda: entrada_dados("9"), text="9", width=8, height=2, bg="#ECEFF1",
              font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE)
btn9.place(x=190, y=61)

btnMultiplica = Button(frame_corpo, command=lambda: entrada_dados("*"), text="*", width=10, height=2, bg="#FFAB40",
                       fg="#feffff", font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE)
btnMultiplica.place(x=280, y=61)


# linha 3
btn4 = Button(frame_corpo, command=lambda: entrada_dados("4"), text="4", width=8, height=2, bg="#ECEFF1",
              font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE)
btn4.place(x=-2, y=122)

btn5 = Button(frame_corpo, command=lambda: entrada_dados("5"), text="5", width=8, height=2, bg="#ECEFF1",
              font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE)
btn5.place(x=94, y=122)

btn6 = Button(frame_corpo, command=lambda: entrada_dados("6"), text="6", width=8, height=2, bg="#ECEFF1",
              font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE)
btn6.place(x=190, y=122)

btnSubtrai = Button(frame_corpo, command=lambda: entrada_dados("-"), text="-", width=10, height=2, bg="#FFAB40",
                    fg="#feffff", font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE)
btnSubtrai.place(x=280, y=122)


# linha 4
btn4 = Button(frame_corpo, command=lambda: entrada_dados("1"), text="1", width=8, height=2, bg="#ECEFF1",
              font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE)
btn4.place(x=-2, y=182)

btn5 = Button(frame_corpo, command=lambda: entrada_dados("2"), text="2", width=8, height=2, bg="#ECEFF1",
              font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE)
btn5.place(x=94, y=182)

btn6 = Button(frame_corpo, command=lambda: entrada_dados("3"), text="3", width=8, height=2, bg="#ECEFF1",
              font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE)
btn6.place(x=190, y=182)

btnAdiciona = Button(frame_corpo, command=lambda: entrada_dados("+"), text="+", width=10, height=2, bg="#FFAB40",
                     fg="#feffff", font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE)
btnAdiciona.place(x=280, y=182)


# linha 5
btn0 = Button(frame_corpo, command=lambda: entrada_dados("0"), text="0", width=15, height=2, bg="#ECEFF1",
              font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE)
btn0.place(x=0, y=242)

btnPonto = Button(frame_corpo, command=lambda: entrada_dados("."), text=".", width=10, height=2, bg="#ECEFF1",
                  font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE)
btnPonto.place(x=165, y=242)

btnResultado = Button(frame_corpo, command=calcula_dados, text="=", width=10, height=2, bg="#FFAB40", fg="#feffff",
                      font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE)
btnResultado.place(x=280, y=242)


# execução
janela.mainloop()
