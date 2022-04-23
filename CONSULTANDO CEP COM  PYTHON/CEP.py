#!/usr/bin/env python
# coding: utf-8

# In[8]:


import requests # IMPORTANDO BIBLIOTÉCA NECESSÁRIA PARA CONSUMIR UMA API UTILIZANDO O REQUEST


def main():
	print('CONSUNTADO CEP ATRAVÉS DE UMA API:\n')
	print()

	cep_input = input('Digite o CEP para a consulta:') # IMPUT DO CEP
    
#VALIDAÇÃO, CASO O NÚMERO INSERIDO  NO IMPUT ACIMA SEJA DIFERENTE DE 8, IRÁ RETORNAR UMA MENSAGEM DE ERRO:

	if len(cep_input) != 8:
		print('Quantidade de dígitos inválido!, por favor, validar!')
		exit()

	request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input)) # FAZENDO UMA REQUISIÇÃO NA API

	address_data = request.json()

	if 'erro' not in address_data:
		print("")
		print('O CEP PESQUISADO FOI ENCONTRADO! SEGUE DETALHES ABAIXO:')
		print("")
		print('CEP: {}'.format(address_data['cep']))
		print('Logradouro: {}'.format(address_data['logradouro']))
		print('Complemento: {}'.format(address_data['complemento']))
		print('Bairro: {}'.format(address_data['bairro']))
		print('Cidade: {}'.format(address_data['localidade']))
		print('Estado: {}'.format(address_data['uf']))
		
	else:
		print('{}: CEP inválido! Por favor, tente novamente.'.format(cep_input))

	print('---------------------------------')
	option = int(input('Deseja realizar uma nova consulta ?\n1. Sim\n2. Sair\n'))
	if option == 1:
		main()
	else:
		print('Saindo...')

if __name__ == '__main__':
	main()

