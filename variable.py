# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 14:02:19 2020

@author: aslih
"""

#string
#%%
s="bugun günlerden pazartesi"
variable_type=type(s)
var1="ankara"
var2="ist"
var3=var1+var2
print(var3)
#%%
#%%
var4="100"
var5="200"
var6=var4+var5
uzunluk=len(var6)
#%%
#numbers
#int, double
integer_deneme =-50
#double=float
float_deneme=-10.7
#%%
#built in function=daha önce tanımlanmış fonksiyonlar
str1 = "deneme"
float1=10.6
#round(float1)=11
str2="1006"
#output=type(parametre(input))
#%%
#user defined functions
a=20
b=50
c=(((a+b)*50)/b)*b/a

def fonksiyon1(c,d):
    """
    bu benim ilk denemem
    
    parametre:
    
    return:
    

    """
    e=(((c+d)*50)/d)*d/c
    return e
sonuc=fonksiyon1(10,20)
def deneme1():
    print("bu benim ikinci denemem")
#%%
#default ve flexible functionlar
#default
def cember_cevresi_hesapla(r,pi=3.14):
    """
    cember cevresi hesapla
    input(parametre):r,pi
    output=cemberin cevresi
    """
    output=2*pi*r
    return output
#%%
#flexible
# def hesapla(boy,kilo):
#     """
#     input(parametre)=boy,kilo
#     output=(boy+kilo)
#     """
#     output=(boy+kilo)
#     return output  
#ctrl ve 1 tusuna aynı anda basınca toplu olarak commente alır.

# def hesapla(boy,kilo,yas):
#     """
#     input(parametre)=boy,kilo,yas
#     output=(boy+kilo)*yas
#     """
#     output=(boy+kilo)*yas
#     return output
#%%
def hesapla(boy,kilo,*args):
    print(args)
    output=(boy+kilo)*args[0]
    return output
#%%
 #%% QUİZ    
 # int variable yas
 # string name isim
 # fonksiyonu olacak
 # fonksiyon print(type(),len,float())
 # *args soyisim
 # default parametre ayakkabi numaraı
#%% 
 yas =10
 name = "Aslıhan"
 soyisim = "Tat"
 def fuction ( yas,name,*args,ayakkabi_numarasi=35):
     print("ismi:",name,"yasi:",yas,"ayak numarasi:",ayakkabi_numarasi)
     print(type(name))
     print(float(yas))
     
     output = args[0]*yas
     
     return output
 
 sonuc = fuction(yas,name,soyisim)
 print("args[0]*yas:",sonuc)   
#%%
kilo=55
boy=1.70
isim= "aslihan"
soyisim="tat"
def function_1(kilo,boy,*args,yas=19):
    print("kilosu:",kilo,"boyu:",boy,"yası:",yas)
    print(type(boy))
    print(float(kilo))
    output =args[0]*(boy*boy)
    
    return output
#%% lambda function
def func1(x):
    return x*x
sonuc = func1(3)
#%% kisa yontem
sonuc2= lambda x:x*x
 print(sonuc2(3))
#%%
 #list
 liste = [1,2,3,4,5]
 type(liste)
 
 liste_str=["pts","sali","perş","cuma"]
 type(liste_str)
 value = liste_str[1]
 print(value)
 liste_dvide=liste[0:3]
 liste.append(7)
 liste.remove(7)
 liste.reverse()
 liste2 = [1,3,5,6,2,4]
 liste2.sort()
 string_int_liste= [1,2,3,4,"a","b"]
 #%% tuple
 t=(1,2,3,2,5,6,2,8,9)
 t.count(5)
 t.count(2)
 t.index(6)
 #%% dictionary
 
 
d ={"alis":13,"pakizan":2,"efe":8,"sukufe":7}
# ali,veli,ayse = keys
# 13,2,8,7 = values
def deneme():
    d ={"alis":13,"pakizan":2,"efe":8,"sukufe":7}
    return d
#%% conditionals
#if else statement
var1 =10
var2 =15
if (var1>var2):
    print("var1 büyüktür var2")
elif (var1==var2):
    print("esitler")
else:
    print("var2 büyüktür var1")
#%%
liste =[1,2,3,4,5]

value=6
if value in liste:
    print("evet {} listenin içinde.".format(value))
    
else:
    print ( "hayır {} değeri listenin içinde degil.".format(value))
#%%    
    
keys = d.keys()

if "aslı" in keys :
    print("evet")
    
else:
    print("hayır"),

#%% QUİZ

def f1(yas):
    str_yas=str(yas)
    
    if(len(str_yas)<3):
        return 1
    elif(len(str_yas)==3):
        if(str_yas[1:3]=="00"):
            return int(str_yas[0])
        else:
            return int(str_yas[0]+ 1)
    else:
        if (str_yas[2:]=="00"):
            return int(str_yas[:2])
        else:
            return int(str_yas[:2])+1
#%% 
# for loap
for each in range (1,11):
    print(each)
for each in "ankara ist":
    print (each)
for each in "ankara ist".split():
    print(each)
liste=[1,2,3,4,5,6,68]
summation=sum(liste)
count=0
for each in liste:
    count=count+each
    print(count)
#while loap
i=0
while(i<4):
    print(i)
    i=i+1
    
liste=[1,2,3,4,5,6,68]   
sinir=len(liste)   
each=0
count=0
while(each<sinir):
    count = count + liste[each]
    each = each + 1
#%%
liste =[1,2,3,4,5,6,4,23,67,21,-500,23,451,46]
mini=10000
for each in liste:
    if(each < mini):
        mini = each
    else:
        continue
#%%
liste1 =[3,4,5,6,7,8,9,245,654,876] 
max=300
for each in liste1:
    if(each>max):
        max = each
    else:
        continue
#%% PYTHON BASİCS DONE
#class
class Calisan:
    zam_orani = 1.8
    counter=0
    def __init__(self,isim,soyisim,maas):#constructor
      self.isim=isim
      self.soyisim=soyisim
      self.maas=maas
      self.email=isim + soyisim +"@asd.com"
      Calisan.counter = Calisan.counter +1
    
    def giveNameSurname(self):
      
      return self.isim + " "+self.soyisim
  
    def zam_yap(self):
        
        self.maas = self.maas + self.maas*self.zam_orani
  
# isci1 = Calisan ("ali","veli",1000)  
# print(isci1.giveNameSurname()) 
# print(isci1.maas) 
#class variable    
calisan1 = Calisan("ali","veli",1000)

print("ilk maas:",calisan1.maas)

calisan1.zam_yap()
print("yeni maas:",calisan1.maas)
calisan2 = Calisan("aslı","tat",7000)
calisan3 = Calisan("yagiz","tut",5000)
calisan4 = Calisan("emo","taş",6000)
#class example
liste=[calisan1,calisan2,calisan3,calisan4]
index=-1
maxi_maas = -1
for each in liste:
    if(each.maas>maxi_maas):
        maxi_maas=each.maas
        index=each
    else:
        continue
print(maxi_maas)  
print(index.giveNameSurname())
#%% syntax error---> genelde yazım hatasidir.
print(9)
#print 9
i=0
while(i<10):
    print (i)
    i=i+1
#%% exceptions

a=10
b="2"
liste = [1,2,3]
print(sum(liste))
#print(a+b)
print(str(a)+b)
print(a+int(b))


k=10
zero=0
print(k)   
#a=k/zero
if(zero==0):
    a=0
else:
    a= k/zero

try:
    a = k/zero 
except ZeroDivisionError:
    a=0
    
    
#index error
list1= [1,2,3,4,5]    
list1[15]

# module not found error
import numppy

# file not found error
import pandas as pd
pd.read_csv("pandas")

# type error
"2"+2
# value error
int("123")
int("sad")

try:
    1/1
except:
    print("except")
else:
    print("else") 
finally:
    print("done")
    
s = "fffggg"

s[::-2]

a = 5.5

b = 3

print(a//b)

sum(1,2,3)
l = [lambda x:x**2, lambda x:x+2,lambda x:x*2]

for i in l:

    print(i(5))

a = {"x":2,"y":3}

b = dict(zip(a.values(),a.keys())) 
if "zaa" in {"caa":1,"zaa":2}:

    print("a")

    if "aa" in "zaa":

        print("b")

class DataiTeam:

   

    def __init__(self, x = "hi"):

        self.x = x



    def show(self):

        print(self.x)



my_class = DataiTeam()

my_class.show() 
d1={"datai"=1,"team"=2}      

a = "zaa"

b = "maa"

print("aa" in 2*(a+b)) 


a = 5.5

b = 3

print(a//b)
#%%
#importing
import numpy as np
#numpy basics
 
array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(array.shape)

a = array.reshape(3,5)
print("shape: ",a.shape)
print("dimension: ",a.ndim)
print("data type: ",a.dtype.name)
print("size:",a.size)
print("type:",type(a))


array1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]],)
print(array1.shape)
zeros=np.zeros((3,4))
zeros[0,0]=5
print(zeros)
np.ones((3,4))
np.empty((2,3))
a= np.arange(10,50,5)
a=np.linspace(10,50,20)
print(a)

#%% numpy basics
import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])
print(a+b)
print(a-b)
print(a**b)
print(np.sin(a))
print(a<2)
c = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2,3],[4,5,6]])
#element wise product
print(c*b)
#matrix product
a.dot(b.T)
print(np.exp(a))
a= np.random.random((5,5))
print(a.sum())
print(a.max())
print(a.min())
print(a.sum(axis=0))
print(a.sum(axis=1))
print(np.sqrt(a))
print(np.square(a)) #a**2
print(np.add(a,a)) #= #a+a
#indicing and slicing
array = np.array([1,2,3,4,5,6,7])
reverse_array =array[::-1]
array1 =np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array1[1,1])
print(array1[1,1:4])
print(array1[-1,:])
print(array1[:,-1])
#%%
import numpy as np
#shape manipulation
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
a= array.ravel()
array2 = a.reshape(3,3)
arrayT = array2.T
print(arrayT.shape)
array5 = np.array([[1,2],[3,4],[5,6]])
array1 = np.array([[1,2],[3,4]])
array2 = np.array([[-1,-2],[-3,-4]]) 
array3= np.vstack((array1,array2))
array4 = np.hstack((array1,array2))
#%% convert and copy
liste = [1,2,3,4]
array = np.array(liste)
liste2 = list(array)
a = np.array([1,2,3])
b = a
c = a
b[0]=4

d= np.array([4,7,9])

e = d.copy()
f = d.copy()
g = d.copy()










   
        

    
    
  
    







