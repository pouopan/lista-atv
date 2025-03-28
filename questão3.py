valor_mercadorias = float(input("Digite o valor total das mercadorias compradas: "))
if valor_mercadorias < 500:
    print("Não há imposto.")
else:
    imposto = (valor_mercadorias - 500) * 0.50
    print(f'Imposto a pagar: R${imposto:.2f}')
