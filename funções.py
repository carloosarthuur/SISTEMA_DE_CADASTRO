# definindo função que contem uma docstring com o texto do painel inicial
def txt_painel():
    
    txt = '''
           PAINEL

1 - Adicionar um livro à lista
2 - Remover um livro
3 - Imprimir toda a lista
4 - Imprimir um intervalo na lista de livros
5 - Procurar um valor específico
6 - Sair'''
    
    return txt
# definindo função que contem uma docstring com o texto do painel de busca do caso 5
def txt_busca():
    txt = """1 - Buscar pelo nome do livro
2 - Buscar pelo autor
3 - Buscar pela data de lançamento
4 - Buscar pelo preço"""
    return txt 
# definindo função que contem uma docstring con o texto de nenhum livro com esse valor encontrado
def txt_não_encontrado():
    txt = """
-------------------------------------------------

Nenhum item encontrado na lista de livros
                              
-------------------------------------------------"""
    return txt

# definindo função para inserir dia ou mes ou ano 
def data(numero_de_digitos, txt, txt_error, maximo):
    contador = 0 # contador que controla o laço
    while contador != numero_de_digitos: # o numero de digitos equivale a quantidade de algarismos que tera no numero
        data = transformacao_int(txt) # faz o usuario digitar um numero 

        str_data = str(data) # transforma esse numero em uma string
        if len(str_data) <= contador or not (data < 1 or data > maximo): # conta as caracterias da string e
# compara com a variavel de entrada contador que determina quantos digitos o valor deve ter no maximo e verifica se o valor está dentro do limite
            contador = numero_de_digitos # se o if for satisfeito contador é igualado ao numero de digitos e se finaliza o loop
        elif data < 1 or data > maximo: # se o valor estiver estiver fora do intervalo definido na entrada da função a msg de erro é imprimida
            print(txt_error)
    return data

# definindo função que gera uma data já formatada
def data_format():
    ativador = True # controla o laço
    while ativador == True: 
        dia = data(2,"\nDia: ", "\nDigite um número entre 1 e 31", 31)
        mes = data(2,"\nMês: ", "\nDigite um número entre 1 e 12", 12)
        ano = data(4,"\nAno: ", "\nDigite um número menor que 2024", 2024)
        
        # Tratamento de erros para datas invalidas
        if mes == 2 and dia > 28 and (ano % 4) != 0: # fevereiro com dia > 28 sem ser ano bissexto 
            print("\nDATA INVÁLIDA")
            continue
        elif mes == 2 and dia > 29 and (ano % 4) == 0: # fevereiro com dia > 29 para ano bissexto
            print("\nDATA INVÁLIDA")
            continue
        elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30: # meses com até 30 dias para dia = 31
            print("\nDATA INVÁLIDA")
            continue
        ativador = False
    data_de_lançamento = (f"{dia:02}/{mes:02}/{ano:04}") # data formatada de forma padronizada 00/00/0000
    return data_de_lançamento

# definindo a funçõa para a criação de dicionarios
def criador_dicionario(lista):
    # atribuindo una variavel a cada valor de usa chave do dicionario
    n = 0
   
    nome = '' # variavel de controle do loop while
    copia = True # variavel de controle do loop while
    nomes = list(map(lambda dicionario: dicionario['nome'], lista)) # insere todos os valores da chave 'nome' de todos os dicionarios da lista em uma outa lista
    while nome == '' or copia == True: # confirma se o nome é diferente de vazio ou se o nome já consta na lista de livros
        nome = input("\nNome do livro: ")
        if nome == '': # verifica se o nome é vazio
            print("\nDIGITE UM NOME NÃO VAZIO")
        else:
            for i in range(len(nomes)): # verifica se o nome inserido já está na lista de livros
                if nome == nomes[i]: # se sim, a função retorna 0
                    print("\nJÁ EXISTE UM LIVRO COM ESSE NOME:")
                    formatação(lista[i])
                    print("\n-------------------------------------------------\n")
                    return 0 # finaliza a função e retorna 0, alem de printar o livro com o msm nome
            copia = False

    autor_do_livro = input("\nAutor: ") # autor do livro

    print("\nDigite a data de lançamento: ")
    data_de_lançamento = data_format() # executa a função para o usuario inserir a data de lançamento

    preco = (transformacao_float_positivo("\nPreço: ")) # executa a função que retorna um float pósitivo
    preco = str(f"{preco:.2f}") # coloca 2 zeros apos a o . ex: 12 -> 12.00 ; 1.5 = 1.50 ; 1.234 -> 1.23
    preco = f"R${preco}" # coloca R$ antes do preço
    
    # inserindo as variaveis correspondentes aos valores em cada uma de suas chaves
    dicionario = {"nome"  : nome, "autor" : autor_do_livro, "data de lançamento" : data_de_lançamento,"preço" : preco}

    return dicionario # retornando o dicionario

# definindo uma função que transforma um input de string para inteiro
def transformacao_int(txt):
    numero = None
    while type(numero) != int:
        numero = input(txt)
        if numero.isnumeric() == True:
            numero = int(numero)
        else:
            print("\nDigite um número válido")
    # quando o laço se encerrar a função retornara escolha como inteiro
    return numero
# definindo função que retorna um float positivo   
def transformacao_float_positivo(txt):
    numero = None
    while type(numero) != float:
        numero = input(txt)
        try:
            numero = float(numero)
            if numero < 0.00:
                print("\nDigite um valor maior ou igual a 0.00")
                numero = None
        except ValueError:
            print("\nDigite um valor válido\n")
    return numero

# definindo função que formata um dicionario para ser impresso de forma bonita
def formatação(dicionario):
    valores = list(dicionario.values())
    chaves = list(dicionario.keys())
    n = 0
    print("\n-------------------------------------------------\n")
    while n <= 3:
        print(f"{chaves[n]} : {valores[n]}")
        n += 1

    return 0
