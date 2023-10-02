import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import itertools as it
import random as rd
from matplotlib.widgets import Button

akt=1
SCIEZKA="D:\\PrzykladyPython\\ObrazyKart\\"
KOLORY=['Pik','Kier','Karo','Trefl']
WARTOSCI=[['2',2],['3',3],['4',4],['5',5],['6',6],['7',7],['8',8],['9',9],['10',10],['W',2],['D',3],['K',4],['A',11]]
KARTY = list(it.product(KOLORY, WARTOSCI))
REWERS=mpimg.imread(SCIEZKA+'Revers.png')

class karta:
      def __init__(self,rodzaj,sciezka):
          self.kolor=rodzaj[0]
          self.wartosc=rodzaj[1][0]
          self.punkty=rodzaj[1][1]
          if self.kolor=='Rewers':
                self.obraz=mpimg.imread(sciezka+'Revers.png')
          else:
                self.obraz=mpimg.imread(sciezka+rodzaj[1][0]+' '+rodzaj[0]+'.png')

                  

idx=1

talia=[]
for tmp in KARTY:
      talia.append(karta(tmp,SCIEZKA))



rd.shuffle(talia)

okno=plt.figure(figsize=(12,8),dpi=100)
okno.suptitle('Kasyno Kurs Radom :)', fontsize=16, fontweight='bold')
plt.title('Nasza gra w oczko')

aa=plt.subplot(4,6,1)

plt.plot()
plt.axis("off")
obr=plt.imshow(REWERS)
axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Next')

plt.subplot(4,6,1)
plt.axis("off")
for i in range(10):
      plt.subplot(4,6,i+2)
      obr=plt.imshow(talia[i].obraz)
      plt.axis("off")

def OnClick(event):
      global idx
      plt.subplot(4,6,2)
      obr=plt.imshow(talia[idx].obraz)
      plt.axis("off")
      idx+=1
      plt.draw()
      
    
fig = plt.gcf()
cid_up = fig.canvas.mpl_connect('button_press_event', OnClick)
plt.show()      
##k1=talia[7]
##print(k1.kolor)
##print(k1.wartosc)
##print(k1.punkty)
##imgplot = plt.imshow(k1.obraz)
##plt.axis("off")
##plt.show()
      
                                  


