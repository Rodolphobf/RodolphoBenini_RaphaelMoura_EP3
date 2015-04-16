# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from Funcoes_EP3 import *


alimento = open("alimentos.csv")
usuario = open("usuario (1).csv")

alimentos = []   #lista quebrada
alimento.r   eadlines() #ler alimentos
alimentos = alimento.split(",")

usuarioslista = []  #lista quebrada
usuario.readlines() #ler usuarios
usuarioslista = usuario.split(",") 

nome = input("Qual o seu nome?/n")
sexo = input("Qual seu sexo/n")
idade = input("Qual a sua idade/n")
peso = input("Qual o seu peso")
altura = input("Qual a sua altura?")
AF = input("Classifique sua atividade fisica semanal de 1 a 5")

if sexo == "homem" or 'Homem':
    tmb = massa_homem(peso,idade,altura)
    
if sexo == "mulher" or "Mulher":
    tmb = massa_mulher(peso,idade,altura)
gviuv
if AF == 1:
    caloria1=tmb*1.2
    
if AF == 2:
    caloria1=tmb*1.375

if AF == 3:
    caloria1=tmb*1.55viv

if AF == 4:
    caloria1=tmb*1.725

if AF == 5:
    caloria1=tmb*1.9
    
    