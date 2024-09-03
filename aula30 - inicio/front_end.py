from tkinter import *

# cores do projeto
preto = "#000000"
branco = "#feffff"
azul = "#0074eb"
vermelho = "#f04141"
verde = "#59b356"
cinzento = "#cdd1cd"

# janela principal
janela = Tk()
janela.resizable(width=FALSE, height=FALSE)
janela.geometry('500x225')
janela.title('Lista de afazeres')
janela.configure(background=cinzento)

# separando os frames
frame_esquerda = Frame(janela, width=300, height=200, background=branco, relief=FLAT)
frame_esquerda.grid(row=0, column=0, sticky=NSEW)

frame_direita = Frame(janela, width=200, height=250, background=branco, relief=FLAT)
frame_direita.grid(row=0, column=1, sticky=NSEW)

# separação do frame da esquerda
esquerda_cima = Frame(frame_esquerda, width=300, height=50, background=branco, relief=FLAT)
esquerda_cima.grid(row=0, column=0, sticky=NSEW)

esquerda_baixo = Frame(frame_esquerda, width=300, height=150, background=branco, relief=FLAT)
esquerda_baixo.grid(row=1, column=0, sticky=NSEW)

# criação dos botões
btn_adicionar = Button(esquerda_cima, text="Adicionar", width=10, height=1, background=azul, fg=branco, font="5",
                       anchor="center", relief=FLAT)
btn_adicionar.grid(row=0, column=0, sticky=NSEW, pady=1)

btn_excluir = Button(esquerda_cima, text="Excluir", width=10, height=1, background=vermelho, fg=branco, font="5",
                     anchor="center", relief=FLAT)
btn_excluir.grid(row=0, column=2, sticky=NSEW, pady=1)

btn_atualizar = Button(esquerda_cima, text="Atualizar", width=10, height=1, background=verde, fg=branco, font="5",
                       anchor="center", relief=FLAT)
btn_atualizar.grid(row=0, column=3, sticky=NSEW, pady=1)

# lista de exibição
titulo_lista_exibicao = Label(frame_direita, text="Tarefas", width=37, height=1, pady=7, padx=10, relief=FLAT, anchor=W,
                              font="Arial 18", fg=preto, bg=branco)
titulo_lista_exibicao.grid(row=0, column=0, sticky=NSEW, pady=1)

corpo_lista_exibicao = Listbox(frame_direita, font="Arial 10", width=1)
corpo_lista_exibicao.grid(row=1, column=0, sticky=NSEW, pady=5)

# adição de itens na lista
tarefas = ["Pagar boletos", "Gerar relatório", "Reunião empresarial", "Fazer pedidos"]
for item in tarefas:
    corpo_lista_exibicao.insert(END, item)

# rodando a janela
janela.mainloop()
