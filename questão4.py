dias_aluguel = int(input("Digite o número de dias que o cliente alugou o carro: "))
km_rodados = float(input("Digite a quantidade de quilômetros rodados: "))
custo_diario = 90
valor_extra = 0
if km_rodados > 100:
    valor_extra = (km_rodados - 100) * 12
valor_total = (dias_aluguel * custo_diario) + valor_extra
print(f'Valor total a ser pago: R${valor_total:.2f}')
