#!/usr/bin/env python
# coding: utf-8

# # Numerické metody lineární algebry

# Naimportujeme si knihovny potřebné pro následující příklady:

# In[1]:


import numpy as np


# ## Násobení matic

# <div class="alert alert-block alert-warning"><b>Cvičení 03.01: </b> Napište program pro násobení matic $\mathbb{A}$ and $\mathbb{B}$.</div>

# In[2]:


A = np.array([
[0, -3.7, 0, 0],
[1, 2, 3, 4.5],
[5, 4, 3, 2],
[1, 2, 3, 2],
[1, 3, 1, 5]
])

B = np.array([
[1, 1, 2, 2, 6],
[1, 2, 3, 4, 7],
[5, 4, 3, 2, 0],
[1, 2, 3, 2, -4]
])

pocet_radku = A.shape[0]
pocet_sloupcu = B.shape[1]
C = np.zeros((pocet_radku,pocet_sloupcu))

for i in range(pocet_radku):          #zvolim i-ty radek matice A
    for j in range(pocet_sloupcu):    # a j-ty sloupec matice B
        for k in range(A.shape[1]):   # projdu zaroven cely i-ty radek A a j-ty sloupec B
            C[i,j] = C[i,j] + A[i,k]*B[k,j] # poscitam vynasobene hodnoty a ulozim je do prvku C[i,j]           
print(C)

C_kontrola = np.dot(A,B)
print(C_kontrola)


# ## Přímé metody pro řešení lineárních rovnic $\mathbb{A}\mathbf{x}=\mathbf{b}$
# 1. Gaussova metoda
# 2. Gauss-Jordanova metoda
# 3. LU dekompozice

# ### Gaussova metoda

# * **Přímý běh:** matici $\mathbb{A}$ převedeme na trojúhleníkový tvar.
# * **Zpětný běh:** vypočítáme složky vektoru $\mathbf{x}$.

# #### Řešení soustav s trojúhelníkovou maticí

#  * Při převodou matice $\mathbb{A}$ na trojúhelníkový tvar hraje roli výběr hlavního prvku $a_{11}$ (pivotu) matice $\mathbb{A}$ (v důsledku omezené přesnosti čísel v počítači)
#   * Příklad na [pivoting](http://kfe.fjfi.cvut.cz/~vachal/edu/nme/cviceni/02_linalg/DOCS/priklad_pivoting.pdf)
#  * Následuje zpětný běh, ve kterém vypočítáme složky vektoru $\mathbf{x}$ ve směru klesajícího indexu $i$:
# $x_{i}=\dfrac{b_{i}-\sum_{j=i+1}^{n-1}a_{ij}x_{j}}{a_{ii}}$ kde $i= n-1, n-2,..., 0$

# <div class="alert alert-block alert-warning"><b>Cvičení 03.02: </b> Vyřeště soustavu lineárních  rovnic s horní trojúhlenikovou maticí.</div>

# In[3]:


#
# zpetny beh

A = np.array([[6,9,21],[0,21,-57],[0,0,78]]) # matice v hornim trojuhelnikovem tvaru
b = np.array([[141,-123,312]]).T # vektor b

x = np.zeros((3,1)) # neznamy vektor
n = x.size
for i in range(n-1,-1,-1):
    soucet = 0
    for j in range(i+1,n,1):
        soucet = soucet+x[j]*A[i,j]
    x[i] = (b[i]-soucet)/A[i,i]

print('Nami vypocitany vektor x = ' , x)

x_kontrola = np.linalg.solve(A,b)
print('Kontrola: x = ',x_kontrola)


# ### Gauss-Jordanova metoda

# * Matici $\mathbb{A}$ převedeme na tvar, kdy jsou na hlavní diagonále samé jedničky
# * Touto metodou lze získat i inverzní matici $\mathbb{A}^{-1}$
# * [Ukázka](http://kfe.fjfi.cvut.cz/~vachal/edu/nme/cviceni/02_linalg/DOCS/priklad_GaussJordan.pdf)

# ### LU dekompozice

# * Matici $\mathbb{A}$ lze rozepsat jako součin $\mathbb{A}=\mathbb{L}\mathbb{U}$ 
#  * $\mathbb{L}$ - matice v dolním trojúhelníkovém tvaru, na hlavní diagonále má jedničky
#  * $\mathbb{U}$ - matice v horním trojúhelníkovém tvaru, na hlavní diagonále má nenulové prvky
# * [Poznámky](http://kfe.fjfi.cvut.cz/~vachal/edu/nme/cviceni/02_linalg/DOCS/teorie_LU_dekompozice.pdf) k LU rozkladu
# * Ukážeme si implementaci [Croutova algoritmu](http://kfe.fjfi.cvut.cz/~limpouch/numet/02-linalg-CZ.pdf)

# <div class="alert alert-block alert-warning"><b>Cvičení 03.03: </b> Příklad na $\mathbb{L}\mathbb{U}$ dekompozici matice $\mathbb{A}$.</div>

# In[4]:


#
# matice A
A = np.array([
[4,3],
[6,3],
])


n = A.shape[0] # pocet radku matice A
U = np.zeros((n, n)) # nulova matice, ze ktere postupne vytvorime horni trojuhlenikovou matici
L = np.eye(n) # jednotkova matice, ze ktere postupne vytvorime dolni trojuhlenikovou matici
for k in range(n):
    U[k, k:] = A[k, k:] - np.dot(L[k,:k],U[:k,k:])
    L[(k+1):,k] = (A[(k+1):,k] - np.dot(L[(k+1):,:],U[:,k])) / U[k, k]

print('Matice L = ',L)
print('Matice U = ',U)


# ## Speciální typy matic

# ### Tridiagonální matice

# * Matice s kladnými prvky na hlavní a první pod- a naddiagonále. 
# * Ukážeme si implementaci [algoritmu](http://kfe.fjfi.cvut.cz/~limpouch/numet/02-linalg-CZ.pdf) řešení soustavy lineárních rovnic s tridiagonální maticí.

# <div class="alert alert-block alert-warning"><b>Cvičení 03.04: </b> Řešení soustavy lineárních rovnic s tridiagonální maticí.</div>

# In[5]:


#
A = np.array([
[0.0, 3.0, 8.0, 15.0],
[1.0, 14.0, 9.0, 0.3],
[0.8, 1.5, 7.0, 2.0],
[3.0, 6.0, 0.0, 11.0]
])

n = A.shape[0] # pocet radku vstupniho souboru

c = A[:,0] # pod diagonalou
a = A[:,1] # diagonala
b = A[:,2] # nad diagonalou
f = A[:,3] # prava strana

x   = np.zeros((n+1,1)) # vektor reseni

# pomocne vektory
rho = np.zeros((n+1,1)) 
mu  = np.zeros((n+1,1)) 

for i in range(n):# primy beh
    mu[i+1]  = -b[i] / ( c[i]*mu[i] + a[i] )
    rho[i+1] = ( f[i] - c[i]*rho[i] ) / ( c[i]*mu[i] + a[i] )


for i in range(n-1,-1,-1): # zpetny beh
    x[i] = mu[i+1]*x[i+1] + rho[i+1]
    
print(x)

