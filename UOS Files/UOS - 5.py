#!/usr/bin/env python
# coding: utf-8

# # UOS  - Kurs Python 5  - Warsztaty 

# # Napisać program, który pobierze od użytkownika słowo i utworzy listę zawierającą 3 różne anagramy danego słowa.
# 
# 

# In[31]:


slowo= input (" Podaj słowo - ")
wynik=[]
for litera in slowo:
    if litera not in wynik:
        wynik.append(litera)
if len(wynik)   <3:
    print('Interesują mnie słowa zawierajace conajmniej trzy różne litery')
else :
    wynik=[]
    while len(wynik)<3:
        slowo=list(slowo)
        rd.shuffle(slowo)
        anagram=''.join(slowo)
        if anagram not in wynik and anagram != slowo:
            wynik.append(anagram)
print(wynik)            


# In[48]:


import random as rd
import math as m

def AnagramSlowa(slowo, ile):
    wynik=[]
    if isinstance(slowo,str)==False or isinstance(ile,int)==False:
        return 'Niepoprawne parametry'
    else:
        for litera in slowo:
            if litera not in wynik:
                wynik.append(litera)
        if len(wynik)   <3 or ile>m.factorial(len(wynik)) :
            return 'Interesują mnie słowa zawierajace conajmniej trzy różne litery i dopuszczalna liczba anagramów lub złe typy'
        else :
            wynik=[]
            while len(wynik)<ile:
                slowo=list(slowo)
                rd.shuffle(slowo)
                anagram=''.join(slowo)
                if anagram not in wynik and anagram != slowo:
                    wynik.append(anagram)
    return wynik

AnagramSlowa('kkuyt',5)


# In[51]:


def ListaAnagramow(*dane):
    wynik=[]
    for slowo in dane:
        wynik.append(AnagramSlowa(slowo[0],slowo[1]))
    return wynik

ListaAnagramow(('piesek',4),('kotek','ala'),('bocian' ,7))
        


# In[27]:


import random as rd
zm='krokodyl'
zm=list(zm)
rd.shuffle(zm)
print(zm)
print(''.join(zm))


# Po przetestowaniu programu utworzyć funkcję, która przyjmuje jako parametr listę słów i zwraca  trzy różne anagramy dla każdego słowa( strukturę danych dla zwracanej wartości można wybrać samemu)

# In[2]:


import random as rd
slowo=input('Podaj słowo - ')
wynik=[]
if len(slowo)<3:
    wynik.append('Dla słowa '+slowo+' nie da sie utworzyć trzech róznych anagramów')
else:    
    for i in range(3):
        czyKontynuacja=True
        while  czyKontynuacja:
            anagram=''.join(rd.sample(slowo,len(slowo)))
            if anagram not in wynik:
                wynik.append(anagram)
                czyKontynuacja=False
            else:
                czyKontynuacja=True
     

print(wynik)


# In[22]:


def AnagramSlowa(slowo):
    wynik=[]
    slowo=str(slowo).lower()
    if len(slowo)<3:
        wynik.append('Dla słowa '+slowo+' nie da sie utworzyć trzech róznych anagramów')
    else:    
        for i in range(3):
            czyKontynuacja=True
            while  czyKontynuacja:
                anagram=''.join(rd.sample(slowo,len(slowo)))
                if anagram not in wynik:
                    wynik.append(anagram)
                    czyKontynuacja=False
                else:
                    czyKontynuacja=True   
    return wynik

print(AnagramSlowa(1256))


# In[23]:


def AnagramListySlow(*lista):
    ListaWynik=[]
    for slowo in lista:
        ListaWynik.append(AnagramSlowa(slowo))
    return ListaWynik

print(AnagramListySlow('Kot','Pies', 'zeBRa','as',112))
    


# In[40]:


print(type('aaa'))


zm='aaaaa'
isinstance(zm, str)


# In[ ]:




