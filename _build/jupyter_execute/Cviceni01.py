#!/usr/bin/env python
# coding: utf-8

# # Základy práce v pythonu

# <div class="alert alert-block alert-info"><b>Tip: </b> Tento soubor je mozne stahnout ve forme <i>*.ipynb</i> nebo jako <i>*.pdf</i>.</div>

# <div class="alert alert-block alert-success"><b>On-line interaktivni verze: </b> Pro spusteni interaktivni verze kliknete ve vrchnim menu na raketu a zvolte <i>Binder</i>, ve kterem lze JN (Jupyter Notebook) upravovat. Volba <i>Live Code</i> umozni pouze spoustet radky s kodem.</div>

# ## Interaktivni Jupyter notebook

# Napiste `print('Hello, World!')` a stisknete `Shift` `+` `Enter` (nebo `Ctrl` `+` `Enter`)

# In[1]:


print('Hello, World')


# Pomoci klavesy `b` vlozite dalsi radek. 
# * Stisknete `b`.

# Odstraneni radku: vyberte radek a stisknete `d` `+` `d`

# Klavesou `a` vlozite novy radek nad prave vybrany. 
# 1. Stisknete `a`. 
# 2. Vyberte tento novy radek a stisknete `m`. Nyni lze do radku misto kodu zapisovat text.
# 3. Zadavani ukoncite stisknutim `Shift` `+` `Enter`.
# 4. Pokud chcete radek prevest na kod, stisknete `y`.
# 

# **Pro nápovědu stisknete `h`.**

# ## Python

# Jednoradkovy komentar se zadava za znak `#`, vice radku lze zakomentovat pomoci `"""` a `"""`

# In[2]:


# toto je komentar
"""
Komentar
na vice
radku...
"""
print("Hello, World!") 


# ### Jednoduche pocitani s promennymi

# Inicializace promennych `a`, `b` a zakladni aritmeticke operace a vypis vysledku:

# In[3]:


a=43
b=5.5

soucet=a+b
rozdil=a-b
soucin=a*b
podil=a/b
mocnina=a**b

# vypis
print('Soucet ',soucet)
print('Rozdil ',rozdil)
print('Soucin ',soucin)
print('Podil ',podil)
print('Mocnina ',mocnina)


# <div class="alert alert-block alert-warning"><b>Cviceni 01.01: </b> Vypoctete objem jehlanu o stranach 3 a 4 majiciho vysku 7. </div>

# In[4]:


a=3
b=4
v=7
S=a*b
V=1/3*S*v
print(V)


# List a range

# ***

# ### Podminkove cykly

# #### If ... else

# <div class="alert alert-block alert-danger"><b>Pozor:</b> vnitrni casti kodu je <b>nutne</b> odsadit, obvykle se pouzivaji <b>ctyri mezery</b>.</div>

# Za klicovymi slovy `if` a `else` musime psat `:`.

# In[5]:


cislo = 0
if cislo > 0:
    print(cislo, "je kladne.")
elif cislo <0:
    print(cislo, "je zaporne")
else:
    print("musi to byt nula")    
print("Tento text se vypise vzdy.")


# #### For ...

# In[6]:


for x in range(10):
    print(x)


# #### While...

# In[7]:


cislo = 0
while cislo < 10:
  print(cislo)
  cislo = cislo+1 # ekvivalenti zapis je take: cislo += 1


# break continue

# ***

# ### List (seznam)

# Prvky seznamu vkladame do hranatych zavorek.

# In[8]:


seznam=[0,1,2,3]
print(seznam[0])


# <div class="alert alert-block alert-danger"><b>Pozor:</b> v seznamu <code>list</code> ma prvni prvek index <b>0</b>!</div>

# #### Hledani v seznamech

# In[9]:


seznam=[0,1,2,3,"a","B"]
print(0 in seznam)


# Jak najit index hledneho prvku v seznamu:

# In[10]:


# jaky index v seznamu ma prvek "a"?
index_hledaneho_prvku = seznam.index("a")
print('Prvek "a" ma v seznamu index: ',index_hledaneho_prvku)


# ***

# ### Funkce

# In[11]:


def objem_jehlanu(a,b,v):
  return 1/3*a*b*v

print("Objem jehlanu = ",objem_jehlanu(2,3,4))


# ***

# ### Numericka knihovna numpy

# Pro importovani numericke knihovny `numpy` pouzijeme prikaz:

# In[12]:


import numpy as np


# #### Pole

# Pole (vektor, matice) lze vytvaret pomoci funkce `array`:

# In[13]:


# vektor
a = np.array([1, 2, 3])

# matice
matice = np.array([[1,2,3],[4,5,6],[7,8,9]])


# <div class="alert alert-block alert-danger"><b>Pozor:</b> v poli <code>array</code> ma prvni prvek index <b>0</b>!</div>

# Rozmery pole zjisitme pomoci funkce `shape`:

# In[14]:


print(a.shape)
print(matice.shape)


# Funkce `size` vrati pocet prvku v poli:

# In[15]:


print(a.size)
print(matice.size)


# Pro vytvareni poli lze pouzivat generatory `arange`,`linspace`,`logspace`,`ones`,`zeros`,`eye`,`random`:

# In[16]:


# vytvorime pole od 0 do 10 s krokem 1
pole = np.arange(0,10,1)
print(pole)


# In[17]:


# vytovrime pole od 0 do 10 s poctem prvku 20
pole = np.linspace(0,10,20)
print(pole)


# In[18]:


# vytovrime pole od 0 do 10 s poctem prvku 20 v logaritmickem meritku  (log se zakladem 10)
pole = np.logspace(0,10,20,base=10)
print(pole)


# In[19]:


# vytovrime matici 2x2 obsahujici same nuly
pole = np.zeros((2,2))
print(pole)


# In[20]:


# vytovrime matici 3x3 obsahujici same jednicky
pole = np.ones((3,3))
print(pole)


# In[21]:


# vytovrime matici 3x3 s jednickami na diagonale, ostatni hodnoty jsou nulove
pole = np.eye(3)
print(pole)


# Pro pristup k prvkum matice pouzivame syntaxi `[min:max]`

# In[22]:


matice = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matice)


# In[23]:


prvni_radek = matice[0,:]
print(prvni_radek)


# In[24]:


prvni_sloupec = matice[:,0]
print(prvni_sloupec)


# Nasobeni matic a vektoru se provadi pomoci operatoru `dot`:

# In[25]:


# matice 2x3
A = np.array([[1,2,3],[4,5,6]])
print(A)
print(A.shape)

# matice 3x2
B = np.array([[1,2],[3,4],[5,6]])
print(B)
print(B.shape)

# vysledek
C = np.dot(A,B)
print(C)


# <div class="alert alert-block alert-danger"><b>Pozor:</b> operace <b>C*C</b> nasobi matice po prvcich (neni to maticove nasobeni)</div>

# In[26]:


# maticove nasobeni
print(np.dot(C,C))

# nasobeni po prvcich
print(C*C)


# #### Funkce

# `numpy` obsahuje casto pouzivane funkce a konstanty (napr. `sqrt`, `log`, `sin`, `abs`, `e`, `pi`, ...):

# In[27]:


print(np.sqrt(5))
print(np.log(5))
print(np.sin(5))
print(np.abs(-3))
print(np.e)
print(np.pi)


# Zjistime soucet prvku (`sum`), maximum (`max`), minimum (`min`), prumernou hodnotou (`average`), smerodatnou odchylku (`std`) a rozptyl (`var`) u matice `A`:

# In[28]:


print(A)

soucet = np.sum(A)
print(soucet)

maximum = np.max(A)
print(maximum)

minimum = np.min(A)
print(minimum)

prumer = np.average(A)
print(prumer)

smerodatna_odchylka = np.std(A)
print(smerodatna_odchylka)

rozptyl = np.var(A)
print(rozptyl)


# Index prvku v matici lze najit pomoci funkce `argwhere`:

# In[29]:


index_hledaneho_prvku = np.argwhere(A == 3)
print(index_hledaneho_prvku)


# In[ ]:




