from Modulo_Livros import*

livros = 'biblioteca.json'
biblioteca = carregarLivros(livros)

while True:
    entradas = ["0","1","2","3","4","5","6"]
    print('''
[1] - Cadastrar livro
[2] - Imprimir biblioteca de livros
[3] - Alterar informações de um livro
[4] - Excluir livro da biblioteca
[5] - Pesquisar livro no banco de dados
[6] - Verficar livros sem estoque
[0] - Sair
    ''')

    modulo = input("Escolha uma das opções listas: ")

    if modulo == "1":
        isbn = input('ISBN do livro: ')

        if isbn == "":
            print("Voltando para o menu...")
        else:
            print(verificar_e_gravar(biblioteca, isbn))
            gravarLivros(livros,biblioteca)

    
    elif modulo == "2":
        imprimir_biblioteca(biblioteca)

    elif modulo == "3":
        isbn = input("Qual o ISBN do livro que você deseja alterar? ")
        if isbn == "":
            print("Voltando para o menu...")
        else:
            print(alterar_dados_biblioteca(biblioteca,isbn))
            gravarLivros(livros,biblioteca)

    elif modulo == "4":
        isbn = input("Qual o ISBN do livro que você deseja excluir? ")
        if isbn == "":
            print("Voltando para o menu...")
        else:
            print(excluir_livro(biblioteca,isbn))
            gravarLivros(livros,biblioteca)

    elif modulo == "5":
        entradas = ["0","1","2","3","4","5","6"]
        print('''
    [1] - Título
    [2] - Autor
    [3] - Gênero
    [4] - Preço de compra
    [5] - Quantidade disponível
    [6] - ISBN
    [0] - Cancelar
        ''')
        dado = input("Escolha uma das opções listadas pesquisar: ")
        if dado == "":
            print("Voltando para o menu...")
        elif dado == "1":
            titulo = input("Qual o titulo do livro que você deseja pesquisar? ").lower().split()
            pesquisarlivro(biblioteca,dado,titulo)
            gravarLivros(livros,biblioteca)
        elif dado == "2":
            titulo = input("Qual o nome do autor do livro que você deseja pesquisar? ").lower()
            pesquisarlivro(biblioteca,dado,titulo)
            gravarLivros(livros,biblioteca)
        elif dado == "3":
            titulo = input("Qual o gênero do livro que você deseja pesquisar? ").lower()
            pesquisarlivro(biblioteca,dado,titulo)
            gravarLivros(livros,biblioteca)
        elif dado == "4":
            try:
                titulo = float(input("Qual o preço do livro que você deseja pesquisar? "))
                pesquisarlivro(biblioteca,dado,titulo)
                gravarLivros(livros,biblioteca)
            except ValueError:
                print("Valor inválido! Você precisa digitar um número.")
            
        elif dado == "5":
            titulo = input("Qual a quantidade do livro que você deseja pesquisar? ")
            pesquisarlivro(biblioteca,dado,titulo)
            gravarLivros(livros,biblioteca)
        elif dado == "6":
            titulo = input("Qual o ISBN do livro que você deseja pesquisar? ")
            pesquisarlivro(biblioteca,dado,titulo)
            gravarLivros(livros,biblioteca)
        elif dado == "0":
            print("Voltando para o Menu...")
        elif dado not in entradas:
            print("Valor inválido! Voltando para o Menu!")
        
            

    elif modulo == "6":
        relatorio(biblioteca)
    
    elif modulo == "0" or "sair" or "Sair":
        print("Programa finalizado!")
        break
    
    elif modulo not in entradas:
        print("Opção inválida!")
