#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 16:14:52 2018

@author: ricardo
"""

def q1(perg, tent=3, lemb='Escolha somente as opções'):
    while True:
        ok = input(perg)
        if ok in ('a', 'A', 'b', 'B', 'c', 'C', 'd', 'D'):
            return False
        if ok in('e', 'E'):
            return True
        tent -= 1
        if tent < 0:
            break
        print(lemb)
    
def q2(perg, tent=3, lemb='Escolha somente as opções'):
    while True:
        ok = input(perg)
        if ok in ('e', 'E', 'b', 'B', 'c', 'C', 'd', 'D'):
            return False
        if ok in('a', 'A'):
            return True
        tent -= 1
        if tent < 0:
            break
        print(lemb)
    
    
def lista():
    lista = ['A - Colombo', 'B - Lula', 'C - Vagabundo', 'D - Teco', 'E - Cabral']
    for cand in lista:
        print(cand)
        
def lista1(q2):
    lista = ['A - Chubaka', 'B - Ken', 'C - Bolsonaro', 'D - Seya', 'E - Cabral']
    for cand in lista:
        print(cand)
        
def continua(perg, lembrete='Apenas sim ou não'):
    while True:
        ok = input(perg)
        if ok in ('s'):
            return True
        if ok in ('n'):
            return False
        break
        print(lembrete)
    
    
print('Quem descobriu o Brasil: ?')
lista()

if q1('Escolha uma das opções: ') != True:
    print('Que pena, você errou')
else:
    if continua('Deseja continuar') != True:
        print('Fim de jogo')
    else:
        lista1('Qual desses participou de Star Wars?')
        if q2('Escolha uma das opções: ') != True:
            print('Você chegou atpé aqui, meus parabens')
        else:
            print('Você venceu o torneio')
        
    
    
    
    
    
    
    
    
    
    
    