# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

alimento = open("alimentos.csv")   #abrir arquivos
usuario = open("usuario (1).csv")
usuario1 = usuario.readlines() #ler usuarios

alimentos = alimento.readlines() #ler alimentos
   
   
l = {}

for i in range(1,len(alimentos)):
    alimentos[i]=alimentos[i].strip()
    a = alimentos[i].split(',')
    l[a[0]] = a[1:4]
    print(l)      
    