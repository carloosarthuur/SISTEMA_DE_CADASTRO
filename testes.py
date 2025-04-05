# lista = [1,2,3,4,5,6,7,8]
# print(lista.index(8))
# n = 0
# for i in lista:
#     print(n)
#     n +=1
# if len(lista) == 0:
#     print("Você ainda não adicionou nada na lista continue")



# primeiro_termo = int(input((f"Digete o valor do prieiro termo, insira  um valor entre 1 e {len(lista)}: ")))
# if primeiro_termo < 1 or primeiro_termo > len(lista):
#     print("Valor fora do intervalo continue")
# segundo_termo = int(input((f"Digete o valor do segundo termo, insira um valor entre {primeiro_termo} e {len(lista)}: ")))
# if segundo_termo < primeiro_termo or segundo_termo > len(lista):
#     print("Valor fora do intervalo continue")



# for dicionario in range(primeiro_termo - 1, segundo_termo):
#     print(lista[dicionario])

            # # se o termo já estiver na lista o usuario voltara para o inicio do laço
            # n = 0
            # for valor in range(0, len(lista)):
            #     if novo_dicionario == lista[n]:
            #         print("\nEsse termo já existe na lista")
            #         n += 1
            #         continue



dico = {'eu' : 2, 'nos' : 3, 'eles' : 4}
chave = 'eu'
chaves = dico.keys()
print(type(chaves))
print(chaves)
print(dico.get(chave))
print(dico['eu'])
print(chaves[0], dico[0])

# ideia cortada por usar o in
# for index in range(primeiro_termo - 1, segundo_termo): # primero termo - 1 determina o inicio do range e segundo_termo determina o final do range
#     print(lista[index]) # sera printado o termo da lista que está na posissão do valor da variavel do for index 

            # ativador == True
            # n = 0
            # if len(lista) == 0:
            #     print("\nVocê ainda não adicionou nada na lista para poder fazer uma busca") # se a lista estiver vazia o usuario sera redirecionado ao inicio     
            #     continue
            # while ativador == True:
            #     print(funções.txt_busca())
            #     escolha_busca = input("\nescolha uma das opções que você deseja encontrar: ")
            #     if escolha_busca == "1" or escolha_busca == "2" or escolha_busca == "3" or escolha_busca == "4":
            #         escolha_busca = int(escolha_busca) # se escolha_painel estiver entre as opções ela sera transformada em inteiro
            #     else:
            #         print("\nDigite um valor valido")
            #         continue

            #    # if n < len(lista):