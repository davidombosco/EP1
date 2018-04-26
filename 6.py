# -*- coding: utf-8 -*-


from firebase import firebase
firebase = firebase.FirebaseApplication('https://ep1-crud.firebaseio.com/', None)

if firebase.get("estoque",None) is None:                
    estoque = {}
else:
    estoque= firebase.get("estoque",None)
##########################################################################################################

while True:                          #p1:criando um loop de opções
    print('\nControle de Estoque:')
    print('\n0 = sair e salvar alterações\n1 = adicionar item\n2 = remover item\n3 = variação de estoque\n4 = imprimir estoque\n5 = alterar valor de um produto\n6 = produtos com estoque negativo\n7 = valor em estoque')   #p1
    escolha = int(input('Faça sua escolha: '))

##########################################################################################################    
    
    if escolha == 0:                         
        print('Até mais')                    
        break                                

##########################################################################################################        
        
    elif escolha == 1:      
        loja = input('Qual sua loja: ')
        loja = loja.lower()
        if loja not in estoque:
            print('Loja não cadastrada')
            cadastrar = int(input('Deseja cadastrar a loja?\n1 = Sim\n2 = Não\n'))
            if cadastrar == 1:                     # quer cadastrar e adicionar itens
                produto = input('Nome do produto: ')
                produto = produto.lower()
                quantidade_inicial = int(input('Quantidade inicial: '))     
                if quantidade_inicial < 0:                                  
                    print('A quantidade inicial não pode ser negativa.')    
                else: 
             # PARTE 3 - ADICIONA O VALOR DO PRODUTO   
                     valor_produto = float(input('Valor do produto: R$'))           
                     if valor_produto < 0:                                        
                         print('O valor deve ser positivo')														
                     else:
                         estoque[loja]={produto:{"quantidade":quantidade_inicial,"valor":valor_produto}}			 
        			    
  
        else:                                       # loja in estoque
            produto = input('Nome do produto: ')  
            produto = produto.lower()
            if produto not in estoque[loja]:                     
                quantidade_inicial = int(input('Quantidade inicial: '))     
                if quantidade_inicial < 0:                                  
                    print('A quantidade inicial não pode ser negativa.')    
                else: 
                    valor_produto = float(input('Valor do produto: R$'))           
                    if valor_produto < 0:                                        
                        print('O valor deve ser positivo')														
                    else:																														
                        estoque[loja][produto] = {"quantidade":quantidade_inicial,"valor":valor_produto}			 
            else:																						
                print('Produto já cadastrado.')									
       
  
##########################################################################################################
  
    elif escolha == 2:                       # remover itens        
        loja = input('De qual loja deseja remover: ')
        loja = loja.lower()
        if loja not in estoque:
            print('Loja não cadastrada')
        else:
            produto = input('Nome do produto: ')	
            produto = produto.lower()
            if produto in estoque[loja]:																			
                del(estoque[loja][produto])
                print (" O produto '{0}' foi removido do estoque da loja {1} com sucesso.".format(produto,loja))																		
            else:																												
                print('Elemento não encontrado')												
   
##########################################################################################################

    elif escolha == 3:                      # alterar item
                                            # alterar valores dos
        loja = input('De qual loja deseja alterar estoque? ')
        loja = loja.lower()
        produto = input('Nome do produto: ')
        produto = produto.lower()
        if loja not in estoque:
          	print('Loja não cadastrada')
        else:
            if produto in estoque[loja]:
                alteracao = int(input('Quantidade que irá variar: '))
                estoque[loja][produto]['quantidade'] = (estoque[loja][produto]['quantidade'] + alteracao)
                print('Novo estoque de {0} na {1}:{2}'.format(produto,loja,estoque[loja][produto]["quantidade"]))
            else:
                print('Elemento não encontrado')
        
##########################################################################################################        
        
    elif escolha == 4:                      # imprime estoque
        loja = input("Deseja imprimir o estoque de qual loja? (digite 'todas' para uma análise geral): \n")
        loja = loja.lower()
        if loja == 'todas':
            for loja in estoque:
              print('Estoque {0}:'.format(loja))
              for produto in estoque[loja]:
                    print("{0}:{1}".format(produto,estoque[loja][produto]['quantidade']))
        elif loja in estoque:
            print('Estoque da loja {0}:'.format(loja))
            for produto in estoque[loja]:
                print("{0}: {1}".format(produto,estoque[loja][produto]['quantidade']))        
        else:
            print('Loja não cadastrada')   
            
##########################################################################################################          
    
   # parte 3 - alterar o valor de um produto
    elif escolha == 5:
        loja = input('Qual a loja que deve ter o valor de um item alterado? ')
        loja = loja.lower()
        if loja not in estoque:
            print('Loja não cadastrada')
        else:    
            produto = input('Nome do produto: ')
            produto = produto.lower()
            if produto in estoque[loja]:
                print('O atual valor é: R${0:.2f}'.format(estoque[loja][produto]['valor']))
                novo_valor = float(input('Digite o novo valor do produto: R$'))
                estoque[loja][produto]['valor'] = novo_valor
                print('{0} agora na {1} custa: R${2:.2f}'.format(produto,loja,novo_valor))
            else:
                print('Produto não encontrado')
            
##########################################################################################################            
      
    # parte 4 - produtos com estoque negativo e valor do estoque
    elif escolha == 6:
        for loja in estoque:
            for i in estoque[loja]:
                produtos_negativos = {}
                if estoque[loja][i]['quantidade'] < 0:
                    quantidade_negativa=estoque[loja][i]["quantidade"]
                    produtos_negativos[i]= quantidade_negativa
                    print('Os produtos com quantidade em estoque negativa da loja {0} são:'.format(loja))
                    for produto in produtos_negativos:
                            print('{0}:{1}'.format(produto,produtos_negativos[produto]))
                    
##########################################################################################################          
      
    elif escolha == 7:
        for loja in estoque:	  
            for i in estoque[loja]:
                lista_valores = []
                lista_valores.append(estoque[loja][i]['quantidade'] * estoque[loja][i]['valor'])
            valor_monetario = sum(lista_valores)
            print('O valor em estoque da loja {0}: R${1:.2f}'.format(loja,valor_monetario))
            
##############################################################################################################

result = firebase.patch('https://ep1-crud.firebaseio.com/estoque', estoque)