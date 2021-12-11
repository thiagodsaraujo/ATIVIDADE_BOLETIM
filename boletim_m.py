from time import sleep
import emoji

alunos = {}


def media_turma(alunos):
    media_total = 0
    for nome, nota in alunos.items():
        media = sum(nota) / len(nota)
        media_total += media
    print(f'Média total da turma: {media_total / len(alunos):.2f}')


def media_aluno(alunos):
    for nome, nota in alunos.items():
        print(f'Média do aluno {nome}: ', end='')
        media = sum(nota) / len(nota)
        print(f'{media:.2f}')


def print_similares(alunos):
    nome = str(input('Voçe deseja procurar por qual aluno? ').upper().strip())
    achou = False
    for aluno in alunos:
        if nome in aluno:
            print(f'\033[1;31m=>  {aluno}\033[m encontra-se no sistema!!')
            print('\033[1;31m=> Aluno:\033[m {} \n\033[1;31m=> Nota:\033[m{}'.format(nome, alunos[nome][::]))
            achou = True
    if not achou:
        print('Não achei esse aluno, tente novamente!')


def le_entrada(mensagem, mensagem_erro, tipo, valores, loop):
    try:
        entrada = tipo(input(mensagem))
        if entrada in valores:
            return entrada
        else:
            print(mensagem_erro)
    except:
        print(mensagem_erro)


def situaçao_aluno(alunos):
    for nome, nota in alunos.items():
        print(f'Média do aluno {nome}: ', end='')
        media = sum(nota) / len(nota)
        print(f'{media:.2f}')
        if media < 4.5:
            print('Aluno(a) Reprovado')
        elif 4.5 <= media <= 6.9:
            print('Aluno(a) em Recuperação')
        else:
            print('Aluno Aprovado')


# maior = max([len(nome) for nome in lista])
##formatacao = '1. %-' + str(maior+1) + 's: 5.0'
# for nome in lista :
#    print(formatacao % nome)

def exibir_alunos(alunos):
    print('\033[1;97m=\033[m' * 40)
    print(f'\033[1;30;107m {"Cod":<6}{"Nome":<12}{"Nota(s)":<2} {"Média":>15}      \033[m')
    pos = 1
    for k, v in alunos.items():
        print('%d. - %-10s: %8s' % (pos, k, v))
        pos += 1
    print('\033[1;97m=\033[m' * 40)


# def media(alunos):


# def media:

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
       '\n\033[1;31m[ => ] Digite a opção desejada: \033[;97m'

opçao = le_entrada(menu, 'Erro. Valor inválido, digite um nº de 1 a 15: ', int, [i for i in range(1, 16)], True)

while opçao != 15:
    if opçao == 1:
        nome = str(input('Digite o nome do aluno: ').upper().strip())
        if nome not in alunos:
            alunos[nome] = []
            print('Aluno adicionado com sucesso!', end=' ')
            print(emoji.emojize(':check_mark:'))
        else:
            print('ERRO! Aluno escolhido já se encontra no sistema', end=' ')
            print(emoji.emojize(':cross_mark:'))
    elif opçao == 2:
        exibir_alunos(alunos)
        nome = str(input('Digite o nome do aluno: ').upper().strip())
        if nome in alunos:
            if len(alunos[nome]) < 3:
                nota = float(input('Digite uma nota para o aluno selecionado: '))
                if nota >= 0 and nota <= 10:
                    alunos[nome].append(nota)
                    print('Nota registrada com sucesso!', end=' ')
                    print(emoji.emojize(':check_mark:'))
                else:
                    print('ERRO! Nota inválida.', end=' ')
                    print(emoji.emojize(':cross_mark:'))
            else:
                print('ERRO! Número máximo de notas atingido.', end=' ')
                print(emoji.emojize(':cross_mark:'))
        else:
            print('ERRO! O aluno selecionado não está inserido no sistema', end=' ')
            print(emoji.emojize(':cross_mark:'))
            opçao = int(input(menu))
    elif opçao == 3:
        exibir_alunos(alunos)
        nome = str(input('Voçê deseja excluir qual aluno? [cod] ').upper().strip())
        if nome in alunos:
            del alunos[nome]
            print('Aluno removido com sucesso!', end=' ')
            print(emoji.emojize(':check_mark:'))
        else:
            print('O aluno não se encontra no sistema!', end=' ')
            print(emoji.emojize(':cross_mark:'))
            opçao = int(input(menu))
    elif opçao == 4:
        exibir_alunos(alunos)
        nome = str(input('Voçe deseja excluir a nota de qual aluno? ').upper().strip())
        if nome in alunos:
            exibir_alunos(alunos)
            pos = int(input('Digite a posição que deseja remover: '))
            print("Notas excluidas com sucesso!!", end=' ')
            print(emoji.emojize(':check_mark:'))
            alunos[nome][pos - 1] = 0
    elif opçao == 5:
        exibir_alunos(alunos)
        nome = str(input('Voçe deseja editar qual aluno? ').upper().strip())
        if nome in alunos:
            alunos.pop(nome)
            nome = str(input('Digite o novo aluno: ')).upper().strip()
            alunos[nome] = []
            print('Operação realizada com sucesso!', end=' ')
            print(emoji.emojize(':check_mark:'))
        else:
            print('O aluno escolhido não se encontra no sistema!', end=' ')
            print(emoji.emojize(':cross_mark:'))
    elif opçao == 6:
        exibir_alunos(alunos)
        nome = str(input('Voçe deseja editar a nota de qual aluno? ').upper().strip())
        if nome in alunos:
            # print(f'As notas do aluno {nome} são: {alunos[nota]}') # como colocar para exibir a nota de determinado aluno
            pos_nota = int(input(f'Qual voce gostaria de editar? Digite 1, 2 ou 3 '))
            print('Operação realizada com sucesso!', end=' ')
            print(emoji.emojize(':check_mark:'))
            nova_nota = int(input('Digite a nova nota: '))
            alunos[nome][pos_nota - 1] = nova_nota
    elif opçao == 7:
        print_similares(alunos)
    elif opçao == 8:
        media_turma(alunos)
        pass
    elif opçao == 9:
        # O melhor aluno da turma é aquele que possui maior média. Ele é exibido no formato já conhecido.
        pass
    elif opçao == 10:
        pass
        # Exibe uma ordem alfabética dos alunos:
        # 1. Alessandro José. Notas: 7.0 9.0 e 2.0. Média: 6.0
        # 2. Bruno Paulo. Notas: 2.0 2.0 e 2.0. Média: 2,0
    elif opçao == 11:
        pass
        # 11.Exibir Aluno Por Ordenados Por Nota Similar ao ponto 10. Mas a ordenação considera a maior nota. Dica: é preciso implementar o Insertion Sort.
    elif opçao == 12:
        for nome, nota in alunos.items():
            print(f'Média do aluno {nome}: ', end='')
            media = sum(nota) / len(nota)
            print(f'{media:.2f}')
            if media < 4.5:
                print('Aluno(a) Reprovado')
            elif 4.5 <= media <= 6.9:
                print('Aluno(a) em Recuperação')
            else:
                print('Aluno Aprovado')
    elif opçao == 13:
        for nome, nota in alunos.items():
            print(f'Média do aluno {nome}: ', end='')
            media = sum(nota) / len(nota)
            print(f'{media:.2f}')
            if 5.0 <= media <= 6.9:
                print(f'{nome} está na Final')
            else:
                print('Não temos nenhum aluno na final!')
        pass
    elif opçao == 14:
        for nome, nota in alunos.items():
            print(f'Média do aluno {nome}: ', end='')
            media = sum(nota) / len(nota)
            print(f'{media:.2f}')
            if media < 5.0:
                print(f'{nome} está Reprovado!')
            else:
                print('Não temos alunos reprovados')
    sleep(0.2)
    exibir_alunos(alunos)
    opçao = le_entrada(menu, 'Erro. Valor inválido, digite um nº de 1 a 15: ', int, [i for i in range(1, 16)], True)

print('-=' * 30)
sleep(1)
print('>>> Finalizando <<<')
print(alunos)
exibir_alunos(alunos)

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
print(f'A menor nota dos alunos foi {menornota}')

elif comando == 10:
                for i in range(0, len(nota_media)):
                    while i>0:
                        if nota_media[i-1][1] < nota_media[i][1]:
                           nota_media[i-1][1],nota_media[i][1] =nota_media[i][1],nota_media[i-1][1]
                           nota_media[i-1][0],nota_media[i][0] =nota_media[i][0],nota_media[i-1][0]
                        i-=1

                for i in range(0, len(nota_media)):
                    nome = nota_media[i][0]
'''




