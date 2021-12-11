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
lista_alunos = []
boletim = {}
dados = []
opçao = le_entrada(menu, 'Erro. Valor inválido, digite um nº de 1 a 15: ', int, [i for i in range(1, 16)],True)
notas = []
contador = 0
while opçao != 15:
    if opçao == 1:
        lista_alunos.clear()
        lista_alunos['Nome'] = str(input('Digite o nome do aluno: ')).upper().strip()
        if lista_alunos['Nome'].strip().upper() not in boletim.values():
            boletim.copy(lista_alunos)
            print('Aluno adicionado com sucesso!')
        else:
            print('Aluno já consta no nosso sistema, digite outro!')


    sleep(0.2)
    print(lista_alunos)
    opçao = le_entrada(menu, 'Erro. Valor inválido, digite um nº de 1 a 15: ', int, [i for i in range(1, 16)],True)

print('-=' * 30)
sleep(1)
print('>>> Finalizando <<<')
sleep(0.3)
print(boletim)