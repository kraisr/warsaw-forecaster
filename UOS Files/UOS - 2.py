#!/usr/bin/env python
# coding: utf-8

# # Operacje na typie danych str

# In[11]:


zm1='Tekst pierwszy'
zm2="Tekst drugi"
zm3=""" A to jest inny tekst
  zapisany w wielu wierszach
  .... bo tak"""
print(zm3)


# # Indeksowanie typu str

# In[17]:


napis="To jest tekst do eksperymetów"

print(napis[3])
print(napis[-2])
print(napis[1:8])
print(napis[12:])
print(napis[:12])
print(napis[1:8:2])


# In[19]:


# czy uda sie zmienic literę w napisie

napis2=napis[:5]+'t'+napis[5+1:]
print(napis2)


# # Metody typu str

# In[21]:


napis ='dzisiaj jest piękny dzień, jedyny w swoim rodzaju'
zm=napis.capitalize()
print(zm)


# In[25]:


#  metoda count zlicza wystąpienia

print( napis.count('jeż'))


# In[27]:


# metoda find  - sprawdza i pokazuje gdzie wystepuje fragment
print( napis.find('jeż'))


# In[29]:


# metoda index  podobna do find - sprawdza i pokazuje gdzie wystepuje fragment
print( napis.index('jeż'))


# In[33]:


# metody sprawdzające
zm='345.0'
print(zm.isdecimal())
print(zm.isnumeric())
print(zm.isalnum())


# In[13]:


#   modyfikacja pierwszego programu 

CzyOk=True
while CzyOk:
    odpowiedz=input(" Podaj dowolną liczbę - ")
    try:
        odpowiedz=int(float(odpowiedz)// 1)
        CzyOk=False
    except ValueError:
        print('Naucz sie gamoniu pisać liczby - .... jeszcze raz')
        CzyOk=True

if odpowiedz % 2 == 0 :
    print('Podałeś liczbę - ', odpowiedz)
    print('To jest liczba parzysta')
else:
    print('Podałeś liczbę - ', odpowiedz)
    print('To jest liczba nieparzysta')


# # Listy

# In[17]:


# tworzenie listy
lista1=[]
lista2=list()

print(type(lista1), type(lista2))

lista3=['Ola', 'Ala','Ula', 'Zula', 'Tola']

lista4=[1,4,6.34,'Ola', True, 56>5, [1,2,3]]

print(type(lista3),lista3)


# In[22]:


# indeksowanie listy
print(lista4[6][1])

lista4[3]='Olek'
print(lista4)


# In[24]:


# metody typu list
print(lista1)
lista1.append('Ola')
lista1.append('Ala')
lista1.append('Zula')
lista1.append('Olaf')
lista1.append('Tola')
print(lista1)
#  append dodaje element listy na końcu


# In[26]:


zm=lista1.insert(2,'Alek')
print(lista1)
print(zm)


# In[30]:


# usuwanie elementów z listy
lista1.remove('Alek')
print(lista1)


# In[33]:


print ('Ala' in lista1)


# In[36]:


# łaczenie list
l1=['Ola','Tola']
l2=['Zula', 'Olaf']

l1.extend(l2)
print(l1)


# In[37]:


# Pobieranie z listy
print(lista1)
lista1.append('Ola')
lista1.append('Ala')
lista1.append('Zula')
lista1.append('Olaf')
lista1.append('Tola')
print(lista1)

lista1.pop()


# In[41]:


print(lista1)
zm=lista1.pop(0)
print(zm)
print(lista1)


# In[39]:


print(lista1)


# In[47]:


lista1.sort()
print(lista1)
lista1.reverse()
print(lista1)


# In[51]:


napis='Tertowanie'
napis=list(napis)
napis[2]='s'
napis=''.join(napis)
print(napis)


# In[72]:


#  Końcowy programik dnia drugiego

lista=['Ola','Jola','Zula']
lista=lista*3
l1=['Ula']*5
lista=lista+l1

odp=input('Jakie imie mam usunąć z listy ??? - ')
ile=lista.count(odp)

if ile==0:
    print('Nic nie robię - nie ma takiej osoby')
else:
    print(odp, "występuje ", ile , "razy ")
    ilosc=int(input('Podaj ile wystąpień '+odp+" mam usunąć ??? "))
    if ile<ilosc:
        ilosc=ile
        
    for i in range(ilosc):
        lista.remove(odp)

print('... i po robocie')
print(lista)
    
    


# In[61]:


lista.append('Ula')
print(lista)


# In[ ]:





# In[ ]:




