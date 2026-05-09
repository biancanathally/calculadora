import tkinter as tk

def clique_botao(valor):
    atual = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, str(atual) + str(valor))

def limpar_tela():
    display.delete(0, tk.END)

def calcular():
    try:
        conta = display.get()
        resultado = eval(conta)
        display.delete(0, tk.END)
        display.insert(tk.END, str(resultado))
    except Exception:
        display.delete(0, tk.END)
        display.insert(tk.END, "Erro")

janela = tk.Tk()
janela.title("Calculadora Clássica")
janela.geometry("250x300")
janela.config(bg="#f0f0f0")

display = tk.Entry(janela, font=("Arial", 24), justify="right", bg="#e8f4f8", bd=5)
display.grid(row=0, column=0, columnspan=3, ipadx=8, ipady=15, pady=10, padx=10, sticky="nsew")

botoes = [
    ('1', 1, 0), ('2', 1, 1), ('+', 1, 2),
    ('3', 2, 0), ('4', 2, 1), ('-', 2, 2),
    ('*', 3, 0), ('/', 3, 1), ('C', 3, 2),
]

for (texto, linha, coluna) in botoes:
    if texto == 'C':
        btn = tk.Button(janela, text=texto, font=("Arial", 16, "bold"), bg="#ff9999", 
                        command=limpar_tela)
    else:
        btn = tk.Button(janela, text=texto, font=("Arial", 16, "bold"), bg="#ffffff",
                        command=lambda t=texto: clique_botao(t))
    
    btn.grid(row=linha, column=coluna, sticky="nsew", padx=2, pady=2)

btn_igual = tk.Button(janela, text='=', font=("Arial", 16, "bold"), bg="#99ccff", command=calcular)
btn_igual.grid(row=4, column=0, columnspan=3, sticky="nsew", padx=2, pady=2)

for i in range(3):
    janela.grid_columnconfigure(i, weight=1)
for i in range(1, 5):
    janela.grid_rowconfigure(i, weight=1)

janela.mainloop()
