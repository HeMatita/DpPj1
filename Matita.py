# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 16:02:17 2017

@author: mathe
"""
#Imports
import time,sys,os
import turtle as tt

#pequeno ajuste visual para quando rodar o programa diretamente
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

clear = lambda: os.system('cls')


#inicio das instruções
print_slow("As instruções para formar a figura são as seguintes:\n utilize F para seguir em linha reta e desenhar\n f para seguir em linha reta mas sem desenhar\n + para virar a esquerda com angulação de 90°\n - para virar a direita com angulação de 90°   ")
desenhar=str(input("\nDigite os comandos\n->"))
time.sleep(0.1)
clear()
numero=int(input("Quantas repetições?"))
time.sleep(0.1)
clear()

desenhar=desenhar.split(" ")
tt.speed('fast')

#For que define o desenho
for i in desenhar:
    if i=="F":
        tt.forward(5)
    if i=="f":
        tt.penup()
        tt.forward(5)
        tt.pendown()
    if i == '+':
        tt.left(90)
    if i == '-':
        tt.right(90)
exitonclick()
