#!/usr/bin/env python
# coding: utf-8
# DESENVOLVIDO POR CAPUZ
# TWITTER: https://twitter.com/CapuzSec


import requests
import urllib.request
from bs4 import BeautifulSoup
import re

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# FUNCAO PARA PESQUISAR UNICO EMAIL

def pesquisaSimples():
 
	 
	email = input("Digite o email que desejada consultar: ")
	print('\n')

	payload = {
		'txtemail': '{}'.format(email),
		'btnSubmit': 'Violado?',
		}

	url = requests.post("https://whatismyipaddress.com/breach-check", data=payload)
	soup = BeautifulSoup(url.text, 'html.parser')

	# Pega texto que tem a resposta 
	r = soup.find_all(class_='breached-main-wrapper')
	r = str(r) 

	# Retira quebra de linha 
	email = email.rstrip('\n')

	if("Breached accounts for" in r):
		print("{} -> Senha já foi vazada, aconselho a trocar a senha o mais rapido possivel!\n".format(email))
	else:
		print("{} ->  A senha do email nunca foi vazada! \n".format(email))

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# FUNCAO PARA PESQUISAR LISTA EMAIL

def consultaLista():
 	
	arquivoEmail = input("Digite o arquivo com todos os emails (cada email em uma linha): ")
	print(' ')
	arquivo = open(arquivoEmail, 'r')
	texto = arquivo.readlines()


	for emailList in texto : 

		payload = {
			'txtemail': '{}'.format(emailList),
			'btnSubmit': 'Violado?',
			}

		url = requests.post("https://whatismyipaddress.com/breach-check", data=payload)
		soup = BeautifulSoup(url.text, 'html.parser')


		# Pega texto que tem a resposta 
		r = soup.find_all(class_='breached-main-wrapper')
		r = str(r) 

		# Retira quebra de linha 
		emailList = emailList.rstrip('\n')

		if("Breached accounts for" in r):
			print("{} -> Senha já foi vazada, aconselho a trocar a senha o mais rapido possivel!".format(emailList))
		else:
			print("{} ->  A senha do email nunca foi vazada!".format(emailList))

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




print(' ')
print('1 - Pesquisar um email')
print('2 - Pesquisar uma lista de email\n')
opcao = int(input('Digite o numero da opção desejada: '))


if opcao == 1:
	pesquisaSimples()

if opcao == 2:
	consultaLista()
