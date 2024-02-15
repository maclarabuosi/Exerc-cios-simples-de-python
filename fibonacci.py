# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 08:42:07 2024

@author: clara.buosi
"""

import math

def fibonacci(i:int) -> int :
    sqrt = math.sqrt(5)
    p1 = ((1 + sqrt)/2) ** i
    p2 = ((1 - sqrt)/2) ** i
    return(math.floor((p1 - p2) / sqrt))

def main():
    n = int(input("Digite um número para calcular a sequencia de Fibonacci: "))
    res = fibonacci(n)
    print(res)
    
main()