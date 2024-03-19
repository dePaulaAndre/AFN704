try:
 
    #Funções lambda
    subtracao = lambda x, y: x - y
    multiplicacao = lambda x, y: x * y
    soma = lambda x, y: x + y
    divisao = lambda x, y: x / y if y != 0 else None
    quadrado = lambda x, f: f(x * x) 
   

    entrada = 1
    while entrada != 0:
        entrada = input("Escolha uma das opções:"
                        "\n 1 - Soma"
                        "\n 2 - Subtração"
                        "\n 3 - Multiplicação"
                        "\n 4 - Divisão"
                        "\n 5 - Potenciação"
                        "\n 6 - Triplo dos números inseridos"
                        "\n 7 - Faça a sua operação"
                        "\n 8 - Números pares e ímpares até o número informado"
                        "\n 0 - Sair"
                        "\n Opção: ")

        try:
            entrada = int(entrada)

            if entrada == 1:
                print("Soma")
                x = int(input("Digite um número: "))
                y = int(input("Digite outro número: "))
                print("O resultado da soma de ", x, " + ", y, " é:", soma(x, y))

            elif entrada == 2:
                print("Subtração")
                x = int(input("Digite um número: "))
                y = int(input("Digite outro número: "))
                print("O resultado da subtração de ", x, " por ", y, " é:", subtracao(x, y))
            
            elif entrada == 3:
                print("Multiplicação")
                x = int(input("Digite um número: "))
                y = int(input("Digite outro número: "))
                print("O resultado da multiplicação de ", x, " por ", y, " é:", multiplicacao(x, y))
            
            elif entrada == 4:
                print("Divisão")
                x = int(input("Digite um número: "))
                y = int(input("Digite outro número: "))
                #Função Monad
                monadDivisao = lambda func, x, y: func(x, y) if x != None and y != None else None

                print("O resultado da divisão é: ")
                print(monadDivisao(divisao, x, y))
            
            elif entrada == 5:
                print("Potenciação")
                x = int(input("Digite um número: "))
                #Função de Continuação
                continuacao = lambda resultado: print("O quadrado do número", x, "é:", resultado)

                quadrado(x, continuacao)  

            elif entrada == 6:
                print("Digite a seguir cinco números")
                num1 = int(input("Digite o primeiro número: "))
                num2 = int(input("Digite o segundo número: "))
                num3 = int(input("Digite o terceiro número: "))
                num4 = int(input("Digite o quarto número: "))
                num5 = int(input("Digite o quinto número: "))

                #Função de Alta Ordem utilizando Map
                numeros = [num1, num2, num3, num4, num5]
                triplo = list(map(lambda x: x * 3, numeros))
                print("Imprimindo em uma lista o triplo dos cinco números digitados: ")
                print(triplo)

            
            elif entrada == 7:
                #Função Closure
                print("Essa função utilizará uma closure. Você deve inserir um operador aritmético e posteriormente inserir dois números distintos.\n ")
                
                def Calculador(operador):
                    def calcular(x, y):
                        if operador == '+':
                            return x + y
                        elif operador == '-':
                            return x - y
                        elif operador == '*':
                            return x * y
                        elif operador == '/':
                            if y != 0:
                                return x / y
                            else:
                                return "Erro: Divisão por zero!"
                        else:
                            return "Erro: Operador inválido!"
                    
                    return calcular

                operador = input("Insira o operador matemático (+, -, *, /): ")

                calculando = Calculador(operador)

                num1 = float(input("\nInsira o primeiro número: "))
                num2 = float(input("\nInsira o segundo número: "))

                result = calculando(num1, num2)

                print("\nResultado da operação:", result)
                print("Essa operação foi feita utilizando uma closure.")
            
            #Função List Comprehension
            elif entrada ==8:
                print("Essa função irá criar duas listas, cada uma listando os números ímpares e pares até o número indicado.\n")

                numMax = int(input("Insira um número máximo: "))

                Par = [x for x in range(1, numMax + 1) if x % 2 == 0]
                Impar = [x for x in range(1, numMax + 1) if x % 2 != 0]

                print("\nNúmeros pares até", numMax, ":", Par)
                print("\nNúmeros ímpares até", numMax, ":", Impar)
                print("\nEssas listas foram criadas utilizando a função List Comprehension\n")

            elif entrada ==0:
                print("Saindo do programa.")
                break
            
            else:
                print("Digite uma opção válida")

        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")
