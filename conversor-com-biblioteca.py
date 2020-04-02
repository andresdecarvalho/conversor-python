from conversor import Conversao

opcao = 0
opcao2 = 0

while opcao != 5:
    print(""" 
            Bem Vindo ao programa de conversão\n
            Selecione a conversão desejada\n
            [1] Pés para metro
            [2] Polegada para centímetro
            [3] Jardas para metros
            [4] Milhas para kilometros
            [5] Sair do programa\n""")           
    opcao = int(input("Qual a sua opção? \nDigite: "))

    if opcao == 1:
        while opcao2 != 2:
            numero = float(input("Digite o valor dos Pés: "))
            print("")
            print(numero, "Pés é equivalente a", Conversao.pe2metro(numero), "metros \n \n")
            opcao2 = int(input("Deseja repetir este cálculo?: \n 1: Sim para repetir \n 2: Não para voltar ao menu\n Digite: "))
        opcao2 = 0 

    elif opcao == 2:
        while opcao2 != 2:
            numero = float(input("Digite o valor das Polegadas: "))
            print("")
            print(numero, "Polegadas é equivalente a", Conversao.pol2cent(numero), "centimetros \n \n")
            opcao2 = int(input("Deseja repetir este cálculo?: \n 1: Sim para repetir \n 2: Não para voltar ao menu\n Digite: "))
        opcao2 = 0   

    elif opcao == 3:
        while opcao2 != 2:
            numero = float(input("Digite o valor das Jardas: "))
            print("")
            print(numero, "Jardas é equivalente a", Conversao.jarda2metro(numero), "metros \n \n ")
            opcao2 = int(input("Deseja repetir este cálculo?: \n 1: Sim para repetir \n 2: Não para voltar ao menu\n Digite: "))
        opcao2 = 0   

    elif opcao == 4:
        while opcao2 != 2:
            numero = float(input("Digite o valor das Milhas: "))
            print("")
            print(numero, "Milhas é equivalente a", Conversao.milhas2km(numero), "quilometros \n \n")
            opcao2 = int(input("Deseja repetir este cálculo?: \n 1: Sim para repetir \n 2: Não para voltar ao menu\n Digite: "))
        opcao2 = 0    

    elif opcao == 5:
        print("Obrigado pro usar o programa de conversão!")
    else:
        print("Opção inválida, digite uma opção válida")
    print("=-=" * 15)

print("Fim do programa. Obrigado por usar!")