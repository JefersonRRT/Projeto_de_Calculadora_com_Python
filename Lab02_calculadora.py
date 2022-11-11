#1º Passo > Imprimir na tela o nome do projeto

print("\n******************* Python Calculator *******************\n")

#2º Passo > Imprimir na tela as 6 possíveis operações que o usuário deve informar no próximo passo

print("Selecione a opção de operação:\n"
      "\n"
      "1 - Somar\n"
      "2 - Subtrair\n"
      "3 - Multiplicar\n"
      "4 - Dividir\n"
      "5 - Exponenciação\n"
      "6 - Raiz\n")

#3º Passo > Imprimir na tela o pedido de um número inteiro, que deve ser informado pelo usuário da calculadora, e
#   colocar este valor na variável 'x'

x = int(input('Digite sua opção (1/2/3/4/5/6): '))

#4º Passo > Após a escolha do usuário, fazer a verificação deste número de acordo com condicionais abaixo.
#   Caso a escolha seja um número inteiro, abaixo de 1 OU maior que 6, o programa se encerra e imprime a mensagem:
#       'Opção Inválida'
#   Caso a escolha for diferente dessa condição, o programa continua.

if x < 1 or x > 6:
    print('\nOpção inválida.')
else:
    pass

#   Se o valor informado pelo usuário for um numero inteiro, maior ou igual a 1 e menor ou igual a 4 as condicionais
#       sao executadas, e o programa pede ao usuário dois números para executar a operação desejada;

    if x >=1 or x <= 4:
        a = int(input('\nDigite o primeiro número: '))
        b = int(input('\nDigite o segundo número: '))

    #   Se a opção escolhida no inicio, onde a variável x = 1, a calculadora irá executar a soma dos dois numeros informados:

    if x == 1:
        print(f'\n{a} + {b} =', (a + b))

    #   Se a opção escolhida no inicio, onde a variável x = 2, a calculadora irá executar a subtração dos dois numeros informados:

    elif x == 2:
        print(f'\n{a} - {b} =', (a - b))

    #   Se a opção escolhida no inicio, onde a variável x = 3, a calculadora irá executar a multiplicação dos dois numeros informados:

    elif x == 3:
        print(f'\n{a} x {b} =', (a * b))

    #   Se a opção escolhida no inicio, onde a variável x = 4, a calculadora irá executar a divisão dos dois numeros informados:

    elif x == 4:
        print(f'\n{a} / {b} =', (a / b))

    #   Se a opção escolhida no inicio, onde a variável x = 5, a calculadora irá executar a exponenciação dos numeros informados:
    #       Onde o primeiro número informado é a base, e o segundo é o expoente:

    elif x == 5:
        print(f'\n{a} ^ {b} =', (a ** b))

    #   Se a opção escolhida no inicio, onde a variável x = 1, a calculadora irá executar a raiz dos numeros informados:
    #       Onde o primeiro número informado é o indice da raiz e o segundo numero é o radicando.

    elif x == 6:
        print(f'\nRaiz {a} de {b} = ', (b ** (1/a)))
    pass

