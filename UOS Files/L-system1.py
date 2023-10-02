#%%
from turtle import *

aksjomat="F-G-G"
dlugosc=10
kat=120
zamiennikG='GG'
zamiennikF='F-G+F+G-F'
zamienniki={'G':'GG', 'F':'F-G+F+G-F','-':'-','+':'+'}
iteracje=5
zolw='kajman'

kajman=Turtle()
def Buduj2 (st,ile):
    nowy=""
    for litera in st:
        nowy+=zamienniki[litera]
    if ile>1:
            ile-=1
            return Buduj2(nowy,ile)
    else:
            return nowy
        


DoRysowania=Buduj2(aksjomat,iteracje)

SlPolecen={}

lista=[zolw+'.'+'fd('+str(dlugosc)+')']
SlPolecen['F']=lista
SlPolecen['G']=lista

lista=[zolw+'.lt('+str(kat)+')']
SlPolecen['+']=lista

lista=[zolw+'.rt('+str(kat)+')']
SlPolecen['-']=lista


kajman.pu()
kajman.goto(-300,200)
kajman.pd()
kajman.color('red')

for litera in DoRysowania:
    for polecenie in SlPolecen[litera]:
        eval(polecenie)
    






# %%
