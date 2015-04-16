# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

alimento = open("alimentos.csv")   #abrir arquivos
usuario = open("usuario (1).csv")

alimentos = alimento.readlines() #ler alimentos
   
   
l = {}

for i in range(1,len(alimentos)):
    alimentos[i]=alimentos[i].strip()
    a = alimentos[i].split(',')
    l[a[0]] = a[1:4]
  
usuario1 = usuario.readlines() #ler usuarios

u = {}

for i in range(3,len(usuario1)):
    usuario1[i]=usuario1[i].strip()
    b = usuario1[i].split(',')
    u[b[0]] = b[1:len(b)]        
    print(u)
    
linha_user = usuario1[1]

lista_user = linha_user.split(",")

print(lista_user)
