import json

def gravarLivros(livros,livro):
    arquivo = open(livros, 'w')
    livrosJson = json.dumps(livro, indent=4)
    arquivo.write(livrosJson)
    arquivo.close()


def carregarLivros(livros):
    arquivo = open(livros, 'r')
    livroJson = arquivo.read()
    arquivo.close()
    if livroJson:
        liv = json.loads(livroJson)
        return liv
    else:
        return {}


def verificar_e_gravar(biblioteca,isbn):
    if biblioteca.get(isbn):
        return "\nISBN já consta na biblioteca!"
    else:
        titulo = input('Título do livro: ')
        autor = input('Autor do livro: ')
        genero = input('Gênero do livro: ')
        try:
            compra = float(input('Preço de compra do livro: '))
            qt = int(input('Quantidade do livro: '))
            biblioteca[isbn] = {"titulo":titulo,
                                "autor": autor,
                                "genero":genero,
                                "compra":compra,
                                "qt": qt}
            return "\nLivro cadastrado!"
        except ValueError:
            print("\nValor fornecido é inválido, você deve digitar um número")
            
    return f"Voltando para o menu..."
    

def imprimir_biblioteca(biblioteca):
    biblioteca_ordem = dict(sorted(biblioteca.items()))
    for key, i in biblioteca_ordem.items():
        print(f"{key} - {i['titulo']} - {i['qt']}")
    
    return f"\nEsses são os livros presentes na biblioteca"


def alterar_dados_biblioteca(biblioteca,isbn):

    if biblioteca.get(isbn):
        entradas = ["0","1","2","3","4","5"]
        print('''
        [1] - Título
        [2] - Autor
        [3] - Gênero
        [4] - Preço de compra
        [5] - Quantidade disponível
        [0] - Cancelar
        ''')
        dado = input("Escolha uma das opções listadas: ")

        if dado == "1":
            print(f"Dado atual: {biblioteca[isbn]['titulo']}")
            novodado = input("Novo título: ")
            biblioteca[isbn]['titulo'] = novodado
            return "\nDados alterados com sucesso!"
        
        elif dado == "2":
            print(f"Dado atual: {biblioteca[isbn]['autor']}")
            novodado = input("Novo autor(a): ")
            biblioteca[isbn]['autor'] = novodado
            return "\nDados alterados com sucesso!"
        
        elif dado == "3":
            print(f"Dado atual: {biblioteca[isbn]['genero']}")
            novodado = input("Novo gênero: ")
            biblioteca[isbn]['genero'] = novodado
            return "\nDados alterados com sucesso!"
        
        elif dado == "4":
            print(f"Dado atual: {biblioteca[isbn]['compra']}")
            novodado = input("Novo valor: ")
            biblioteca[isbn]['compra'] = novodado 
            return "\nDados alterados com sucesso!"

        elif dado == "5":
            print(f"Dado atual: {biblioteca[isbn]['qt']}")
            novodado = input("Nova quantidade: ")
            biblioteca[isbn]['qt'] = novodado
            return "\nDados alterados com sucesso!"
        
        elif dado == "0":
            return "Voltando para o Menu!"
        elif dado not in entradas:
            print("Valor inválido!")
            return alterar_dados_biblioteca(biblioteca,isbn)
        

    else:
        return "\nISBN não consta na biblioteca!"
    

def excluir_livro(biblioteca,isbn):
    if biblioteca.get(isbn):
        del biblioteca[isbn]
        return '\nLivro excluido!'

    else:
        return "\nISBN não localizado na biblioteca!"
    

def pesquisarlivro(biblioteca,dado,titulo):
    if dado == "1":
        for a in titulo:
            for key, i in biblioteca.items():
                lista_palavras_titulo = i['titulo'].lower().split()
                if a in lista_palavras_titulo:
                    valor_venda = i['compra']+(i['compra']/100*80)
                    print(f'''
    ISBN: {key}
    Título: {i['titulo']}
    Autor(a): {i['autor']}
    Gênero: {i['genero']}
    Preço de compra: R${i['compra']}
    Preço de venda: R${valor_venda}
    Quantidade em estoque: {i['qt']}''')
            
        return print("\nEsses são os dados desse livro.")
    elif dado == "2":
        for key, i in biblioteca.items():
            lista_palavras_titulo = i['autor'].lower().split()
            if titulo in lista_palavras_titulo:
                valor_venda = i['compra']+(i['compra']/100*80)
                print(f'''
    ISBN: {key}
    Título: {i['titulo']}
    Autor(a): {i['autor']}
    Gênero: {i['genero']}
    Preço de compra: R${i['compra']}
    Preço de venda: R${valor_venda}
    Quantidade em estoque: {i['qt']}''')
            
        return print("\nEsses são os dados desse livro.")
    
    elif dado == "3":
        for key, i in biblioteca.items():
            lista_palavras_titulo = i['genero'].lower().split()
            if titulo in lista_palavras_titulo:
                valor_venda = i['compra']+(i['compra']/100*80)
                print(f'''
    ISBN: {key}
    Título: {i['titulo']}
    Autor(a): {i['autor']}
    Gênero: {i['genero']}
    Preço de compra: R${i['compra']}
    Preço de venda: R${valor_venda}
    Quantidade em estoque: {i['qt']}''')
            
        return print("\nEsses são os dados desse livro.")
    
    elif dado == "4":
        for key, i in biblioteca.items():
            if titulo == i['compra']:
                valor_venda = i['compra']+(i['compra']/100*80)
                print(f'''
    ISBN: {key}
    Título: {i['titulo']}
    Autor(a): {i['autor']}
    Gênero: {i['genero']}
    Preço de compra: R${i['compra']}
    Preço de venda: R${valor_venda}
    Quantidade em estoque: {i['qt']}''')
            
        return print("\nEsses são os dados desse livro.")
    
    elif dado == "5":
        for key, i in biblioteca.items():
            if titulo in str(i['qt']):
                valor_venda = i['compra']+(i['compra']/100*80)
                print(f'''
    ISBN: {key}
    Título: {i['titulo']}
    Autor(a): {i['autor']}
    Gênero: {i['genero']}
    Preço de compra: R${i['compra']}
    Preço de venda: R${valor_venda}
    Quantidade em estoque: {i['qt']}''')
            
        return print("\nEsses são os dados desse livro.")
    
    elif dado == "6":
        for key, i in biblioteca.items():
            if titulo == key:
                valor_venda = i['compra']+(i['compra']/100*80)
                print(f'''
    ISBN: {key}
    Título: {i['titulo']}
    Autor(a): {i['autor']}
    Gênero: {i['genero']}
    Preço de compra: R${i['compra']}
    Preço de venda: R${valor_venda}
    Quantidade em estoque: {i['qt']}''')
            
        return print("\nEsses são os dados desse livro.")
    

def relatorio(biblioteca):
    cont = 0
    for key, titulo in biblioteca.items():
        if titulo['qt'] == 0:
            print(f"{key} - {titulo['titulo']} - {titulo['qt']}")
            cont = cont+1
    if cont == 0:
        return print("\nNão há livros sem estoque na biblioteca.")
    else:
        return print("\nEsses são os livros sem estoque!")