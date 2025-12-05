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


operacao, num1, num2 = operacoes()

while operacao != 0:
    try:
        if operacao == 1:
            texto = "soma"
            calculo = soma(num1, num2)
        elif operacao == 2:
            texto = "subtração"
            calculo = subtracao(num1, num2)
        elif operacao == 3:
            texto = "multiplicação"
            calculo = multiplicacao(num1, num2)
        elif operacao == 4:
            texto = "divisão"
            calculo = divisao(num1, num2)
        else:
            print("Operação inválida")
            operacao = 5
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    if operacao != 5:
        print("---------------------")
        print(f"A {texto} dos numeros é igual a: {calculo}")
        print("---------------------")
    operacao, num1, num2 = operacoes()
print("Até mais!")