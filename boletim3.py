from time import sleep
print('\033[1;97m=\033[m'*120)
print('\033[1;34m>>> SISTEMA MANIPULAÇÃO DE NOTAS <<<\033[m'.center(120))
print('\033[1;97m=\033[m'*120)
menu = '\033[1m[ 1 ]\033[m\033[0;36m Adicionar aluno;\033[m'\
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
       '\n\033[1;31m[ => ] Digite a opção desejada: \033[;97m'

lista_alunos = dict()
opçao = input(menu)

while opçao != 15:
    if opçao == 1:
        nome = str(input('Digite o nome do aluno: ').capitalize().strip())
        if nome not in lista_alunos:
            lista_alunos[nome] = []
            print('Aluno adicionado com sucesso')
            print(lista_alunos)
        else:
            print('Erro! Aluno escolhido já se encontra no sistema')
    elif opçao == 2:
        nome = str(input('Digite o nome do aluno: ').capitalize().strip())
        if len(lista_alunos[nome]) < 3:
            if nome in lista_alunos:
                nota = float(input('Digite a nota do aluno selecionado: '))
                if nota >= 0 and nota <= 10:
                    lista_alunos[nome].append(nota)
                    print('Nota registrada com sucesso!')
                    print(lista_alunos)
                else:
                    print('Erro! Nota inválida.')
            else:
                print('Erro! O aluno selecionado não está inserido no sistema')
        else:
            print('Erro! Número máximo de notas atingido.')
    elif opçao == 3:
        nome = str(input('Voçe deseja excluir qual aluno: ').capitalize().strip())
        if nome in lista_alunos:
            lista_alunos.pop(nome)
            print(lista_alunos)
            print('Aluno removido com sucesso!')
        else:
            print('O aluno não se encontra no sistema!')
            opçao = int(input(menu))
    elif opçao == 4:
        nome = str(input('Voçe deseja excluir a ultima nota de qual aluno? ').capitalize().strip())
        if nome in lista_alunos:
            print("Notas excluidas com sucesso!!")
            lista_alunos[nome].remove(nota)
            print(lista_alunos)
        else:
            print('O aluno não se encontra no sistema!')
    elif opçao == 5:
        nome = str(input('Voçe deseja editar qual aluno? ').capitalize().strip())
        if nome in lista_alunos:
            lista_alunos.pop(nome)
            nome = str(input('Digite o novo aluno: ')).capitalize().strip()
            lista_alunos[nome] = []
            print('Operação realizada com sucesso!')
            print(lista_alunos)
        else:
            print('O aluno escolhido não se encontra no sistema!')
    elif opçao == 6:
        nome = str(input('Voçe deseja editar a nota de qual aluno? ').capitalize().strip())
        if nome in lista_alunos:
            print(f'As notas do aluno: {lista_alunos[nome]}') # como colocar para exibir a nota de determinado aluno
            pos = input('Qual nota voce gostaria de editar? Digite 1, 2 ou 3 ')
            #del lista_alunos.keys(nota[1]) # duvida jemerson, como acessar a nota especifica para excluir
            if pos == 1:
                nova_nota = lista_alunos[nome](pos -1)
            print('Operação realizada com sucesso!')
            print(lista_alunos)
    elif opçao == 7:

    sleep(0.5)
    opçao = int(input(menu))


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
