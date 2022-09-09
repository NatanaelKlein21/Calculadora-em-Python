from tkinter import *
from tkinter import ttk
from unittest import result

# CORES 
cor1 = "#1a1919" # preta
cor2 = "#feffff" # branca
cor3 = "#38576b" # azul carregado
cor4 = "#ECEFF1" # cinzenta
cor5 = "#FFAB40" # laranja

janela = Tk()
janela.title('Calculadora')
janela.geometry('242x270')
janela.config(bg=cor1)

# FRAMES
frame_tela = Frame(janela, width=242, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=242, height=220)
frame_corpo.grid(row=1, column=0)


todos_valores = ''
valor_texto = StringVar()

# FUNCOES
def entrar_valores(event):

    global todos_valores
    todos_valores = todos_valores + str(event)
    # passando valor para tela
    valor_texto.set(todos_valores)

def calcular():

    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))

def limpar_tela():

    global todos_valores
    todos_valores = ''
    valor_texto.set('')

# LABEL
app_label = Label(
    frame_tela,  
    textvariable = valor_texto, 
    width=16, 
    height=2, 
    padx=7, 
    relief=FLAT, 
    anchor="e", 
    justify=RIGHT, 
    font=('Ivy 22'), 
    bg=cor3, 
    fg=cor2
)

app_label.place(x=0, y=0)


# BOTOES
# linha 1
b_1 = Button(
    frame_corpo, 
    command = lambda: limpar_tela(),
    text="C", 
    width=10, 
    height=2, 
    bg=cor4, 
    font=('Ivy 13 bold'), 
    relief=RAISED, 
    overrelief=RIDGE
)
b_2 = Button(
    frame_corpo, 
    command = lambda: entrar_valores("%"),
    text="%", 
    width=3, 
    height=2, 
    bg=cor4, 
    font=('Ivy 13 bold'), 
    relief=RAISED, 
    overrelief=RIDGE
)
b_3 = Button(
    frame_corpo,
    command = lambda: entrar_valores("/"),
    text="/", 
    width=3, 
    height=2, 
    fg=cor5, 
    font=('Ivy 13 bold'), 
    relief=RAISED, 
    overrelief=RIDGE
)
b_1.place(x=0, y=0)
b_2.place(x=120, y=0)
b_3.place(x=180, y=0)

# linha 2
b_4 = Button(
    frame_corpo, 
    command = lambda: entrar_valores("7"),
    text="7", 
    width=3, 
    height=2, 
    bg=cor4, 
    font=('Ivy 13 bold'), 
    relief=RAISED, 
    overrelief=RIDGE
)
b_5 = Button(
    frame_corpo, 
    command = lambda: entrar_valores("8"),
    text="8", 
    width=3, 
    height=2, 
    bg=cor4, 
    font=('Ivy 13 bold'), 
    relief=RAISED, 
    overrelief=RIDGE
)
b_6 = Button(
    frame_corpo, 
    command = lambda: entrar_valores("9"),
    text="9", 
    width=3, 
    height=2, 
    bg=cor4, 
    font=('Ivy 13 bold'), 
    relief=RAISED, 
    overrelief=RIDGE
)
b_7 = Button(
    frame_corpo, 
    command = lambda: entrar_valores("*"),
    text="*", 
    width=3, 
    height=2, 
    fg=cor5, 
    font=('Ivy 13 bold'), 
    relief=RAISED, 
    overrelief=RIDGE
)
b_4.place(x=0, y=41)
b_5.place(x=60, y=41)
b_6.place(x=120, y=41)
b_7.place(x=180, y=41)

# linha 3
b_8 = Button(
    frame_corpo, 
    command = lambda: entrar_valores("4"),
    text="4", 
    width=3, 
    height=2, 
    bg=cor4, 
    font=('Ivy 13 bold'), 
    relief=RAISED, 
    overrelief=RIDGE
)
b_9 = Button(
    frame_corpo, 
    command = lambda: entrar_valores("5"),
    text="5", 
    width=3, 
    height=2, 
    bg=cor4, 
    font=('Ivy 13 bold'), 
    relief=RAISED, 
    overrelief=RIDGE
)
b_10 = Button(
    frame_corpo, 
    command = lambda: entrar_valores("6"),
    text="6", 
    width=3, 
    height=2, 
    bg=cor4, 
    font=('Ivy 13 bold'), 
    relief=RAISED, 
    overrelief=RIDGE
)
b_11 = Button(
    frame_corpo, 
    command = lambda: entrar_valores("-"),
    text="-", 
    width=3, 
    height=2, 
    bg=cor4, 
    fg=cor5, 
    font=('Ivy 13 bold'), 
    relief=RAISED, 
    overrelief=RIDGE
)
b_8.place(x=0, y=82)
b_9.place(x=60, y=82)
b_10.place(x=120, y=82)
b_11.place(x=180, y=82)

# linha 4
b_12 = Button(
    frame_corpo, 
    command = lambda: entrar_valores("1"),
    text="1", 
    width=3, 
    height=2, 
    bg=cor4, 
    font=('Ivy 13 bold'), 
    relief=RAISED, 
    overrelief=RIDGE
)
b_13 = Button(
    frame_corpo, 
    command = lambda: entrar_valores("2"),
    text="2", 
    width=3, 
    height=2, 
    bg=cor4, 
    font=('Ivy 13 bold'), 
    relief=RAISED, 
    overrelief=RIDGE
)
b_14 = Button(
    frame_corpo, 
    command = lambda: entrar_valores("3"),
    text="3", 
    width=3, 
    height=2, 
    bg=cor4, 
    font=('Ivy 13 bold'), 
    relief=RAISED, 
    overrelief=RIDGE
)
b_15 = Button(
    frame_corpo, 
    command = lambda: entrar_valores("+"),
    text="+", 
    width=3, 
    height=2, 
    bg=cor4, 
    fg=cor5, 
    font=('Ivy 13 bold'), 
    relief=RAISED, 
    overrelief=RIDGE
)
b_12.place(x=0, y=123)
b_13.place(x=60, y=123)
b_14.place(x=120, y=123)
b_15.place(x=180, y=123)

# linha 5
b_16 = Button(
    frame_corpo, 
    command = lambda: entrar_valores("0"),
    text="0", 
    width=10, 
    height=2, 
    bg=cor4, 
    font=('Ivy 13 bold'), 
    relief=RAISED, 
    overrelief=RIDGE
)
b_18 = Button(
    frame_corpo, 
    command = lambda: entrar_valores("."),
    text=".", 
    width=3, 
    height=2, 
    bg=cor4, 
    font=('Ivy 13 bold'), 
    relief=RAISED, 
    overrelief=RIDGE
)
b_19 = Button(
    frame_corpo, 
    command = lambda: calcular(),
    text="=", 
    width=3, 
    height=2, 
    bg=cor2, 
    fg=cor5, 
    font=('Ivy 13 bold'), 
    relief=RAISED, 
    overrelief=RIDGE
)
b_16.place(x=0, y=164)
b_18.place(x=120, y=164)
b_19.place(x=180, y=164)


janela.mainloop()