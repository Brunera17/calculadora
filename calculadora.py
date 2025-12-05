def soma(num1, num2):
    return num1 + num2
def subtracao(num1, num2):
    return num1 - num2
def multiplicacao(num1, num2):
    return num1 * num2
def divisao(num1, num2):
    return num1 / num2

def operacoes():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print("---------------------")
    print("Selecione a Operação:")
    print("---------------------")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("---------------------")
    print("0. Sair")
    print("---------------------")
    operacao = int(input("Digite a operação (1/2/3/4) ou 0: "))
    return operacao, num1, num2

def calculo(operacao, num1, num2):
    if operacao == 1:
        return soma(num1, num2)
    elif operacao == 2:
        return subtracao(num1, num2)
    elif operacao == 3:
        return multiplicacao(num1, num2)
    elif operacao == 4:
        return divisao(num1, num2)
    else:
        print("Operação inválida")
        operacao = 5
        return operacao


operacao, num1, num2 = operacoes()

while operacao != 0:
    try:
        calculo = calculo(operacao, num1, num2)
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    if operacao != 5:
        print("---------------------")
        print(f"A {texto} dos numeros é igual a: {calculo}")
        print("---------------------")
    operacao, num1, num2 = operacoes()
print("Até mais!")