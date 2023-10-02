#!/usr/bin/env python
# coding: utf-8

# # Słowniki

# In[8]:


slownik={}
print(slownik, type(slownik))


# In[28]:


slownik=dict()
print(slownik, type(slownik))


# In[29]:


slownik['Ala']='504 567 789'
print(slownik)


# In[30]:


slownik[('Ula' , 'Zula')]='664 678 678'
print(slownik)


# In[31]:


slownik['Tola']=('664 678 678','553 456 788')
print(slownik)


# In[14]:


print(slownik['Ala'])


# In[17]:


print( 'Franek' in slownik)

print('Ala' in slownik)


# In[32]:


slownik['Zenek']=' Brak telefonu'
print(slownik)
slownik['Zenek']=' Dostał telefon'
print(slownik)


# In[22]:


# Metody typu dict
print(slownik.keys())

print(slownik.values())

print(slownik.items())


# In[25]:


zm=slownik.pop('Aligator',' Nie ma')
print(zm)
print(slownik)


# In[27]:


zm=slownik.popitem()

print(zm)
print(slownik)


# In[35]:


#print(slownik)

for  element in slownik:
    print(element)


# In[36]:


for  element in slownik.keys():
    print(element)


# In[37]:


for  element in slownik.values():
    print(element)


# In[39]:


for  klucz, wartosc in slownik.items():
    print("Do klucza " ,klucz, " dowiazana jest ",wartosc)


# # Pliki

# In[40]:


plik=open("d:\PlikiPython\MegaKustTest.txt", 'w')
plik.writelines('Ala')
plik.writelines('Ola')
plik.writelines('Ula')
plik.close()


# In[43]:


plik=open("d:\\PlikiPython\\negaKustTest.txt", 'w')
plik.writelines('Ala\n')
plik.writelines('Ola\n')
plik.writelines('Ula\n')
plik.close()


# In[45]:


plik=open("d:\\PlikiPython\\negaKustTest.txt", 'a')
plik.writelines('Zosia\n')
plik.close()


# In[54]:


# Odczytywanie z pliku
plik=open("d:\\PlikiPython\\negaKustTest.txt", 'rt')
zawartosc=plik.readlines()
print(zawartosc)
plik.close()


# In[57]:


plik=open("d:\\PlikiPython\\negaKustTest.txt", 'rt')
print(plik.read(7))
plik.close()


# # Przykladowe programy

# In[67]:


plik=open('D:\\PlikiPython\\SlowaZamienniki.txt')
zawartosc=plik.readlines()
plik.close()
slownik={}
for linia in zawartosc:
      slowa=(linia.strip()).split(',')
      slownik[slowa[0]]=slowa[1]
listaKluczy=list(slownik.keys())      

plik=open('D:\PlikiPython\DoCenzury.txt')
zawartosc=plik.readlines()
plik.close()

wynik=[]
for linia in zawartosc:
      ListaSlow=(linia.strip()).split(' ')
      for i in range(len(ListaSlow)):
            if ListaSlow[i] in listaKluczy:
                  ListaSlow[i]=slownik[ListaSlow[i]]
      wynik.append(' '.join(ListaSlow)+'\n')

    
plik=open('D:\PlikiPython\PoCenzurze.txt', 'w')
plik.writelines(wynik)
plik.close()    


# In[ ]:




