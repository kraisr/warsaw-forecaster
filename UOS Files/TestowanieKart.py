#%%
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import itertools
import random
from matplotlib.widgets import Button
import os
def DodajB(self):
    obszary[14].imshow(talia.pop().obraz)
def DodajG(self):
    obszary[25].imshow(talia.pop().obraz)


SCIEZKA=os.getcwd() + "/CardImages/"
KOLORY=('Pik','Kier','Karo','Trefl')
WARTOSCI=(['2',2],['3',3],['4',4],['5',5],['6',6],['7',7],['8',8],
         ['9',9],['10',10],['W',2],['D',3],['K',4],['A',11])
KARTY = list(itertools.product(KOLORY, WARTOSCI))

REWERS=mpimg.imread(SCIEZKA + 'Revers.png')
GRACZ=mpimg.imread(SCIEZKA + 'Gracz.png')
BANKIER=mpimg.imread(SCIEZKA + 'Bankier.png')
FURA=mpimg.imread(SCIEZKA + 'Fura.png')
WYGRANA=mpimg.imread(SCIEZKA + 'Wygrana.png')

class karta:
      def __init__(self,rodzaj,sciezka):
          self.kolor=rodzaj[0]
          self.wartosc=rodzaj[1][0]
          self.punkty=rodzaj[1][1]
          self.obraz=mpimg.imread(sciezka+rodzaj[1][0] + ' '+ rodzaj[0] + '.png')


talia = []
for tmp in KARTY:
      talia.append(karta(tmp,SCIEZKA))

random.shuffle(talia)

okno = plt.figure(figsize=(14,10),dpi=100)
obszary = []
for i in range(44):
    tmp = plt.subplot(4,11,i+1)
    tmp.axis('off')
    obszary.append(tmp)

okno.suptitle('Kasyno Pythona :)',
              fontsize = 16,
              fontweight ='bold',
              color = 'red')

obszary[11].imshow(BANKIER)
obszary[22].imshow(GRACZ)

bDlaBankiera = Button(plt.axes([0.79, 0.14, 0.1, 0.075]), 'Karta dla bankiera' )
bDlaBankiera.color ='green'
bDlaBankiera.on_clicked(DodajB)


axGraczStop = plt.axes([0.59, 0.14, 0.1, 0.075])
bGraczStop = Button(axGraczStop, 'Karta gracza')
bGraczStop.color ='red'
bGraczStop.on_clicked(DodajG)
plt.show()





# %%
