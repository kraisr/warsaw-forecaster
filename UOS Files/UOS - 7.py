#!/usr/bin/env python
# coding: utf-8

# # Elementy interaktywne + wykresy

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons
import os
get_ipython().run_line_magic('matplotlib', 'notebook')

x=np.arange(-5,5,0.01)
y1=5*np.sin(x)
y2=0.25*x**2
y3=np.sin(1/x**2)
slownik={'5*sin(x)':y1, '0.25$x^2$':y2 , 'sin(1/$x^2$)':y3}



okno, obszar=plt.subplots()
okno.subplots_adjust(left=0.3)
linia,=obszar.plot(x, y1, lw=1, color='red')


rax = plt.axes([0.05, 0.7, 0.18, 0.18], facecolor='lightgray')
radio = RadioButtons(rax,('5*sin(x)','0.25$x^2$','sin(1/$x^2$)'))

def ZmianaFunkcji(label):
      linia.set_ydata(slownik[label])
      plt.draw()

      
radio.on_clicked(ZmianaFunkcji)


rax = plt.axes([0.05, 0.4, 0.15, 0.15], facecolor='lightgray')
radio2 = RadioButtons(rax, ('red', 'blue', 'magenta'))

def KolorFunkcji(label):
    linia.set_color(label)
    plt.draw()
    
radio2.on_clicked(KolorFunkcji)


rax = plt.axes([0.05, 0.1, 0.15, 0.15], facecolor='lightgray')
radio3 = RadioButtons(rax, ('1', '2', '3'))

def GruboscLinii(label):
    linia.set_linewidth(int(label))
    plt.draw()
radio3.on_clicked(GruboscLinii)


# # Zadanie do próby samodzielnego wykonania

# In[3]:


plik=open(os.getcwd() + '/ListaFunkcji.txt','r')
zawartosc=plik.readlines()
plik.close()

okno=plt.figure(figsize=(14,10), dpi=100)
okna=[]
for i in range(9):
      okna.append(plt.subplot(3,3,i+1))
 

x=np.arange(-10,10,0.1)

for i in range(9):
    dane=(zawartosc[i].strip()).split(',')
    y=eval(dane[0])
    okna[i].plot(x,y, color=dane[2], lw=int(dane[3]))
    okna[i].set_title(dane[1])  
    
plt.tight_layout()   






# In[ ]:




