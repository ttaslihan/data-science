# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 23:56:06 2021

@author: aslih
"""

import pandas as pd

df = pd.read_csv("iris.csv")
print(df.Species.unique())
print(df.info())
print(df.describe())
setosa= df[df.Species == "Iris-setosa"]

versicolor = df[df.Species == "Iris-versicolor"]

print(setosa.describe())
print(versicolor.describe())
#%% 
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("iris.csv")
df1 = df.drop(["Id"],axis=1)

#df1.plot()
#plt.show()

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.plot(versicolor .Id, versicolor .PetalLengthCm, color = "green", label="versicolor ")
plt.plot(virginica .Id, virginica.PetalLengthCm, color = "purple", label="virginica ")
plt.plot(setosa.Id, setosa.PetalLengthCm, color = "red", label="setosa ")
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()
plt.show()

df1.plot(grid=True, linestyle =":")
plt.show()

df1.plot(grid=True, alpha=10)
plt.show()
#%% scatter plot
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("iris.csv")
setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.scatter(setosa.PetalLengthCm,setosa.PetalWidthCm,color="red",label="setosa")
plt.scatter(versicolor.PetalLengthCm,versicolor.PetalWidthCm,color="green",label="versicolor")
plt.scatter(virginica.PetalLengthCm,virginica.PetalWidthCm,color="blue",label="virginica")
plt.legend()
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidhtCm")
plt.title("scatter plot")
plt.show()

#%% histogram plot
plt.hist(setosa.PetalLengthCm, bins=10)
plt.legend()
plt.xlabel("PetalLengthCm values")
plt.ylabel("frekans")
plt.title("hist")
plt.show()
#%% bar plot
import numpy as np
x=np.array([1,2,3,4,5,6,7])
a=["c","b","d","abd","turkey","ırak","italya"]
y= x*2+5

plt.bar(a,y)
plt.title("bar plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
#%% subplots
df1 = df.drop(["Id"],axis=1)
df1.plot(grid=True, alpha=0.9,subplots=True)

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.subplot(2,1,1)
plt.plot(setosa.Id,setosa.PetalLengthCm,color="red",label="setosa")
plt.ylabel("setosa -PetalLengthCm")
plt.subplot(2,1,2)
plt.plot(versicolor.Id,versicolor.PetalLenghtCm,color="blue",label="versicolor")
plt.ylabel("versicolor -PetalLengthCm")
plt.show()

import numpy as np

array1 = np.array([[1,2],[3,4]])

array2 = np.array([[-1,-2],[-3,-4]])

np.hstack((array1,array2))
