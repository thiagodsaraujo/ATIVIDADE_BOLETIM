print('\033[1;97m=\033[m' * 120)
print('\033[1;34m>>> SISTEMA DE MANIPULAÇÃO DE NOTAS <<<\033[m'.center(120))
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

print('\033[1;97m=\033[m' * 120)
print('\033[1;34m>>> SISTEMA MANIPULAÇÃO DE NOTAS <<<\033[m'.center(120))
print('\033[1;97m=\033[m' * 120)

contador = 0
lista_alunos = {}
opçao = int(input(menu))
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
                nota = float(input(f'Digite uma nota para {nome}: '))
                if 0 <= nota <= 10:
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
        nome = str(input('Voçe deseja excluir a nota de qual aluno? ').capitalize().strip())
        for i in lista_alunos.keys(nome):
            print(f'{i:<15}',end='')
            contador += 1
        if nome in lista_alunos:
            nota = int(input(f'Qual nota do aluno {nome} você gostaria de excluir? (1, 2 ou 3)'))
            if nota not in lista_alunos:
                print('A nota digitada ainda não foi catalogada. Selecione outra opção.')
            else:
                if nota == valor[0]:
                    lista_alunos[nome].pop(valor[0])
                elif nota == valor[1]:
                    lista_alunos[nome].pop(valor[1])
                elif nota == valor[2]:
                    lista_alunos[nome].pop(valor[2])
                print("Notas excluidas com sucesso!!")
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
            print(
                f'As notas de {nome} são as seguintes: {lista_alunos[nome]}')  # como colocar para exibir a nota de determinado aluno
            nota = int(input('Qual nota voce gostaria de editar? Digite 1, 2 ou 3 '))
            if nota not in lista_alunos:
                print('A nota digitada ainda não foi catalogada. Selecione outra opção.')
            else:
                if nota == 1:
                    lista_alunos[nome].pop(nota - 1)
                    str(input('Digite a nova nota: '))
                    lista_alunos[nome].index(nota - 1)
                    print('Nota editada com sucesso!')
                elif nota == 2:
                    lista_alunos[nome].pop(nota - 1)
                    str(input('Digite a nova nota: '))
                    lista_alunos[nome].index(nota - 1)
                    print('Nota editada com sucesso!')
                elif nota == 3:
                    lista_alunos[nome].pop(nota - 1)
                    str(input('Digite a nova nota: '))
                    lista_alunos[nome].index(nota - 1)
                    print('Nota editada com sucesso!')
        else:
            print(f'{nome} não se ecnontra no sistema.')

    opçao = int(input(menu))

print(lista_alunos)
