#!/usr/bin/env python
# coding: utf-8

# # Pogodynka 2 :)

# # Nowa sekcja

# In[1]:


#%%sh
#curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
##curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
#sudo apt-get update
#sudo ACCEPT_EULA=Y apt-get -q -y install msodbcsql17

#!pip install pyodbc


import pandas as pd
import pyodbc
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
##%matplotlib notebook

okno=plt.figure(figsize=(8,6), dpi=100)

polaczenie = pyodbc.connect("""DRIVER={ODBC Driver 17 for SQL Server};
                            SERVER=analityk.wwsi.edu.pl,50221;
                            DATABASE=synop;
                            uid=student;
                            pwd=ciekawski""") 
zapytanie = """SELECT 
                    dl,
                    szer,
                    nr
               FROM PolskaPunkty """
kontury=pd.read_sql(zapytanie, polaczenie)
#print(kontury)

zapytanie="""
SELECT  distinct data,
        godzina,
        CisnienieNaPoziomieMorza as cisn,
        TemperaturaPowietrza as temp,
        TemperaturaPunktuRosy as tempR,
        row_number() over (Order by data,godzina) as nr
from Depesze 
where data> dateadd(day,-3,cast(getdate() as date))
       and stacja='12375'
      """
daneW=pd.read_sql(zapytanie, polaczenie)
#print(daneW)

zapytanie="""with ct as
(
   Select top 1 godzina
   from Depesze
   where data=cast(getdate() as date)
   group by godzina
   having count(*)>40
   order by godzina desc
)
SELECT  distinct data,
        godzina,
        dlugosc as dl,
        szerokosc as szer,
        CisnienieNaPoziomieMorza as cisn,
        TemperaturaPowietrza as temp
from Depesze as D join Stacje as s ON D.stacja=S.idstacji
where kraj='Poland' and data=cast(getdate() as date)
       and godzina=(Select godzina from ct)
      and CisnienieNaPoziomieMorza>0"""
daneI=pd.read_sql(zapytanie, polaczenie)
daneI.head()

#obszar=plt.subplot(4,1,1)
plt.plot(daneW['nr'], daneW['cisn'], color='blue')
#plt.set_title('Zmiany ciśnienia w Warszawie')




plt.show()


# 

# In[ ]:





# 

# In[ ]:





# # Nowa sekcja

# In[ ]:





# 
