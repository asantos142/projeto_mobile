#Membros do Grupo: António Santos e Pedro Guerreiro

lista = []

def dobro(lst):
    double = [number * 2 for number in lst]
    return double

def par(lst):
    n_par = [num for num in lst if num % 2 == 0]
    return n_par

def impar(lst):
    n_impar = [num for num in lst if num % 2 == 1]
    return n_impar

def positivo(lst):
    pos = [num for num in lst if num > 0]
    return pos

def negativo(lst):
    neg = [num for num in lst if num < 0]
    return neg

def receber_input():
    menu_opcoes = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '0')
    
    while True:
        print()
        print('   MENU   ')
        print('1 - Inserir valor na lista ')
        print('2 - Imprimir lista ')
        print('3 - Apagar lista ')
        print('4 - Procurar maior numero da lista ')
        print('5 - Procurar menor numero da lista ')
        print('6 - Imprimir o valor da soma dos números da lista ')
        print('7 - Substituir cada um dos valores da lista pelo seu dobro ')
        print('8 - Imprimir apenas os valores pares ')
        print('9 - Imprimir apenas os valores ímpares ')
        print('10 - Imprimir apenas os valores positivos ')
        print('11 - Imprimir apenas os valores negativos ')
        print('12 - Inverter o conteúdo da lista ')
        print('13 - Ordenar a lista por ordem crescente ')
        print('14 - Ordenar a lista por ordem decrescente')
        print('0 - Sair do programa ')

        print()
        input_usuario = input('Escolha uma opcao: ')

        if input_usuario in menu_opcoes:
            return input_usuario

        else:
            print('OPCAO INVALIDA')

while True:

    input_usuario = receber_input()

    if input_usuario == '1':
        lista.append(int(input()))
        print(lista)

    elif input_usuario == '2':
        print(lista)

    elif input_usuario == '3':
        lista.clear()
        print(lista)

    elif input_usuario == '4':
        maior_lista = max(lista)
        print(maior_lista)

    elif input_usuario == '5':
        print(min(lista))

    elif input_usuario == '6':
        soma_lista = sum(lista)
        print(soma_lista)

    elif input_usuario == '7':
       num_dobro = dobro(lista)
       print(num_dobro)

    elif input_usuario == '8':
        num_par = par(lista)
        print(num_par)

    elif input_usuario == '9':
        num_impar = impar(lista)
        print(num_impar)

    elif input_usuario == '10':
        num_positivo = positivo(lista)
        print(num_positivo)

    elif input_usuario == '11':
        num_negativo = negativo(lista)
        print(num_negativo)

    elif input_usuario == '12':
        lista.reverse()
        print(lista)

    elif input_usuario == '13':
        lista.sort()
        print(lista)

    elif input_usuario == '14':
        lista.sort(reverse=True)
        print(lista)
    
    elif input_usuario == '0':
        break
