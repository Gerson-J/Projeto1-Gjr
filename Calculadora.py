#Calculadora de 4 operação'.
numero1=float(input("Digite o primeiro número:"))
numero2=float(input("Digite o segundo número:"))
operacao=input("Digite a operação desejada(+,-,*ou/):")

if operacao=='+':
    resultado=numero1+numero2
elif operacao=='-':
    resultado=numero1-numero2
elif operacao=='*':
    resultado=numero1*numero2
elif operacao=='/':
    
    if numero2 !=0:
        resultado=numero1/numero2
    else:
        resultado="Divisão por zero não é possivel."
else:
    resultado="Operação inválida. Por favor, escolha entre +,-,*ou/"
    
print(f"O resultado da operação {operacao} é: {resultado}.")