from time import sleep
def le_entrada(mensagem, mensagem_erro, tipo, valores,loop) :
    try :
        entrada = tipo(input(mensagem))
        if entrada in valores :
            return entrada
        else :
            print(mensagem_erro)
    except :
        print(mensagem_erro)

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

alunos = {}

opçao = le_entrada(menu, 'Erro. Valor inválido, digite um nº de 1 a 15: ', int, [i for i in range(1, 16)],True)

while opçao != 15:
    if opçao == 1:
        nome = str(input('Digite o nome do aluno: ').upper().strip())
        if nome not in alunos:
            alunos[nome] = []
            print('-' * 30)
            print('Aluno adicionado com sucesso!')
            print('-' * 30)
        else:
            print('ERRO! Aluno escolhido já se encontra no sistema')
    elif opçao == 2:
        nome = str(input('Digite o nome do aluno: ').upper().strip())
        if len(alunos[nome]) < 3:
            if nome in alunos:
                nota = float(input('Digite a nota do aluno selecionado: '))
                if nota >= 0 and nota <= 10:
                    alunos[nome].append(nota)
                    print('Nota registrada com sucesso!')
                else:
                   print('ERRO! Nota inválida.')
            else:
                print('ERRO! O aluno selecionado não está inserido no sistema')
        else:
            print('ERRO! Número máximo de notas atingido.')
    elif opçao == 3:
        nome = str(input('Voçê deseja excluir qual aluno: ').upper().strip())
        if nome in alunos:
            alunos[nome].pop(nome)
            print('Aluno remove com sucesso!')
        else:
            print('O aluno não se encontra no sistema!')
            opçao = int(input(menu))
    elif opçao == 4:
        nome = str(input('Voçe deseja excluir a nota de qual aluno? ').upper().strip())
        if nome in alunos:
            pos = int(input('Digite a posição que deseja remover: '))
            print("Notas excluidas com sucesso!!")
            #del alunos[nome]
            alunos[nome][pos-1] = None
    #elif opçao == 2:
    #    nome = str(input('Voçe deseja adicionar a nota de qual aluno? ').upper().strip())
    #    if nome in alunos:
    #        pos = int(input('Digite a posição que deseja alterar: '))
    #        nova_nota = float('Digite a nova nota: ')
    #        print("Notas excluidas com sucesso!!")
    #        alunos[nome][pos - 1] = nova_nota
    #        else:
    #            print(f'A nota digitada não encontra no sistema de {nome}')
    #    else:
    #        print('O aluno não se encontra no sistema!')
    elif opçao == 5:
        nome = str(input('Voçe deseja editar qual aluno? ').upper().strip())
        if nome in alunos:
            alunos.pop(nome)
            nome = str(input('Digite o novo aluno: ')).upper().strip()
            alunos[nome] = []
            print('Operação realizada com sucesso!')
        else:
            print('O aluno escolhido não se encontra no sistema!')
    elif opçao == 6:
        nome = str(input('Voçe deseja editar a nota de qual aluno? ').upper().strip())
        if nome in alunos:
            #print(f'As notas do aluno {nome} são: {alunos[nota]}') # como colocar para exibir a nota de determinado aluno
            pos_nota = int(input(f'Qual voce gostaria de editar? Digite 1, 2 ou 3 '))
            print('Operação realizada com sucesso!')
            nova_nota = int(input('Digite a nova nota: '))
            alunos[nome][pos_nota - 1] = nova_nota
    sleep(0.2)
    print(alunos)
    opçao = le_entrada(menu, 'Erro. Valor inválido, digite um nº de 1 a 15: ', int, [i for i in range(1, 16)],True)

print('-=' * 30)
sleep(1)
print('>>> Finalizando <<<')
sleep(0.3)
print(alunos)




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
