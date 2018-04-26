# -*- coding: utf-8 -*-

import json
with open ("dados4.json", "r") as dadosabertos:
    dadosprontos=dadosabertos.read()
    estoque=json.loads(dadosprontos)


#####################################

while True:                          #p1:criando um loop de opções
    print('\nControle de Estoque:')
    print('\n0 = sair\n1 = adicionar item\n2 = remover item\n3 = alterar item\n4 = imprime estoque\n5 = alterar valor de um produto\n6 = produtos com estoque negativo\n7 = valor em estoque')   #p1
    escolha = int(input('Faça sua escolha: ')) #p1

    if escolha == 0:                         #p1
        print('Até mais')                    # encerra o código  #p1  
        break                                #p1

    elif escolha == 1:                                  # adiciona itens #p1
        produto = input('Nome do produto: ')            #p1
        if produto not in estoque:                      #p1
            quantidade_inicial = int(input('Quantidade inicial: '))     #p1
            if quantidade_inicial < 0:                                  #p1
                print('A quantidade inicial não pode ser negativa.')    #p1
            else: 
             # PARTE 3 - ADICIONA O VALOR DO PRODUTO   
            	valor_produto = float(input('Valor do produto: '))           #p3
            	if valor_produto < 0:                                        #p3
            			print('O valor deve ser positivo')														#p3
            	else:																														#p3
              		estoque[produto] = {"quantidade":quantidade_inicial,"valor":valor_produto}			#p3 
        else:																						#p1
            print('Produto já cadastrado.')							#p1
        
    elif escolha == 2:                       # remover itens        #p1
        produto = input('Nome do produto: ')												#p1
        if produto in estoque:																			#p1
            del(estoque[produto])																		#p1
        else:																												#p1
            print('Elemento não encontrado')												#p1
    
    elif escolha == 3:                      # alterar item
                                            # alterar valores dos
        produto = input('Nome do produto: ')
        if produto in estoque:
            alteracao = int(input('Quantidade: '))
            estoque[produto]["quantidade"] = (estoque[produto]["quantidade"] + alteracao)
            print('Novo estoque de {0}: {1}'.format(produto,estoque[produto]["quantidade"]))
        else:
            print('Elemento não encontrado')
        
    elif escolha == 4:                      # imprime estoque
        for produto in estoque:
          print("{0}: {1}".format(produto,estoque[produto]["quantidade"]))
          
    
   # parte 3 - alterar o valor de um produto
    elif escolha == 5:
        produto = input('Nome do produto: ')
        if produto in estoque:
            print('O atual valor é: {0}'.format(estoque[produto]['valor']))
            novo_valor = float(input('Digite o novo valor do produto: '))
            estoque[produto]['valor'] = novo_valor
            print('{0} agora custa: {1}'.format(produto,novo_valor))
        else:
        		print('Produto não encontrado')
      
    # parte 4 - produtos com estoque negativo e valor do estoque
    elif escolha == 6:
        produtos_negativos = {}
        for i in estoque:
            if estoque[i]['quantidade'] < 0:
                quantidade_negativa=estoque[i]["quantidade"]
                produtos_negativos[i]= {"quantidade": quantidade_negativa}
        print('Os produtos com quantidade em estoque negativa são:')
        for n in produtos_negativos:
            print('{0}:{1}'.format(n,produtos_negativos[n]['quantidade']))
      
    elif escolha == 7:
        lista_valores = []
        for i in estoque:
            lista_valores.append(estoque[i]['quantidade'] * estoque[i]['valor'])
        valor_monetario = sum(lista_valores)
        print('O valor em estoque: {0}'.format(valor_monetario))
        
##########################################################################################
        
with open ("dados4.json","w") as importacao:
    estoque=json.dumps(estoque,sort_keys=True,indent=4)
    importacao.write(estoque)