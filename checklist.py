#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os

def listaDados(objeto):
	for item in objeto:
		print("# %i - %s" %(objeto.index(item)+1, item ))

def executarItem(objeto, qnt):
    if qnt == 1:
        nome = os.path.basename(objeto[0])
        print("Executando %s" %nome)
        os.system("gedit "+os.path.abspath(itens[0]))
        print("%s foi instalado com sucesso" %nome)
    elif qnt > 1:
        print("Qual arquivo gostaria de executar")
        listaDados(objeto)
        opt = int(raw_input("Digite o número do arquivo: "))
        os.system("gedit " + os.path.abspath(itens[opt-1]))
    else:
        print("Não foram encontradas ocorrências de arquivos executáveis")

    #os.system('start /wait ' + caminho + '\\AdobeReader\\Adobe_Acrobat_Reader_MUI_DC.exe /sAll')


def nomeExtensao(objeto):
	for item in objeto:
		name = os.path.basename(item)
		#finfo = file(item)
		#file_name = finfo.name
		explode_name = name.split('.')
		only_name = ".".join(explode_name[:-1])
		extension = name[-3:]
		print(name+"\n"+
			only_name+"\n"+
			extension)
		print(ispdf(name))

def isexe(nome):
	#explode_name = nome.split('.')
	extension = nome[-3:]
	if extension == "exe":
		return True
	else:
		return False

def ispdf(nome):
	#explode_name = nome.split('.')
	extension = nome[-3:]
	if extension == "pdf":
		return True
	else:
		return False

def istxt(nome):
	#explode_name = nome.split('.')
	extension = nome[-3:]
	if extension == "txt":
		return True
	else:
		return False

caminho = "/home/bruno/Documentos/BTI/python"
caminhos = [os.path.join(caminho, nome) for nome in os.listdir(caminho)]
dirlist = [pasta for pasta in caminhos if os.path.isdir(pasta)]
#dirlist = [os.path.abspath(pasta) for pasta in caminhos if os.path.isdir(pasta)]
filelist = [arquivo for arquivo in dirlist if os.path.isfile(arquivo)]
#filelist2 = [arquivo for arquivo in os.path.abspath(dirlist) if os.path.isfile(arquivo)]
'''
caminhos = [os.path.join(caminho, nome) for nome in os.listdir(caminho)]
#caminhos = [os.path.abspath(nome) for nome in os.listdir(caminho)]
'''

for cont in range(0, len(dirlist)):
    print("pasta %i" %(cont+1))
    itens = [item for item in os.listdir(dirlist[cont]) if istxt(item)]
    executarItem(itens, len(itens))
