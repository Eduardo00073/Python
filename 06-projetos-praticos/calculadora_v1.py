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

# criação dos botões
# linha 1
btnC = Button(frame_corpo, text="C", width=15, height=2, bg="#ECEFF1",
              font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE)
btnC.place(x=0, y=0)

btnPorcentagem = Button(frame_corpo, text="%", width=10, height=2, bg="#ECEFF1",
                        font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE)
btnPorcentagem.place(x=165, y=0)

btnDivisao = Button(frame_corpo, text="/", width=10, height=2, bg="#FFAB40",
                    fg="#feffff", font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE)
btnDivisao.place(x=280, y=0)


# linha 2
btn7 = Button(frame_corpo, text="7", width=8, height=2, bg="#ECEFF1",
              font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE)
btn7.place(x=-2, y=61)

btn8 = Button(frame_corpo, text="8", width=8, height=2, bg="#ECEFF1",
              font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE)
btn8.place(x=94, y=61)

btn9 = Button(frame_corpo, text="9", width=8, height=2, bg="#ECEFF1",
              font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE)
btn9.place(x=190, y=61)

btnMultiplica = Button(frame_corpo, text="*", width=10, height=2, bg="#FFAB40",
                       fg="#feffff", font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE)
btnMultiplica.place(x=280, y=61)


# linha 3
btn4 = Button(frame_corpo, text="4", width=8, height=2, bg="#ECEFF1",
              font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE)
btn4.place(x=-2, y=122)

btn5 = Button(frame_corpo, text="5", width=8, height=2, bg="#ECEFF1",
              font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE)
btn5.place(x=94, y=122)

btn6 = Button(frame_corpo, text="6", width=8, height=2, bg="#ECEFF1",
              font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE)
btn6.place(x=190, y=122)

btnSubtrai = Button(frame_corpo, text="-", width=10, height=2, bg="#FFAB40",
                    fg="#feffff", font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE)
btnSubtrai.place(x=280, y=122)

# execução
janela.mainloop()
