numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

operacao = input("\nDigite a operação")
calculo = 0

if operacao == "+":
    calculo = numero1 + numero2
elif operacao == "-":
    calculo = numero1 - numero2
elif operacao == "*":
    calculo = numero1 * numero2
elif operacao == "/":
    calculo = numero1 / numero2

print("O resultado é: ", calculo)