#Faça uma calculadora de 4 operação
numero1=float(input("Digite o primeiro número"))
numero2=float(input("Digite o segundo número"))
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
    
print(f"O resultado da operação {operacao} é:{resultado}.")






#Solicite ao usuário o valor do raio
raio=float(input("Digite o valor do raio da circunferência"))

pi=3.14159

area=pi*(raio*2)

print(f"A área da circunferência com o raio {raio} é:{area}")








#Digite o a temperatura em grau Celsius
celsius=float(input("Digite a temperatura em grau Celsius"))

fahrenheit=(9*celsius+160)/5

print(f"A temperatura de {celsius} graus Celsius equivale a {fahrenheit} graus fahrenheit")


 




#Digite a temperatura em grau Fahrenheit
fahrenheit=float(input("Digite a temperatura em grau Fahrenheit"))

celsius=((fahrenheit-32)*(5/9))

print(f"A temperatura de {fahrenheit} graus Fahrenheit equivale a {celsius} graus Celsius")








#Encontre o maior número

numero1=float(input("Digite o primeiro número"))
numero2=float(input("Digite o segundo número"))
numero3=float(input("Digite o terceiro número"))

maior_numero=max(numero1,numero2,numero3)

print(f"O maior número é:{maior_numero}")










#Leia um número inteiro e mostre uma mensagem indicando se este número é par ou ímpar e se é positivo ou negativo'.
numero=int(input("Digite um número inteiro:"))

if numero%2==0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
    
if numero>0:
    print(f"O número {numero} é positivo.")
elif numero<0:
    print(f"O número {numero} é negativo.")
else:
    print("O número é zero.")











#Crie um programa que peça 5 números inteiros e apresente: a média, o maior e o menor.
numeros = []
for i in range(5):
    numero = float(input(f"Digite o {i+1}° número: "))
    numeros.append(numero)
    
media = sum(numeros) / len(numeros)

maior = max(numeros)
menor = min(numeros)

print(f"A média dos múmeros digitados é: {media}")
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")








# Calcule o fatorial de um número
def calcular_fatorial(numero):
    if numero < 0:
        return "Erro: Não é possível calcular o fatorial de um número negativo"
    else:
        fatorial = 1 
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial 

numero = int(input("Digite um número para calcular o seu fatorial:"))

resultado = calcular_fatorial(numero)
print(f"O fatorial de {numero} é: {resultado}")












#  calcule os quadrados e cubos dos números de 0 a 10
print("Número | Quadrado | Cubo")
print("--------------------------")
for num in range(11):
    quadrado = num ** 2
    cubo = num ** 3
    print(f"{num:6} | {quadrado:8} | {cubo:5}")