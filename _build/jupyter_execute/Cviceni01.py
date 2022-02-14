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

# ## Podminkove cykly

# ### If ... else

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


# ### For ...

# In[6]:


for x in range(10):
    print(x)


# ### While...

# In[7]:


cislo = 0
while cislo < 10:
  print(cislo)
  cislo = cislo+1 # ekvivalenti zapis je take: cislo += 1


# break continue

# ## Funkce

# In[8]:


def objem_jehlanu(a,b,v):
  return 1/3*a*b*v

print("Objem jehlanu = ",objem_jehlanu(2,3,4))


# ## Vyjimky

# Pro odhaleni pripadnych chyb muzeme pouzit konstrukci `try - except`:

# In[9]:


try:
  print(neznama_promenna)
except: # pro pripad chyby
  print("Neco je spatne.")
else: # pokud se chyba neobjevi
  print("Vse je v poradku.") 


# ## Numericka knihovna numpy

# Pro importovani numericke knihovny `numpy` pouzijeme prikaz:

# In[10]:


import numpy as np


# #### Maticove operace

# Pole (vektor, matice) lze vytvaret pomoci funkce `array()`:

# In[11]:


# vektor
a = np.array([1, 2, 3])

# matice (pole)
A = np.array([[1,2,3],[4,5,6],[7,8,9]])


# <div class="alert alert-block alert-danger"><b>Pozor:</b> v poli <code>array</code> ma prvni prvek index <b>0</b>!</div>

# Rozmery pole zjisitme pomoci funkce `shape`:

# In[12]:


print(a.shape)
print(A.shape)


# Funkce `size` vrati pocet prvku v poli:

# In[13]:


print(a.size)
print(A.size)


# Pro vytvareni poli lze pouzivat nasledujici generatory:

# * Pomoci funkce `arange()` vytvorime pole s prvky od 0 do 10 a krokem 1:

# In[14]:


pole = np.arange(0,10,1)
print(pole)


# * Pomoci funkce `linspace()` vygenerujeme pole s prvky od 0 do 10, pricemz pocet prvku je 20:

# In[15]:


pole = np.linspace(0,10,20)
print(pole)


# * Prikazem `logspace()` vytvorime pole od 0 do 10 s poctem prvku 20 v logaritmickem meritku ($\log_{10}$):

# In[16]:


pole = np.logspace(0,10,20,base=10)
print(pole)


# * Pomoci funkce `zeros()` vytvorime nulovou matici 2x2:

# In[17]:


pole = np.zeros((2,2))
print(pole)


#  * Funkci `ones()` vytvorime jednotkovou matici 3x3:

# In[18]:


pole = np.ones((3,3))
print(pole)


# * Pomoci funkce `eye()` vytvorime matici 3x3 s jednickami na diagonale, ostatni hodnoty jsou nulove:

# In[19]:



pole = np.eye(3)
print(pole)


# * Pole nahodnych cisel v rozmezi 0 az 1 se vygeneruje pomoci funkce `np.random.rand()`:

# In[20]:


pole_nahodnych_cisel = np.random.rand(3,2)


# Pro pristup k prvkum pole `A` pouzivame syntaxi `[min:max]`

# In[21]:


prvni_radek = A[0,:]
print(prvni_radek)


# In[22]:


prvni_sloupec = A[:,0]
print(prvni_sloupec)


# Nasobeni matic a vektoru se provadi pomoci operatoru `dot`:

# In[23]:


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

# In[24]:


# maticove nasobeni
print(np.dot(C,C))

# nasobeni po prvcich
print(C*C)


# ### Funkce

# `numpy` obsahuje casto pouzivane funkce a konstanty (napr. `sqrt()`, `log()`, `sin()`, `abs()`, `e`, `pi`, ...):

# In[25]:


print(np.sqrt(5))
print(np.log(5))
print(np.sin(5))
print(np.abs(-3))
print(np.e)
print(np.pi)


# Soucet prvku v poli je dan funkci `sum()`:

# In[26]:


# soucet prvku v poli
soucet = np.sum(A)
print(soucet)


# Minimalni a maximalni hodnotu v poli urcime funkci `min()` a `max()`:

# In[27]:


# maximalni hodnota v poli
maximum = np.max(A)
print(maximum)

# minimalni hodnota v poli
minimum = np.min(A)
print(minimum)


# Funkce `average()` vraci prumernou hodnotu; `std()` je smerodatna odchylka a `var()` je rozptyl:

# In[28]:


# prumerna hodnota
prumer = np.average(A)
print(prumer)

# smerodatna odchylka
smerodatna_odchylka = np.std(A)
print(smerodatna_odchylka)

# rozptyl
rozptyl = np.var(A)
print(rozptyl)


# Index prvku v poli lze najit pomoci funkce `argwhere()`:

# In[29]:


index_hledaneho_prvku = np.argwhere(A == 3)
print(index_hledaneho_prvku)


# In[ ]:





# <div class="alert alert-block alert-info"><b>Tip: </b> Dalsi priklady a navody pro praci s knihovnou <code>numpy</code> lze nalez na <a href='https://numpy.org/'>https://numpy.org/</a>.</div>

# ## Visualizace dat

# Pro kresleni grafu vyuzijeme knihovnu `matplotlib.pyplot`:

# In[30]:


import matplotlib.pyplot as plt


# ### Graf jedne promenne

# Vygenerujeme $x$ a $y$ hodnoty pro funkci `sin()`:

# In[31]:


x = np.linspace(0,4*np.pi,100)
y = np.sin(x)


# Nejdrive je potreba vytvorit objekt obrazku pomoci `fig`. Vykresleni dat provedeme prikazem `plot()`:

# In[32]:


fig, ax = plt.subplots()
ax.plot(x,y)


# Přidáme popisky os pomoci `set_xlabel()`, `set_ylabel()` a nazev grafu pomoci `set_title()`:

# In[33]:


fig, ax = plt.subplots()
ax.plot(x,y)
ax.set_xlabel('x')
ax.set_ylabel('sin(x)')
ax.set_title('Graf funkce sin(x)')


# Pridame funkci `cos()`, nastavime barvu (`color`), styl (`linestyle`) a sirku (`linewidth`) linky. Pruhlednost se nastavuje parametrem `alpha`. Legendu zobrazime prikazem `legend()`:

# In[34]:


# funkce cos()
y1 = np.cos(x)

fig, ax = plt.subplots()
ax.plot(x,y)

# vykreslime funkci cos()
ax.plot(x,y1, color='red',linestyle='dashed',linewidth=2,label='cos(x)',alpha=0.5)


ax.set_xlabel('x')
ax.set_ylabel('sin(x), cos(x)')
ax.set_title('Grafy funkci sin(x) a cos(x)')
ax.legend()


# Na zaver obrazek ulozime prikazem `savefig()`:

# In[35]:


fig.savefig("obrazek.png", dpi=300)


# ### Visualizace zavislosti dvou promennych

# Mejme funkci $z(x,y)$, ktera zavisi na dvou promennych $z(x,y)=\exp(-\sqrt{x^2+y^2})\cos(2x)\sin(2y)$, a vykreslime jeji zavislost v 2D grafu.

# Vytvorime mrizku $x\times y$ pomoci funkce `meshgrid`:

# In[36]:


fig, ax = plt.subplots()
osa_x = np.linspace(-2, 2, 50)
osa_y = np.linspace(-2, 2, 50)
(x,y) = np.meshgrid(osa_x,osa_y)


# Spocitame hodnoty funkce $z(x,y)$:

# In[37]:


z = np.exp(-np.sqrt(x**2+y**2))*np.cos(2*x)*np.sin(2*y)


# 2D graf vykreslime pomoci funkce `pcolor()` s parametrem `shading='auto'`:

# In[38]:


fig, ax = plt.subplots()
osa_x = np.linspace(-2, 2, 50)
osa_y = np.linspace(-2, 2, 50)
(x,y) = np.meshgrid(osa_x,osa_y)
z = np.exp(-np.sqrt(x**2+y**2))*np.cos(2*x)*np.sin(2*y)
ax.pcolor(x,y,z,shading='auto')


# Kontury ziskame funkci `contour()`:

# In[39]:


fig, ax = plt.subplots()
osa_x = np.linspace(-2, 2, 50)
osa_y = np.linspace(-2, 2, 50)
(x,y) = np.meshgrid(osa_x,osa_y)
z = np.exp(-np.sqrt(x**2+y**2))*np.cos(2*x)*np.sin(2*y)
ax.contour(x,y,z)


# ### 3D visualizace

# Predpokladame, ze mame stejnou funkci $z(x,y)=\exp(-\sqrt{x^2+y^2})\cos(2x)\sin(2y)$, kterou chceme vykreslit v 3D grafu. Nejdrive vytvorime trojrozmernou osu:

# In[40]:


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')


# Vytvorime mrizku $x\times y$ pomoci funkce `meshgrid`:

# In[41]:


osa_x = np.linspace(-2, 2, 50)
osa_y = np.linspace(-2, 2, 50)
(x,y) = np.meshgrid(osa_x,osa_y)


# Spocitame hodnoty funkce $z(x,y)$:

# In[42]:


z = np.exp(-np.sqrt(x**2+y**2))*np.cos(2*x)*np.sin(2*y)


# 3D data vykreslime pomoci funkce `plot_surface()` a pridame popisky os:

# In[43]:


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

osa_x = np.linspace(-2, 2, 50)
osa_y = np.linspace(-2, 2, 50)
(x,y) = np.meshgrid(osa_x,osa_y)
z = np.exp(-np.sqrt(x**2+y**2))*np.cos(2*x)*np.sin(2*y)

ax.plot_surface(x, y, z)
ax.set(xlabel='x', ylabel='y', zlabel='z')


# <div class="alert alert-block alert-info"><b>Tip: </b> Dalsi priklady a navody pro praci s knihovnou <code>matplotlib</code> lze nalez na <a href='https://matplotlib.org/'>https://matplotlib.org/</a>.</div>
