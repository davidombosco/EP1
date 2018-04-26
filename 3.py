# -*- coding: utf-8 -*-

import json
with open ("dados3.json", "r") as dadosabertos:
    dadosprontos=dadosabertos.read()
    estoque=json.loads(dadosprontos)

#####################################

while True:
    print('\nControle de Estoque:')
    print('\n0 = sair\n1 = adicionar item\n2 = remover item\n3 = alterar item\n4 = imprime estoque\n5 = alterar valor de um produto')
    escolha = int(input('Faça sua escolha: '))

    if escolha == 0:                         
        print('Até mais')                    # encerra o código  
        break

    elif escolha == 1:                                  # adiciona itens
        produto = input('Nome do produto: ')            
        if produto not in estoque:
            quantidade_inicial = int(input('Quantidade inicial: '))
            if quantidade_inicial < 0:
                print('A quantidade inicial não pode ser negativa.')
            else:
                
             # PARTE 3 - ADICIONA O VALOR DO PRODUTO   
            	valor_produto = float(input('Valor do produto: '))    
            	if valor_produto < 0:
                    print('O valor deve ser positivo')
            	else:
                    estoque[produto] = {"quantidade":quantidade_inicial,"valor":valor_produto} 
        else:
            print('Produto já cadastrado.')
        
    elif escolha == 2:                       # remover itens
        produto = input('Nome do produto: ')
        if produto in estoque:
            del(estoque[produto])
        else:
            print('Elemento não encontrado')
    
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
          
    elif escolha == 5:
        produto = input('Nome do produto: ')
        if produto in estoque:
            print('O atual valor é: {0}'.format(estoque[produto]['valor']))
            novo_valor = float(input('Digite o novo valor do produto: '))
            estoque[produto]['valor'] = novo_valor
            print('{0} agora custa: {1}'.format(produto,novo_valor))
        else:
            print('Produto não encontrado')

#################################################################################################
            
with open ("dados3.json","w") as importacao:
    estoque=json.dumps(estoque,sort_keys=True,indent=4)
    importacao.write(estoque)
