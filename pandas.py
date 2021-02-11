# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 22:02:36 2021

@author: aslih
"""

# 1) Pandas hızlı ve etkili for dataframes
# isim yas medeni hali --> dataframes
# veli 45 bekar 

# 2) csv ve text dosyalarini acip inceleyeyip sonuclarimizi bu dosya tiplerine rahatca
# rahatca kaydedebilir

# 3) pandas bizim işimizi kolaylastırıyor for missing data.
# 4) reshape yapıp datayı daha etkili bir şekilde kullanılır.
# 5) slicing, indexing kolay
# 6) time series data anlizinde çok yardımcı
# 7) her şeyden önemlisi hız!!! pandas hız açısından optimize edilmiş hızlı bir kütüphane

import pandas as pd

dictionary= { "NAME":["ali","veli","kenan","ayse","evren","mehmet"],
             "AGE":[15,16,17,18,46,87],
             "MAAS":[100,150,240,560,890,600]}
dataframe1 = pd.DataFrame(dictionary)
head = dataframe1.head() #--> baştaki 5 satırı vermek için kullanılır.
tail = dataframe1.tail() #--> sondaki 5 satırı gösterir.
#%%
# pandas basic method

print(dataframe1.columns)
print(dataframe1.info())
print(dataframe1.dtypes) #**
print(dataframe1.describe()) # sadece nümerik feature alır = columns(age,maas)
#%% indexing and slicing
print(dataframe1["AGE"])
print(dataframe1.AGE)
dataframe1["NEGATİF"]=[-1,-2,-3,-4,-5,-6]

print(dataframe1.loc[:,"AGE"])

print(dataframe1.loc[:3,"AGE"])

print(dataframe1.loc[:3,"AGE":"NEGATİF"])

print(dataframe1.loc[:3,"AGE":"yeni feature"])

print(dataframe1.loc[::-1,:])

print(dataframe1.loc[:,:"MAAS"])

print(dataframe1.iloc[:,2])
#%% filtering

filtre1 = dataframe1.MAAS>200

#dataframe tablo şeklinde olanlara denir------ series ise tek sütün halinde olanlara denir
filtrelenmis_data = dataframe1[filtre1]
filtre2 = dataframe1.AGE<20
dataframe1[filtre1 & filtre2 ]#**
print(dataframe1[dataframe1.AGE>85])
#%% list comprehension
import numpy as np
dataframe1.MAAS
ortalama_maas = dataframe1.MAAS.mean()
# ortalama_maas_np = np.mean(dataframe1.MAAS)
dataframe1["maas_seviyesi"]= ["dusuk"if ortalama_maas > each else " yuksek" for each in dataframe1.MAAS]
# for each in dataframe1.MAAS:
#      if (ortalama_maas>each):
#           print("yüksek")
#      else:
#           print("dusuk")
dataframe1.columns = [each.lower() for each in dataframe1.columns]
dataframe1.columns = [each.split()[0]+"_"+each.split()[1] if(len(each.split())>1) else each for each in dataframe1.columns]
#%% concatenating and drop

dataframe1.drop(["yeni_feature"],axis = 1, inplace=True)

data1 = dataframe1.head()
data2 = dataframe1.tail()
# vertical 
data_concat = pd.concat([data1,data2],axis=0)
#horizontal

maas= dataframe1.maas
age = dataframe1.age
data_h_concat= pd.concat([maas,age],axis=1)
#%% Transforming data
dataframe1["two_age"]=[each*2 for each in dataframe1.age]
#apply
def multiply(age):
    return age*2
dataframe1["apply_metodu"]= dataframe1.age.apply(multiply)
