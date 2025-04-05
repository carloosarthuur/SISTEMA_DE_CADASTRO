# importando funções que usaremos
import funções

# criando a lista de disciplinas
lista = []

a = 1
# criando variavel de escolha das opções do painel
escolha_painel = None

# criando um loop que contem o programa

while escolha_painel != 6: # o while continuara enquanto escolha_painel seja diferente de 6

    #  mostrando as opções ao usuario
    print(funções.txt_painel())
    escolha_painel = input("\nESCOLHA UMA DAS OPÇÕES: ")

    # contornando a proibição do operador in para listas
    if escolha_painel == "1" or escolha_painel == "2" or escolha_painel == "3" or escolha_painel == "4" or escolha_painel == "5" or escolha_painel == "6":

        escolha_painel = int(escolha_painel) # se escolha_painel estiver entre as opções ela sera transformada em inteiro
    else:
        print("\nDIGITE UM VALOR VÁLIDO")
        # se o usuario escolher uma opção que não conta nas opções, ele sera redirecionado para o inicio do laço
        continue

    # criando um match case que executa uma das funções do programa conforme o valor de escolha_painel
    match escolha_painel:
        case 1: # adicionar um dicionario a lista
            if len(lista) == 50: # numero maximo de itens na lista
                print("LISTA ESTÁ CHEIA")
                continue
            novo_dicionario = funções.criador_dicionario(lista) # criando e atribuindo um novo dicionario a variavel novo_dicionario
            if novo_dicionario != 0: # se a função criador_dicionario retornar um dicionario ele sera adicionado, se não o loop sera reiniciado
                lista.append(novo_dicionario) # adiciona novo dicionario

        case 2: # apaga um item da lista
            if len(lista) == 0: # se a lista estiver vazia o usuario sera redirecionado ao inicio
                print("\nVOCÊ AINDA NÃO ADICIONOU NADA NA LISTA PARA SER APAGADO")
                continue
            elif len(lista) == 1: # se a lista tiver apenas 1 item, esse item sera exculido
                print(f"{funções.formatação(lista[0])}\n-------------------------------------------------\n\nO ÚNICO LIVRO DA LISTA FOI APAGADO")
                lista.pop() # função que exclui o item 
                continue

            
            print("\ESCOLHA O LIVRO QUE DESEJA REMOVER\n")
            for i in range (len(lista)): # mostra todos os nomes dos livros dalista para o usuario escolher qual ele quer excluir
                nomes = list(map(lambda dicionario: dicionario['nome'], lista)) # insere todos os valores da chave 'nome' de todos os dicionarios da lista em uma outa lista
                print(f"{i + 1} - {nomes[i]}") # printa cada nome ao lado de um numero 

            numero = funções.transformacao_int(f"\nDigite a opção do livro deseja apagar: ") #o usuario escolhe o numero correspondente ao livro que ele quer apagar
            if numero <= len(lista):
                print(f"{funções.formatação(lista[numero - 1])}\n-------------------------------------------------\n\nFOI APAGADO")
                lista.pop(numero - 1) # livro é apagado

        case 3: # imprimir toda a lista
            n = 0 # variavel que sera usada para imprimir os dicionarios da lista e controla o laço while
            
            if len(lista) == 0:  # se a lista estiver vazia o usuario sera redirecionado ao inicio
                print("\nVOCÊ AINDA NÃO ADICIONOU NADA NA LISTA PARA PODER SER IMPRESSO")
                continue
            
            while n < len(lista): # enqaunto n for menor que o numero de componentes da lista o laço continuara
# retirei o ativador while desse laço pois vi que podia substituí-lo pelo n < len(lista)
                dicionario = lista[n] # adiciona o dicionario na psoição n da lista a variavel dicionario
                funções.formatação(dicionario)
                n += 1 # soma 1 ao valor de n
                # o laço se repete até todos os livros serem impressos 
            print("\n-------------------------------------------------")  # traço final adicionado apos o ultimo dicionario impresso          


        case 4: # imprimir um intervalo da lista
            if len(lista) == 0: # se a lista estiver vazia o usuario sera redirecionado ao inicio
                print("\nVOCÊ AINDA NÃO ADICIONOU NADA NA LISTA PARA PODER IMPRIMIR UM ITERVALO") 
                continue
            elif len(lista) == 1: # se a lista tiver somente um item, somente sera imprimido esse item
                funções.formatação(lista[0]) # printa o item na posição 0 
                print("\n-------------------------------------------------\n\nSUA LISTA SÓ TEM UM LIVRO") # traço final adicionado apos o dicionario impresso
                continue
            elif len(lista) == 2: # se a lista tiver somente 2 itens, serão impressos esses 2 valores
                funções.formatação(lista[0]) # printa o item na posição 0 
                funções.formatação(lista[1]) # printa o item na posição 1
                print("\n-------------------------------------------------\n\nSUA LISTA SÓ TEM DOIS LIVROS") # traço final adicionado apos o dicionario impresso
                continue
            
            ativador = True # variavel que controla o laço while
            while ativador == True:
                
                # escolha do primiero valor do intervalo
                print(f"\nDigite o primeiro valor, insira um número entre 1 e {len(lista)}: \n")
                for i in range (len(lista)): # imprime todos os nomes de livros da lista ao lado de um numero correspondente a sua posição
                    nomes = list(map(lambda dicionario: dicionario['nome'], lista)) # insere todos os valores da chave 'nome' de todos os dicionarios da lista em uma outa lista
                    print(f"{i + 1} - {nomes[i]}")
                # o usuario digita o primeiro valor e transforma o input do usuario em int se for possivel
                primeiro_valor = funções.transformacao_int("\nPRIMEIRO VALOR DO INTERVALO: ") # o usuario escolhe um numero entre os livros
                
                if primeiro_valor < 1 or primeiro_valor > len(lista): # se o primeiro_valor estiver fora do intervalo
                    print("\nVALOR FORA DO INTERVALO") # se o numero digitado pelo usuario estiver fora do intevalo de possibilidades ele voltara para o inicio do laço
                    continue 
                elif primeiro_valor == len(lista): # se o usuario escolheu o ultimo item da lista
                    funções.formatação(lista[-1]) # imprime o ultimo item da lista
                    print("\n-------------------------------------------------") # traço final adicionado apos o dicionario ser impresso
                elif primeiro_valor == (len(lista) - 1): # se o usuario escolher o penultimo item da lista, sera impresso o penultimo e o ultimo item da lista
                    funções.formatação(lista[-2])
                    funções.formatação(lista[-1])
                    print("\n-------------------------------------------------") # traço final adicionado apos o ultimo dicionario impresso

                
                else: 
                    # escolha segundo valor do intervalo
                    print(f"\nDigite o segundo valor, insira um número entre {primeiro_valor + 1} e {len(lista)}: \n") 
                    for i in range (primeiro_valor, len(lista)): # imprime todos os nomes de livros que aparecem depois do primeiro valor
                        nomes = list(map(lambda dicionario: dicionario['nome'], lista)) # insere todos os valores da chave 'nome' de todos os dicionarios da lista em uma outa lista
                        print(f"{i + 1} - {nomes[i]}")
                    # o usuario digita o segundo valor e transforma o input do usuario em int se for possivel
                    segundo_valor = funções.transformacao_int("\nSEGUNDO VALOR DO INTERVALO: ") # o usuario escolhe um numero entre os livros que apareceram
                    
                    if segundo_valor <= primeiro_valor or segundo_valor > len(lista): # se o numero digitado pelo usuario estiver fora do intevalo do primeiro valor + 1 até o len(lista) sera redirecionado ao inicio do laço
                        print("\nVALOR FORA DO INTERVALO") 
                        continue                            
                    
                    n = primeiro_valor # defini a variavel n como igaul ao primiero_valor (somente para não confundir)
                    for n in range (n - 1, segundo_valor): # primero valor - 1 determina o inicio do loop e segundo_valor determina o final do loop
                        funções.formatação(lista[n]) # printa a lista na posição n
                        # repete até imprimir todos os livros no intervalo
                    print("\n-------------------------------------------------") # traço final adicionado apos o ultimo dicionario impresso
                
                ativador = False # ao terminar o loop o laço sera encerrado

        case 5: #procurando um item específico
            if len(lista) == 0:
                print("\nVOCÊ AINDA NÃO ADICIONOU NADA NA LISTA PARA PODER PESQUISAR ALGO") # se a lista estiver vazia o usuario sera redirecionado ao inicio
                continue            

            ativador = True # ativa e desativa o laço while
            while ativador == True: # laço que executa a função de procura do programa
                print(funções.txt_busca())
                escolha = funções.transformacao_int("\nEscolha o que você quer pesquisar :") 
                
                if escolha == 1 or escolha == 2 or escolha == 3 or escolha == 4: #  só executa se escolha estiver em [1, 2, 3, 4]
                    match escolha: # dependedo do valor da variavel escolha sera atribuido um valor a variavel chave correspondente ao que se deseja procurar
                        case 1:
                            chave = "nome"                
                        case 2:
                            chave = "autor"
                        case 3: # caso especifico para data de lançamento
                            chave = "data de lançamento"
                            data_de_lançamento = funções.data_format() # o usuario insere a data de lançamento que deseja procurar

                        case 4: # formata o preço para ser pesquisado na lista de dicionarios
                            chave = "preço"  
                            preco = funções.transformacao_float_positivo(f"\nPesquisa:\n\n{chave} que procura: ") # o usuario insere o preço que deseja procurar
                            preco = str(f"{preco:.2f}")
                            preco = f"R${preco}"
                            print(preco)

                    chaves = list(map(lambda dicionario: dicionario[chave], lista)) # insere todos os valores da chave 'nome' de todos os dicionarios da lista em uma outa lista
                    if chave == "data de lançamento": # se a chave for igual a data de lançamento a pesquisa sera igual a data de lançamento
                        pesquisa = data_de_lançamento
                    elif chave == "preço": # se a chave for igual a data de lançamento a pesquisa sera igual ao preço
                        pesquisa = preco
                    else: # se a chave não for equivalente a data de lançamento ou ao preço é pedido um input do usuario
                        pesquisa = input(f"\nPesquisa\n\n{chave} que procura: ") # apos ser definido em qual chave será feita a procura, é peido o valor dessa chave

                    ativador_mensagem = True # controla o ativamento de uma mensagem
                    n = 0 # variavel que controla o loop e tbm controla qual dicionario sera impresso
                    
                    while n < len(chaves): # enquanto n for menor que o numero de itens da lista de valores da chave:
                        
                        if pesquisa == chaves[n]: # somente rodara se a pesquisa for igual ao valor da chave n na lista de valores de chave
                            funções.formatação(lista[n]) # printa o dicionario na posição n quando a pesquisa for igual ao valor da chave de mema posição n na lista de chaves
                            ativador_mensagem = False # se for impresso ao menos um item a mensagem não será ativada

                        n += 1 # soma 1 até o loop se encerrar
                        ativador = False # ativador é finalizado
                    
                    if ativador_mensagem == True: # se nenhum item for encontrado o ativador sera igual a True e essa mensagem sera impressa
                        print(funções.txt_não_encontrado())
                    else: # se não o traço final sera adicionado apos o ultimo dicionario impresso
                        print("\n-------------------------------------------------")


# se o usuario escolheu 6 o programa sera finalizado
print("\nFIM DO PROGRAMA\n")