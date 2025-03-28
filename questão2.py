segundos = int(input("Digite o valor em segundos: "))
dias = segundos // (24 * 3600)
segundos %= (24 * 3600)
horas = segundos // 3600
segundos %= 3600
minutos = segundos // 60
segundos %= 60
print(f'{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos')
