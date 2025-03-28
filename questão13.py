salario_inicial = float(input("Digite o salário inicial: "))
anos = int(input("Digite a quantidade de anos: "))
salario_atual = salario_inicial
for i in range(anos):
    salario_atual *= 2
print(f'O salário atual após {anos} anos é: R${salario_atual:.2f}')
