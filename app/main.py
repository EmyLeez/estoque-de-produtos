def estoque():
    print("Bem-vindo ao sistema de estoque\n")
    
    while True:
        print("Selecione um número de acordo com seu interesse:\n")
        print("1 - Cadastrar novo produto ")
        print("2 - Listar todos os produtos ")
        print("3 - Sair ")
        opcao1 = int(input("Digite o número: "))

        if opcao1 == 3:
            print("Obrigada por usar nosso sistema!")
            return 'Sistema encerrado'


print(estoque())


