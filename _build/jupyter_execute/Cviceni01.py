#!/usr/bin/env python
# coding: utf-8

# # Jupyter notebook a základy Pythonu

# <div class="alert alert-block alert-info"><b>Tip: </b> Tento soubor je možné stáhnout kliknutím na <i class="fa fa-download" aria-hidden="true"></i>, a to ve formě <code>*.ipynb</code> pro pozdější off-line editaci v prostředí Anaconda.</div>

# <div class="alert alert-block alert-success"><b>On-line interaktivní verze: </b> Pro spuštení interaktivní verze tohoto <i>Jupyter notebook</i> klikněte ve vrchním menu na <i class="fa fa-rocket" aria-hidden="true"></i> a zvolte <i>Binder</i>, ve kterém lze <i>Jupyter notebook</i> upravovat a následně uložit na disk. Volba <i>Live Code</i> umožní editovat a spouštět řádky s kódem.</div>

# ## Interaktivní Jupyter notebook

# Napište `print('Hello, World!')` a stiskněte `Shift` `+` `Enter` (nebo `Ctrl` `+` `Enter`)

# In[1]:


print('Hello, World')


# Pomocí klávesy `b` vložíte další řádek do JP.
# * Stiskněte `b`.

# Odstranění řádku: vyberte řádek v JP a stiskněte `d` `+` `d`

# Klávesou `a` vložíte nový řádek nad právě vybraný.
# 1. Stiskněte `a`. 
# 2. Vyberte tento nový řádek a stiskněte `m`. Nyní lze do řádku místo kódu zapisovat text,
# 3. Zadávání ukončíte stisknutím kombinace `Shift` `+` `Enter`.
# 4. Pokud chcete řádek převést na kód, stiskněte `y`.
# 

# **Pro nápovědu stiskněte `h`.**

# ## Python

# Jednořádkový komentář se zadává za znak `#`, více řádků lze zakomentovat pomocí `"""` a `"""`:

# In[2]:


# toto je komentar
"""
Komentar
na vice
radku...
"""
print("Hello, World!") 


# Inicializace proměnných `a`, `b`, základní aritmetické operace a výpis výsledku pomocí funkce `print()`:

# In[3]:


a=43
b=5.0

soucet=a+b
rozdil=a-b
soucin=a*b
podil=a/b
mocnina=a**b
zbytek_po_deleni = a%b

# vypis
print('Soucet ',soucet)
print('Rozdil ',rozdil)
print('Soucin ',soucin)
print('Podil ',podil)
print('Mocnina ',mocnina)
print('Zbytek po deleni ',zbytek_po_deleni)


# <div class="alert alert-block alert-warning"><b>Cviceni 01.01: </b> Vypočtěte objem jehladnu o stranách 3 a 4 majiícího výšku 7. </div>

# In[4]:


a=3.0
b=4.0
v=7.0
S=a*b
V=1/3*S*v
print(V)


# ## Podmínkové cykly

# ### If ... else

# <div class="alert alert-block alert-danger"><b>Pozor:</b> vnitřní části kódu <b>nutné odsadit</b>, obvykle se používají <b>čtyři mezery</b>.</div>

# Za klíčovými slovy `if` a `else` musíme psát `:`.

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

# Funkce se definuje příkazem `def`. Následuje jméno funkce, seznam vstupních parametrů a vše je zakončené `:`. Tělo funkce musí být odsazené. Funkce může vrátit hodnotu pomocí příkazu `return`.

# In[8]:


def objem_jehlanu(a,b,v):
  return 1/3*a*b*v

print("Objem jehlanu = ",objem_jehlanu(2,3,4))


# <div class="alert alert-block alert-warning"><b>Cviceni 01.02: </b> Napište funkci, která rozhodne, zda zadané číslo je liché nebo sudé a vypište výsledek. </div>

# In[9]:


def funkce(c):
    if cislo % 2 == 0:
        print('Cislo ',c,' je sude.')
    else:
        print('Cislo ',c,' je liche.')

cislo = 5
funkce(cislo)


# ## Výjimky

# Pro odhalení případných chyb můžeme použít konstrukci `try - except`:

# In[10]:


try:
  print(neznama_promenna)
except: # pro pripad chyby
  print("Neco je spatne.")
else: # pokud se chyba neobjevi
  print("Vse je v poradku.") 


# ## Numerická knihovna numpy

# Pro import numerické knihovny `numpy` použijeme příkaz:

# In[11]:


import numpy as np


# ### Maticové operace

# Pole (vektor, matice) lze vytvářet pomocí funkce `array()`:

# In[12]:


# vektor
a = np.array([1, 2, 3])

# matice (pole)
A = np.array([[1,2,3],[4,5,6],[7,8,9]])


# <div class="alert alert-block alert-danger"><b>Pozor:</b> v poli <code>array</code> má <b>první prvek index 0</b>!</div>

# Rozměry pole zjistíme pomocí funkce `shape`:

# In[13]:


print(a.shape)
print(A.shape)


# Funkce `size` vrátí počet prvků v poli:

# In[14]:


print(a.size)
print(A.size)


# Matici lze transponovat funkcí `transpose()`:

# In[15]:


A_transponovana = A.transpose()
print(A_transponovana)


# Pro vytváření polí lze používat následující generátory:

# * Pomocí funkce `arange()` vytvoříme pole s prvky od 0 do 10 **(poslední prvek není obsažen)** a krokem 1:

# In[16]:


pole = np.arange(0,10,1)
print(pole)


# * Pomocí funkce `linspace()` vygenerujeme pole s prvky od 0 do 10 **(včetně)**, přičemž počet prvků je 20:

# In[17]:


pole = np.linspace(0,10,20)
print(pole)


# * Příkazem `logspace()` vytvoříme pole od 0 do 10 s počtem prvků 20 v logaritmickém měřítku ($\log_{10}$):

# In[18]:


pole = np.logspace(0,10,20,base=10)
print(pole)


# * Pomocí funkce `zeros()` vytvoříme nulovou matici 2x2:

# In[19]:


pole = np.zeros((2,2))
print(pole)


#  * Funkcí `ones()` vytvoříme jednotkovou matici 3x3:

# In[20]:


pole = np.ones((3,3))
print(pole)


# * Pomocí funkce `eye()` vytvoříme matici 3x3 s jedničkami na diagonále, ostatní hodnoty jsou nulové:

# In[21]:


pole = np.eye(3)
print(pole)


# * Pole náhodných čísel v rozmezí 0 az 1 se vygeneruje pomocí funkce `np.random.rand()`:

# In[22]:


pole_nahodnych_cisel = np.random.rand(3,2)


# Pro přístup k prvkům pole `A` používáme syntaxi `A[i,j]`, kde `i` je index řádku a `j` je index sloupce:

# In[23]:


prvni_prvek_pole = A[0,0]
print(prvni_prvek_pole)


# Pro přístup k prvkům pole používáme syntaxi `[min:max:krok]`. Mějme vektor $\mathbf{v}=(0,1,2,3,4,5,6)$. Nyní z něj vyjmeme první ("0") až šestý prvek ("5"), a to s krokem 2:

# In[24]:


v = np.arange(0,7)
print(v)
vyber_z_v = v[0:6:2]
print(vyber_z_v)


# Podobně u matice $A$ vybereme např. poslední dva prvky ve třetím sloupci.

# In[25]:


A_vyber = A[1:,2]
print(A_vyber)


# In[26]:


prvni_radek = A[0,:]
print(prvni_radek)


# In[27]:


prvni_sloupec = A[:,0]
print(prvni_sloupec)


# Násobení matic a vektorů se provádí pomocí operátoru `dot`:

# In[28]:


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


# <div class="alert alert-block alert-danger"><b>Pozor:</b> operace <b>C*C</b> násobí matice po prvcích (není to maticové násobení)</div>

# In[29]:


# maticove nasobeni
print(np.dot(C,C))

# nasobeni po prvcich
print(C*C)


# ### Funkce

# `numpy` obsahuje často používané funkce a konstanty (napr. `sqrt()`, `log()`, `log10()`, `sin()`, `abs()`, `e`, `pi`, ...):

# In[30]:


print(np.sqrt(5))
print(np.log(5))
print(np.log10(5))
print(np.sin(5))
print(np.abs(-3))
print(np.e)
print(np.pi)


# Součet prvků v poli je dán funkcí `sum()`:

# In[31]:


# soucet prvku v poli
soucet = np.sum(A)
print(soucet)


# Minimální a maximální hodnotu v poli určíme funkcí `min()` a `max()`:

# In[32]:


# maximalni hodnota v poli
maximum = np.max(A)
print(maximum)

# minimalni hodnota v poli
minimum = np.min(A)
print(minimum)


# Funkce `average()` vrací průměrnou hodnotu; `std()` je směrodatná odchylka a `var()` je rozptyl:

# In[33]:


# prumerna hodnota
prumer = np.average(A)
print(prumer)

# smerodatna odchylka
smerodatna_odchylka = np.std(A)
print(smerodatna_odchylka)

# rozptyl
rozptyl = np.var(A)
print(rozptyl)


# Index prvku v poli lze najít pomocí funkce `argwhere()`:

# In[34]:


index_hledaneho_prvku = np.argwhere(A == 3)
print(index_hledaneho_prvku)


# <div class="alert alert-block alert-info"><b>Tip: </b> Další příklady a návody pro práci s knihovnou <code>numpy</code> lze nalézt na <a href='https://numpy.org/'>https://numpy.org/</a>.</div>

# ## Visualizace dat

# Pro kreslení grafů využijeme knihovnu `matplotlib.pyplot`:

# In[35]:


import matplotlib.pyplot as plt


# ### Graf jedné proměnné

# Vygenerujeme $x$ a $y$ hodnoty pro funkci `sin()`:

# In[36]:


x = np.linspace(0,4*np.pi,100)
y = np.sin(x)


# Nejdříve je potřeba vytvořit obrázek pomocí `fig`. Vykreslení dat provedeme příkazem `plot()`:

# In[37]:


fig, ax = plt.subplots()
ax.plot(x,y)


# Přidáme popisky os pomocí `set_xlabel()`, `set_ylabel()` a název grafu pomocí `set_title()`:

# In[38]:


fig, ax = plt.subplots()
ax.plot(x,y)
ax.set_xlabel('x')
ax.set_ylabel('sin(x)')
ax.set_title('Graf funkce sin(x)')


# Přidáme funkci `cos()`, nastavíme barvu (`color`), styl (`linestyle`) a šířku (`linewidth`) linky. Průhlednost se nastavuje parametrem `alpha`. Legendu zobrazíme příkazem `legend()`:

# In[39]:


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


# Na závěr obrázek uložíme příkazem `savefig()`:

# In[40]:


fig.savefig("obrazek.png", dpi=300)


# ### Visualizace závislosti dvou proměnných

# Mějme funkci $z(x,y)$, která závisí na dvou proměnných $z(x,y)=\exp(-\sqrt{x^2+y^2})\cos(2x)\sin(2y)$, a vykreslíme její závislost v 2D grafu.

# Vytvoříme mřížku $x\times y$ pomocí funkce `meshgrid()`:

# In[41]:


fig, ax = plt.subplots()
osa_x = np.linspace(-2, 2, 50)
osa_y = np.linspace(-2, 2, 50)
(x,y) = np.meshgrid(osa_x,osa_y)


# Spočítáme hodnoty funkce $z(x,y)$:

# In[42]:


z = np.exp(-np.sqrt(x**2+y**2))*np.cos(2*x)*np.sin(2*y)


# 2D graf vykreslíme pomocí funkce `pcolor()` s parametrem `shading='auto'`:

# In[43]:


fig, ax = plt.subplots()
osa_x = np.linspace(-2, 2, 50)
osa_y = np.linspace(-2, 2, 50)
(x,y) = np.meshgrid(osa_x,osa_y)
z = np.exp(-np.sqrt(x**2+y**2))*np.cos(2*x)*np.sin(2*y)
ax.pcolor(x,y,z,shading='auto')


# Kontury získáme použitím funkce `contour()`:

# In[44]:


fig, ax = plt.subplots()
osa_x = np.linspace(-2, 2, 50)
osa_y = np.linspace(-2, 2, 50)
(x,y) = np.meshgrid(osa_x,osa_y)
z = np.exp(-np.sqrt(x**2+y**2))*np.cos(2*x)*np.sin(2*y)
ax.contour(x,y,z)


# ### 3D visualizace

# Máme stejnou funkci $z(x,y)=\exp(-\sqrt{x^2+y^2})\cos(2x)\sin(2y)$, kterou nyní chceme vykreslit v 3D grafu. Nejdříve vytvoříme trojrozměrnou osu:

# In[45]:


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')


# Vytvoříme mřížku $x\times y$ pomocí funkce `meshgrid`:

# In[46]:


osa_x = np.linspace(-2, 2, 50)
osa_y = np.linspace(-2, 2, 50)
(x,y) = np.meshgrid(osa_x,osa_y)


# Spočítáme hodnoty funkce $z(x,y)$:

# In[47]:


z = np.exp(-np.sqrt(x**2+y**2))*np.cos(2*x)*np.sin(2*y)


# 3D data vykreslíme pomocí funkce `plot_surface()` a přidáme popisky os:

# In[48]:


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

osa_x = np.linspace(-2, 2, 50)
osa_y = np.linspace(-2, 2, 50)
(x,y) = np.meshgrid(osa_x,osa_y)
z = np.exp(-np.sqrt(x**2+y**2))*np.cos(2*x)*np.sin(2*y)

ax.plot_surface(x, y, z)
ax.set(xlabel='x', ylabel='y', zlabel='z')


# <div class="alert alert-block alert-warning"><b>Cviceni 01.03: </b> Vykreslete průběh funkce $\log x$ pro $x$ od 0.1 do 10. Osy grafu popište, přidejte legendu a obrázek uložte ve formátu *.jpg.</div>

# In[49]:


x = np.linspace(1e-1,10,100)
y = np.log10(x)
fig, ax = plt.subplots()
ax.plot(x,y,label='log(10)')
ax.set_xlabel('x')
ax.set_ylabel('log(x)')
ax.legend()
fig.savefig('log10.jpg',dpi=100)


# <div class="alert alert-block alert-info"><b>Tip: </b> Další příklady a návody pro práci s knihovnou <code>matplotlib</code> lze nalézt na <a href='https://matplotlib.org/'>https://matplotlib.org/</a>.</div>
