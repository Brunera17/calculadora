from calculadora import operacoes, calculo

operacao, num1, num2 = operacoes()

while operacao != 0:
    try:
        resultado, texto = calculo(operacao, num1, num2)
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    if operacao != 5:
        print("---------------------")
        print(f"A {texto} dos numeros é igual a: {resultado}")
        print("---------------------")
    operacao, num1, num2 = operacoes()
print("Até mais!")
exit()