menu_opcoes = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '0')
lista = []

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
        break
    else:
        print('OPCAO_INVALIDA')

if input_usuario == '1':
    lista.append(input())

elif input_usuario == '2':
    print(lista)

elif input_usuario == '3':
    lista.clear()

elif input_usuario == '4':
    maior_lista = max(lista)
    print(maior)

elif input_usuario == '5':
    print(min(lista))

elif input_usuario == '6':
    soma_lista = sum(lista)
    print(soma_lista)

elif input_usuario == '7':
    dobro = []
    for elementos in lista:
        dobro.append(lista*2)
    print(dobro)

elif input_usuario == '8':
    for num in lista:
        if num % 2 == 0:
            print(num)

elif input_usuario == '9':
    for num in lista:
        if num % 2 != 0:
            print(num)

elif input_usuario == '10':
    for i in lista:
        if i >= 0:
            print(i)

elif input_usuario == '11':
    for i in lista:
        if i <= 0:
            print(i)

elif input_usuario == '12':
    lista.reverse()

elif input_usuario == '13':
    lista.sort()
    print(lista)

elif input_usuario == '14':
       lista.sort(reverse)
       print(lista)



   
