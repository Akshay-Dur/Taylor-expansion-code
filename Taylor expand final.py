# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 19:18:46 2023

@author: Akshay
"""

import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
x=sym.Symbol('x')
#f=sym.diff(x**2) #Derivative
#print(f.subs(x, 1)) #Evaluate function f at x=1
'''The imaginary number is written as sym.I'''
f=sym.exp(sym.I*x) #Function to Taylor expand
def taylor_exp(f, x, about, order): #Taylor expanding function f with respect to the variable x, around "about" 
    for i in range(order+1):
        if i==0:
            taylor_exp=f.subs(x, about)
            deriv=f
        else:
            deriv=sym.diff(deriv, x)
            taylor_exp+=deriv.subs(x, about)*(x-about)**i/sym.factorial(i)
    return taylor_exp
#taylor_exp(f, x, 0, 7).subs(x, 2.9) #Example: evaluate Taylor expanstion at x=2.9
print(taylor_exp(f, x, 0, 7))