#!/usr/bin/env python
# coding: utf-8

# # Úkol 1

# 1. Napište funkci počítající faktoriál $n!$ z čísla $n\in \mathbb{N}$ (bez použití knihovny `math`). **(0.3 b)**
# 2. S vuyžitím této funkce napište další funkci počítající hodnotu Eulerova čísla $e=\sum_{n=0}^N \dfrac{1}{n!}$ pro $N\in \mathbb{N}$. Vypište výsledek pro $N=20$. **(0.3 b)**
# 3. Vykreslete graf funkce $f(x)=1/x$ pro $x\in \langle 0,1;5\rangle$ s počtem prvků 500 a popište osy. Sečtěte obsah plochy pod grafem mezi `x[92]` a `x[267]`(což přibližně odpovídá $x\in \langle 1;e\rangle$). **(0.4 b)**

# In[1]:


# sem vlozte vas kod


# In[2]:


import numpy as np


def f(n):
    faktorial = 1
    for i in range(1,n + 1,1):
        faktorial = faktorial*i
    return faktorial

def e(n):
    soucet = 0
    for i in range(n):
        soucet = soucet + 1/f(i)      
    return soucet

print(e(20))
print(np.e)


# In[3]:


import matplotlib.pyplot as plt
x = np.linspace(1e-1,5,500)
y = 1/x
fig, ax = plt.subplots()
ax.plot(x,y)


# In[4]:


np.sum(y[92:267])

