#!/usr/bin/env python
# coding: utf-8

# # Základy práce v pythonu

# <div class="alert alert-block alert-info"><b>Tip: </b> Tento soubor je mozne stahnout ve forme <i>*.ipynb</i> nebo jako <i>*.pdf</i>.</div>

# <div class="alert alert-block alert-success"><b>On-line interaktivni verze: </b> Pro spusteni interaktivni verze kliknete ve vrchnim menu na raketu a zvolte <i>Binder</i>, ve kterem lze JN (Jupyter Notebook) upravovat. Volba <i>Live Code</i> umozni pouze spoustet radky s kodem.</div>

# ## Interaktivni Jupyter notebook

# Napiste `print('Hello, World!')` a stisknete `Shift` `+` `Enter` (nebo `Ctrl` `+` `Enter`)

# In[1]:


print('hello world')


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

"""V Pythonu nejsou žádné víceřádkové komentáře, které by
odpovídaly /* */ z C++ či Javy, nicméně často se místo nich
používají víceřádkové řetězce, které se jen nepřiřadí do
žádné proměnné a dále nepoužijí. Obvyklé je to zejména u
tzv. docstringů (viz dále)."""


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


# numpy, pyplot

# ***

# ### Funkce

# In[11]:


def objem_jehlanu(a,b,v):
  return 1/3*a*b*v

print("Objem jehlanu = ",objem_jehlanu(2,3,4))


# In[ ]:




