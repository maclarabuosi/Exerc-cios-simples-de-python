# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 09:15:17 2024

@author: clara.buosi
"""
temp = float(input("Digite uma temperatura em Celsius:"))

kelvin = temp + 273
fahrenheit = 1.8 * temp + 32

print(f"{temp:.1f}°C equivale a {fahrenheit:.1f}°F e {kelvin:.1f}°K")