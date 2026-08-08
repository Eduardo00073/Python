from tkinter import *
from back_end import *

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


def main(valor):
    # novo item
    if valor == "Adicionar":
        for widget in esquerda_baixo.winfo_children():
            widget.destroy()

        def adicionar():
            tarefa_entrada = entrada.get()
            inserir([tarefa_entrada])
            mostrar_itens()
            entrada.delete(0, END)

        tarefa = Label(esquerda_baixo, text="Informe a nova tarefa abaixo", width=32, height=4, pady=15,
                       relief=FLAT, anchor=CENTER, font="Arial 12", fg=preto, bg=branco)
        tarefa.grid(row=0, column=0, sticky=NSEW)

        entrada = Entry(esquerda_baixo, width=15)
        entrada.grid(row=1, column=0, sticky=NSEW)

        btn_add_tarefa = Button(esquerda_baixo, text="Adicionar tarefa", width=9, height=1, pady=10, background=azul,
                                fg=branco, font="5", anchor="center", relief=FLAT, command=adicionar)
        btn_add_tarefa.grid(row=2, column=0, sticky=NSEW, pady=15)

    if valor == "Atualizar":
        for widget in esquerda_baixo.winfo_children():
            widget.destroy()

        def on():
            nova_tarefa = Label(esquerda_baixo, text="Informe o novo valor da tarefa abaixo", width=32, height=4,
                                pady=15, relief=FLAT, anchor=CENTER, font="Arial 12", fg=preto, bg=branco)
            nova_tarefa.grid(row=0, column=0, sticky=NSEW)

            entrada_atualizar = Entry(esquerda_baixo, width=15)
            entrada_atualizar.grid(row=1, column=0, sticky=NSEW)

            valor_selecionado = corpo_lista_exibicao.curselection()[0]
            palavra = corpo_lista_exibicao.get(valor_selecionado)
            entrada_atualizar.insert(0, palavra)

            tarefas = buscar()

            def alterar():
                for item in tarefas:
                    if palavra == item[1]:
                        nova_palavra = [entrada_atualizar.get(), item[0]]
                        atualizar(nova_palavra)
                        entrada_atualizar.delete(0, END)

                mostrar_itens()

            btn_altera_tarefa = Button(esquerda_baixo, text="Atualizar tarefa", width=9, height=1, pady=10,
                                       background=verde, fg=branco, font="5", anchor="center", relief=FLAT,
                                       command=alterar)
            btn_altera_tarefa.grid(row=2, column=0, sticky=NSEW, pady=15)

        on()


# remover item
def remover():
    for widget in esquerda_baixo.winfo_children():
        widget.destroy()

    valor_selecionado = corpo_lista_exibicao.curselection()[0]
    palavra = corpo_lista_exibicao.get(valor_selecionado)

    tarefas = buscar()

    for item in tarefas:
        if palavra == item[1]:
            deletar([item[0]])

        msg_removido = Label(esquerda_baixo, text="Tarefa removida!", width=32, height=5, pady=15,
                             relief=FLAT, anchor=CENTER, font="Arial 12", fg=preto, bg=branco)
        msg_removido.grid(row=0, column=0, sticky=NSEW)

    mostrar_itens()


# criação dos botões
btn_adicionar = Button(esquerda_cima, text="Adicionar", width=10, height=1, background=azul, fg=branco, font="5",
                       anchor="center", relief=FLAT, command=lambda: main("Adicionar"))
btn_adicionar.grid(row=0, column=0, sticky=NSEW, pady=1)

btn_excluir = Button(esquerda_cima, text="Excluir", width=10, height=1, background=vermelho, fg=branco, font="5",
                     anchor="center", relief=FLAT, command=remover)
btn_excluir.grid(row=0, column=2, sticky=NSEW, pady=1)

btn_atualizar = Button(esquerda_cima, text="Atualizar", width=10, height=1, background=verde, fg=branco, font="5",
                       anchor="center", relief=FLAT, command=lambda: main("Atualizar"))
btn_atualizar.grid(row=0, column=3, sticky=NSEW, pady=1)

# lista de exibição
titulo_lista_exibicao = Label(frame_direita, text="Tarefas", width=37, height=1, pady=7, padx=10, relief=FLAT, anchor=W,
                              font="Arial 18", fg=preto, bg=branco)
titulo_lista_exibicao.grid(row=0, column=0, sticky=NSEW, pady=1)

corpo_lista_exibicao = Listbox(frame_direita, font="Arial 10", width=1)
corpo_lista_exibicao.grid(row=1, column=0, sticky=NSEW, pady=5)


# adição de itens na lista
def mostrar_itens():
    corpo_lista_exibicao.delete(0, END)
    tarefas = buscar()
    for item in tarefas:
        corpo_lista_exibicao.insert(END, item[1])


mostrar_itens()

# rodando a janela
janela.mainloop()
