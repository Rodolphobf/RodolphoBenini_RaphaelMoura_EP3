# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from FuncoesEP3 import *


alimento = open("alimentos.csv")   #abrir arquivos
usuario = open("usuario (1).csv")

alimentos = alimento.readlines() #ler alimentos
   
   
l = {}

for i in range(1,len(alimentos)):                 #criando os dicionarios de alimentos
    alimentos[i]=alimentos[i].strip()
    a = alimentos[i].split(',')
    l[a[0]] = a[1:4]
  
usuario1 = usuario.readlines() #ler usuarios

u = {}

for i in range(3,len(usuario1)):
    usuario1[i]=usuario1[i].strip()
    b = usuario1[i].split(',')
    u[b[0]] = b[1:len(b)]        
    
    
linha_user = usuario1[1]

lista_user = linha_user.split(",")

nome = lista_user[0]
idade = int(lista_user[1])
peso = float(lista_user[2])
sexo = str(lista_user[3])
sexo = sexo.lower()
altura = float(lista_user[4])
FF = lista_user[5]
print(lista_user[3])

if sexo == "M":
    massa_homem(peso,idade,altura)   
    if FF == "minimo":
        TMB = massa_homem*1.2   
    if FF == 'baixo':
        TMB = massa_homem*1.375
    if FF == 'medio' :
        TMB = massa_homem*1.55
    if FF == 'alto':
        TMB = massa_homem*1.725
    if FF == 'muito alto':
        TMB = massa_homem*1.9


if sexo == "F":
    massa_mulher(peso,idade,altura)
    if FF == "minimo":
        TMB = massa_mulher*1.2
    if FF == 'baixo':
        TMB = massa_mulher*1.375
    if FF == 'medio' :
        TMB = massa_mulher*1.55
    if FF == 'alto':
        TMB = massa_mulher*1.725
    if FF == 'muito alto':
        TMB = massa_mulher*1.9
        
print(TMB)

