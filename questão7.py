numero_impar = int(input("Digite um número ímpar: "))
if numero_impar % 2 == 0:
    print("O número digitado não é ímpar.")
else:
    quadrado_anterior = (numero_impar - 2) ** 2
    quadrado_proximo = (numero_impar + 2) ** 2
    diferenca = quadrado_proximo - quadrado_anterior
    print(f'A diferença entre os quadrados é: {diferenca}')
