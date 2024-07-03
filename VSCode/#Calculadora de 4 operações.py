#Calculadora de 4 operações

numero1 = float(input("Digite um número:"))
numero2 = float(input("Digite outro número:"))
operacao = input("Digite uma operação desejada(+, -, * ou /):")

if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
    resultado = numero1 - numero2
elif operacao == '*':
    resultado = numero1 * numero2
elif operacao == '/':
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Divisão por zero não foi possível."
else:
    resultado = "Operação inválida. Por favor, escolha entre +, -, * ou /."
print(f"O resultado da operação {operacao} é: {resultado}.")    