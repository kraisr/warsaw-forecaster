#!/usr/bin/env python
# coding: utf-8

# # Funkcje w Pythonie

# In[6]:


def PierwszaFunkcja():
    liczba=int(input('Podaj liczbę całkowitą '))
    if liczba % 2 == 0:
        return liczba**2
    
print(PierwszaFunkcja())    
print(PierwszaFunkcja())   


# In[12]:


def DrugaFunkcja(liczba):
     if liczba % 2 == 0:
        return liczba**2
print(DrugaFunkcja(8))
print(DrugaFunkcja(9))
print(DrugaFunkcja(8)+DrugaFunkcja(12))    


# In[17]:


#Parametry z wartością domyślną
def sumuj(a=4,b=7):
    return a+b

print(sumuj(12,15))
print(sumuj(11))
print(sumuj())

print(sumuj(b=12))

print(sumuj(b=12, a=55))


# In[15]:


def RobListe(wartosc,lista=[]):
    lista.append(wartosc)
    return lista

print(RobListe(3))

print(RobListe('Ala'))

print(RobListe((3,7)))
print(RobListe(7,['a','b']))


# In[22]:


# Parametr z *

def sumator(a,b,*reszta):
    wynik=a+b
    for liczba in reszta:
        wynik+=liczba
    return wynik

print(sumator(4,2,7,8,9))
         


# In[23]:


#parametr z **

def Przyklad(a,b,*reszta,**slownik):
    print (a,b)
    print(reszta)
    print(slownik)

print(Przyklad(5,33,'Ola','Ula',False, kolor='red', imie='Tola', stanKonta=12456))    


# # Wartości losowe

# In[29]:


import random as rd
rd.random()


# In[36]:


rd.randrange(5)


# In[50]:


rd.randint(0,4)


# In[68]:


rd.randrange(0,20,3)


# In[72]:


lista=[1,4,7,4,2,8,9,3,4,2]
rd.choice(lista)


# In[82]:


rd.sample(lista,3)


# In[81]:


rd.shuffle(lista)

print(lista)


# # Przykladowe programy

# In[ ]:


# Napisać funkcję, która poprosi użytkonika o podanie słowa i zwróci  3 różne anagramy tego słowa


# In[ ]:


Wczytać plik o nazwie operacje.txt i utworzyć plik wynikowy (będzie omówione)

