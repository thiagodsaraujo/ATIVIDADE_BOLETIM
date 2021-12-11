from time import sleep

print('\033[1;97m=\033[m' * 120)
print('\033[1;34m>>> SISTEMA MANIPULAÇÃO DE NOTAS <<<\033[m'.center(120))
print('\033[1;97m=\033[m' * 120)
menu = '\033[1m[ 1 ]\033[m\033[0;36m Adicionar aluno;\033[m' \
       '\n\033[1m[ 2 ]\033[m\033[0;36m Adicionar nota;\033[m' \
       '\n\033[1m[ 3 ]\033[m\033[0;36m Remover aluno;\033[m' \
       '\n\033[1m[ 4 ]\033[m\033[0;36m Remover nota;\033[m' \
       '\n\033[1m[ 5 ]\033[m\033[0;36m Editar nome de aluno;\033[m' \
       '\n\033[1m[ 6 ]\033[m\033[0;36m Editar nota de aluno;\033[m' \
       '\n\033[1m[ 7 ]\033[m\033[0;36m Buscar aluno por nome;\033[m' \
       '\n\033[1m[ 8 ]\033[m\033[0;36m Calular média da turma;\033[m' \
       '\n\033[1m[ 9 ]\033[m\033[0;36m Exibir o melhor aluno;\033[m' \
       '\n\033[1m[ 10 ]\033[m\033[0;36m Exibir alunos em ordem alfabética;\033[m' \
       '\n\033[1m[ 11 ]\033[m\033[0;36m Exibir alunos ordenados por nota;\033[m' \
       '\n\033[1m[ 12 ]\033[m\033[0;36m Exibir alunos aprovados por média;\033[m' \
       '\n\033[1m[ 13 ]\033[m\033[0;36m Exibir alunos na final;\033[m' \
       '\n\033[1m[ 14 ]\033[m\033[0;36m Exibir alunos reprovados;\033[m' \
       '\n\033[1m[ 15 ]\033[m\033[0;36m Encerrar programa.\033[m' \
       '\n\033[0;31mDigite a opção desejada: \033[m'
menu_erro = '\033[1m[ 1 ]\033[m\033[0;36m Adicionar aluno;\033[m' \
            '\n\033[1m[ 2 ]\033[m\033[0;36m Adicionar nota;\033[m' \
            '\n\033[1m[ 3 ]\033[m\033[0;36m Remover aluno;\033[m' \
            '\n\033[1m[ 4 ]\033[m\033[0;36m Remover nota;\033[m' \
            '\n\033[1m[ 5 ]\033[m\033[0;36m Editar nome de aluno;\033[m' \
            '\n\033[1m[ 6 ]\033[m\033[0;36m Editar nota de aluno;\033[m' \
            '\n\033[1m[ 7 ]\033[m\033[0;36m Buscar aluno por nome;\033[m' \
            '\n\033[1m[ 8 ]\033[m\033[0;36m Calular média da turma;\033[m' \
            '\n\033[1m[ 9 ]\033[m\033[0;36m Exibir o melhor aluno;\033[m' \
            '\n\033[1m[ 10 ]\033[m\033[0;36m Exibir alunos em ordem alfabética;\033[m' \
            '\n\033[1m[ 11 ]\033[m\033[0;36m Exibir alunos ordenados por nota;\033[m' \
            '\n\033[1m[ 12 ]\033[m\033[0;36m Exibir alunos aprovados por média;\033[m' \
            '\n\033[1m[ 13 ]\033[m\033[0;36m Exibir alunos na final;\033[m' \
            '\n\033[1m[ 14 ]\033[m\033[0;36m Exibir alunos reprovados;\033[m' \
            '\n\033[1m[ 15 ]\033[m\033[0;36m Encerrar programa.\033[m' \
            '\n\033[0;31m ERRO! Digite uma opção entre 1 e 15: \033[m'

lista_alunos = dict()
opçao = str(input(menu))

while True:
    if opçao.isdigit():
        pass
    else:
        print('ERRO! Digite somente número!')
        break

print('-=' * 30)
sleep(1)
print('>>> Finalizando <<<')
sleep(0.5)
print(lista_alunos)

'''# Formula da média
media = float(nota1 + nota2 + nota3 + nota4) / 4
# Arredondamento do resultado
media = round(media, 1)

# Estruturas condicionais em relação a media
if (media < 4.5):
    print('A média total do(a) aluno(a) ', aluno, ' foi ', media)
    print('Aluno(a) Reprovado')
elif (media >= 4.5 and media <= 6.9):
    print('A média total do(a) aluno(a) ', aluno, ' foi ', media)
    print('Aluno(a) em Recuperação')
else:
    print('A média total do(a) aluno(a) ', aluno, ' foi ', media)
    print('Aluno Aprovado')'''

'''from time import sleep
print('-' * 60)
print('Media dos alunos'.center(60))
print('-' * 60)
media = maiornota = menornota = numalunos = totnotas = 0
notas = float(input('Notas dos alunos e digite 0 para parar de digitar notas: '))
while notas != 0:
    notas = float(input('Notas dos alunos e digite 0 para parar de digitar notas: '))
    numalunos += 1
    totnotas += notas
    if maiornota < notas and menornota < notas:
        maiornota = notas
        menornota = notas
    elif notas > maiornota:
        maiornota = notas
    elif notas < menornota:
        if notas != 0:
            menornota = notas
media = totnotas / numalunos
print('Calculando...')
sleep(1)
print('-' * 60)
print(f'A média das notas dos alunos é {media:.2f}')
print(f'A maior nota dos alunos foi {maiornota}')
print(f'A menor nota dos alunos foi {menornota}')'''
