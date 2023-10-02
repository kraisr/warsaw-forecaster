#!/usr/bin/env python
# coding: utf-8

# # Rysowanie wykresów z pakietem matplotlib

# In[38]:


# Potrzebne pakiety
import matplotlib.pyplot as plt
import numpy as np
# Właczyć tryb interaktywny
get_ipython().run_line_magic('matplotlib', 'inline')

x=(4,7,5,12,7,3,2,-1)
plt.plot(x, color='magenta', lw=3)


# In[40]:


# Pierwszy wykres
import matplotlib as mp
x=np.arange(-8, 8, 0.1)
y=np.sin(x)
y1=np.cos(x)

#mp.rc('lines',lw=2,linestyle='-',marker='*')
#mp.rcParams['lines.markersize']=3
#mp.rcParams['font.size']='14.0'

mp.rcdefaults()
plt.plot(x,y,color='green', lw=1, label='Funkcja sin(x)')
plt.plot(x,y1,color='red', lw=1, label='Funkcja cos(x)')
plt.axvline(0, ls='dashed')
plt.axhline(0,ls='dashed')
plt.legend(loc=5)
plt.suptitle('To jest nasz wykres')
plt.xlabel('Os x')
plt.ylabel('Os y')


#plt.savefig("D://Test333.pdf")


# In[58]:


# Wiele wykresów w jednym oknie

get_ipython().run_line_magic('matplotlib', 'notebook')
x=np.arange(-8,8,0.1)

y1=np.sin(x)
y2=x**2 
y3=np.sin(x)/x
y4= x**3

okno, obszary=plt.subplots(2,2)
okno.suptitle('Tytuł okna', fontsize=14, fontweight='bold', color='red')
obszary[0,0].plot(x,y1, color='blue', lw=2, label='sin(x)')
obszary[0,0].set_title('Wykres funkcji sin(x)')

obszary[0,1].plot(x,y2, color='red', lw=2, label='$x^2$')
obszary[0,1].set_title('Wykres funkcji $x^2$')

obszary[1,0].plot(x,y3, color='magenta', lw=2, label='sin(x)/x')
obszary[1,0].set_title('Wykres funkcji sin(x)/x')

obszary[1,1].plot(x,y4, color='green', lw=3, label='$x^3$')
obszary[1,1].set_title('Wykres funkcji $x^3$')
plt.tight_layout()



# In[71]:


# Wykresy trójwymiarowe
get_ipython().run_line_magic('matplotlib', 'notebook')
from pylab import *
from mpl_toolkits.mplot3d import Axes3D

fig=figure()
ax=Axes3D(fig)


y=x = linspace(-10,10,100) 
X,Y=meshgrid(x,y)
Z1=sqrt(X**2+Y**2)
Z=sin(Z1)/Z1
ax.plot_surface(X,Y,Z,cmap='flag')
show()


# In[67]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.collections as collections


t = np.arange(0.0, 2, 0.01)
s1 = np.sin(2*np.pi*t)
s2 = 1.2*np.sin(4*np.pi*t)


fig, ax = plt.subplots()
ax.set_title('using span_where')
ax.plot(t, s1, color='black')
ax.axhline(0, color='black', lw=2)

collection = collections.BrokenBarHCollection.span_where(
    t, ymin=0, ymax=1, where=s1 > 0, facecolor='green', alpha=0.5)
ax.add_collection(collection)

collection = collections.BrokenBarHCollection.span_where(
    t, ymin=-1, ymax=0, where=s1 < 0, facecolor='red', alpha=0.5)
ax.add_collection(collection)


plt.show()


# In[ ]:




