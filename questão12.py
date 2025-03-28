quantidade_turmas = int(input("Digite a quantidade de turmas: "))
quantidade_alunos = int(input("Digite a quantidade total de alunos: "))
media_alunos = quantidade_alunos / quantidade_turmas
print(f'A média de alunos por turma é: {media_alunos:.2f}')
if media_alunos > 40:
    print("Aviso: Algumas turmas têm mais de 40 alunos.")
