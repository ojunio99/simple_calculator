import tkinter as tk
from tkinter import messagebox

def adicao(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        messagebox.showerror("Erro", "Divisão por zero não é permitida.")

def calcular():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())

    if operacao.get() == "+":
        resultado = adicao(num1, num2)
    elif operacao.get() == "-":
        resultado = subtracao(num1, num2)
    elif operacao.get() == "*":
        resultado = multiplicacao(num1, num2)
    elif operacao.get() == "/":
        resultado = divisao(num1, num2)

    # Exibir o resultado no Label
    label_resultado.config(text=f"O resultado é: {resultado}")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Calculadora")

operacao = tk.StringVar()

label_num1 = tk.Label(root, text="Digite o primeiro número:")
label_num1.grid(row=0, column=0)

entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

label_num2 = tk.Label(root, text="Digite o segundo número:")
label_num2.grid(row=1, column=0)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)

button_somar = tk.Radiobutton(root, text="+", variable=operacao, value="+")
button_somar.grid(row=2, column=0)

button_subtrair = tk.Radiobutton(root, text="-", variable=operacao, value="-")
button_subtrair.grid(row=2, column=1)

button_multiplicar = tk.Radiobutton(root, text="*", variable=operacao, value="*")
button_multiplicar.grid(row=3, column=0)

button_dividir = tk.Radiobutton(root, text="/", variable=operacao, value="/")
button_dividir.grid(row=3, column=1)

button_calcular = tk.Button(root, text="Calcular", command=calcular)
button_calcular.grid(row=4, columnspan=2)

# Label para exibir o resultado
label_resultado = tk.Label(root, text="")
label_resultado.grid(row=5, columnspan=2)

root.mainloop()
