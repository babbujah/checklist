#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os

def listaDados(objeto):
	for item in objeto:
		print(item)

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


caminho = "/home/bruno/Documentos/BTI/python"
print(caminho)

print("caminhos")
caminhos = [os.path.join(caminho, nome) for nome in os.listdir(caminho)]
#caminhos = [os.path.abspath(nome) for nome in os.listdir(caminho)]
listaDados(caminhos)
print("\n")

print("pastas")
dirlist = [pasta for pasta in caminhos if os.path.isdir(pasta)]
listaDados(dirlist)
print("\n")

print("arquivos")
filelist = [arquivo for arquivo in caminhos if os.path.isfile(arquivo)]
listaDados(filelist)
print("\n")

nomeExtensao(filelist)
