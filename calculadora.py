import tkinter as tk


# -------------------------
# Funções do display
# -------------------------

def adicionar_no_display(valor):
    atual = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, atual + str(valor))


def limpar_display():
    display.delete(0, tk.END)


def calcular():
    expressao = display.get()

    try:
        resultado = eval(expressao)

        display.delete(0, tk.END)
        display.insert(tk.END, str(resultado))

    except ZeroDivisionError:
        display.delete(0, tk.END)
        display.insert(tk.END, "Erro: divisão por 0")

    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Erro")


# -------------------------
# Funções das operações
# -------------------------

def somar():
    pass


def subtrair():
    pass


def multiplicar():
    adicionar_no_display("*")


def dividir():
    adicionar_no_display('/')


# -------------------------
# Janela principal
# -------------------------

janela = tk.Tk()
janela.title("Calculadora Clássica")
janela.geometry("250x300")
janela.config(bg="#f0f0f0")


# -------------------------
# Display
# -------------------------

display = tk.Entry(
    janela,
    font=("Arial", 24),
    justify="right",
    bg="#e8f4f8",
    bd=5
)

display.grid(
    row=0,
    column=0,
    columnspan=3,
    ipadx=8,
    ipady=15,
    pady=10,
    padx=10,
    sticky="nsew"
)


# -------------------------
# Botões
# -------------------------

botoes = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('/', 4, 3),
]


for texto, linha, coluna in botoes:
    if texto == 'C':
        comando = limpar_display

    elif texto == '+':
        comando = somar

    elif texto == '-':
        comando = subtrair

    elif texto == '*':
        comando = multiplicar

    elif texto == '/':
        comando = dividir

    else:
        comando = lambda t=texto: adicionar_no_display(t)

    btn = tk.Button(
        janela,
        text=texto,
        font=("Arial", 16, "bold"),
        bg="#ffffff",
        command=comando
    )

    btn.grid(
        row=linha,
        column=coluna,
        sticky="nsew",
        padx=2,
        pady=2
    )


btn_igual = tk.Button(
    janela,
    text='=',
    font=("Arial", 16, "bold"),
    bg="#99ccff",
    command=calcular
)

btn_igual.grid(
    row=5,
    column=0,
    columnspan=4,
    sticky="nsew",
    padx=2,
    pady=2
)


# -------------------------
# Responsividade da tela
# -------------------------

for i in range(3):
    janela.grid_columnconfigure(i, weight=1)

for i in range(1, 5):
    janela.grid_rowconfigure(i, weight=1)


janela.mainloop()