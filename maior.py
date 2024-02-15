# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 09:08:58 2024

@author: clara.buosi
"""

num = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))

maior = int((num+num2)/2 + abs(num-num2)/2)

print(f"O maior número digitado é {maior}")