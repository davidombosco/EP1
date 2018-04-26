# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 15:31:48 2018
@author: david
"""
import json
with open ("dados2.json", "r") as dadosabertos:
    dadosprontos=dadosabertos.read()
    estoque=json.loads(dadosprontos)


#####################################

while True:
    print('\nControle de Estoque:')
    print('\n0 = sair\n1 = adicionar item\n2 = remover item\n3 = alterar item\n4 = imprime estoque')
    escolha = int(input('Faça sua escolha: '))

    if escolha == 0:                         
        print('Até mais')                    # encerra o código  
        break

    elif escolha == 1:                                  # adiciona itens
        produto = input('Nome do produto: ')
        #parte 3 - adicionar valor
        if produto not in estoque:
            quantidade_inicial = int(input('Quantidade inicial: '))
            valor_produto = float(input('Valor do produto: '))
            if quantidade_inicial < 0:
                print('A quantidade inicial não pode ser negativa.')
            else:
                estoque[produto] = {"quantidade":quantidade_inicial}   
        else:
            print('Produto já cadastrado.')
        
    elif escolha == 2:                       # remover itens
        produto = input('Nome do produto: ')
        if produto in estoque:
            del(estoque[produto])
        else:
            print('Elemento não encontrado')
    
    elif escolha == 3:                      # alterar item
        produto = input('Nome do produto: ')
        if produto in estoque:
            alteracao = int(input('Quantidade: '))
            estoque[produto]["quantidade"] = (estoque[produto]["quantidade"] + alteracao)
            print('Novo estoque de {0}: {1}'.format(produto,estoque[produto]["quantidade"]))
        else:
            print('Elemento não encontrado')
        
    elif escolha == 4:                      # imprime estoque
        for produto in estoque:
          for quantidade in estoque[produto]:
            print("{0}: {1}".format(produto,estoque[produto][quantidade]))
            
################################################################################
            
with open ("dados2.json","w") as importacao:
    estoque=json.dumps(estoque,sort_keys=True,indent=4)
    importacao.write(estoque)