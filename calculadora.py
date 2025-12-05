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
        texto = "soma"
        return soma(num1, num2), texto
    elif operacao == 2:
        texto = "subtração"
        return subtracao(num1, num2), texto
    elif operacao == 3:
        texto = "multiplicação"
        return multiplicacao(num1, num2), texto
    elif operacao == 4:
        texto = "divisão"
        return divisao(num1, num2), texto
    else:
        print("Operação inválida")
        operacao = 5
        return operacao