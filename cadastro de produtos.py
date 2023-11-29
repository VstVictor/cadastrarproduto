# Cadastre o Produto

#apresentação
print('\n\t\t\t\t -- Cadastre o Produto --\n')

# produto = {'descricao': '', 'preço':0.0}

produto = {
    'descrição': 'descrição do produto',
    'preço': 0.0,
    'quantidade':0,
    'disponível': False
}

# entrada

produto['descrição'] = input('qual o produto?:')
produto['preço'] = float(input('informe o preço do produto:'))
produto['quantidade'] = int(input('quantidade desse produto:'))
produto['disponível'] = input('o produto está disponível (sim/não)?')

#saída

print(f'descrição...........{produto["descrição"]}')
print(f'preço..............{produto["preço"]}')
print(f'quantidade..........{produto["quantidade"]}')
if produto['disponível'].lower()== 'sim':
    print('disponível')
else:
    print('produto indisponível')
preçototal = produto['preço'] * produto['quantidade']
print(f' Preço Total: R${preçototal}')