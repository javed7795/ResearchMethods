#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


data=pd.read_csv("Table-2019_44.csv")
data_X=[]
data_Y=[]


# In[3]:


X=data[data.Category=="Gross Imports"]["Crude Oil - Qty. - TMT"].values
Y=data[data.Category=="Gross Imports"]["Crude Oil - Value - Rs. Crore"].values
data_X.append(X)
data_Y.append(Y)
plt.figure(dpi=100)

plt.title("Crude Oil Value in Crores w.r.t. Crude Oil Quantity over years ")

# X and Y labels
plt.xlabel('Crude Oil Quantity in Trillion Metric Ton')
plt.ylabel('Crude Oil Value in Crores')


plt.scatter(X,Y)
# Show plot
plt.savefig("CrudeScatter.png", dpi=200)
plt.show()

X=data[data.Category=="Gross Imports"]["Petroleum  Products - Qty. - TMT"].values
Y=data[data.Category=="Gross Imports"]["Petroleum Products - Value - Rs. Crore"].values

data_X.append(X)
data_Y.append(Y)

plt.figure(dpi=100)

plt.title("Petroleum Products Value in Crores w.r.t. Petroleum Products Quantity over years ")

# X and Y labels
plt.xlabel('Petroleum Products in Trillion Metric Ton')
plt.ylabel('Petroleum Products Value in Crores')


plt.scatter(X,Y)
# Show plot
plt.savefig("PetroleumScatter.png", dpi=200)
plt.show()

X=data[data.Category=="Gross Imports"]["LNG - Qty. - TMT"].values
Y=data[data.Category=="Gross Imports"]["LNG - Value - Rs. Crore"].values

data_X.append(X)
data_Y.append(Y)

plt.figure(dpi=100)

plt.title("LNG Value in Crores w.r.t. LNG Quantity over years ")

# X and Y labels
plt.xlabel('LNG in Trillion Metric Ton')
plt.ylabel('LNG Value in Crores')


plt.scatter(X,Y)
# Show plot
plt.savefig("LNGScatter.png", dpi=200)
plt.show()


# In[4]:


box=[]
for i in range(3):
    box.append(data_Y[i]/data_X[i])

plt.figure(dpi=100)

plt.title("Price Distribution of Commodity w.r.t. Quantity over the years ")

# X and Y labels
plt.xlabel('Energy Commodity')
plt.ylabel('Energy Commodity Price in Crores Per TMT')

plt.boxplot(box)
my_xticks = ['Crude','Petroleum','LNG']
plt.xticks([1,2,3], my_xticks)
# Show plot
plt.savefig("BoxPlot.png", dpi=200)
plt.show()


# In[5]:


# Data for plot
n_groups = 7
Crude = box[0]
petrol = box[1]
LNG = box[2]



# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.25
opacity = 0.7

rects1 = plt.bar(index, Crude, bar_width,
alpha=opacity,
color='b',
label='Crude')

rects2 = plt.bar(index + bar_width, petrol, bar_width,
alpha=opacity,
color='g',
label='Petrol')

rects2 = plt.bar(index + 2*bar_width, LNG, bar_width,
alpha=opacity,
color='y',
label='LNG')



plt.xlabel('Year')
plt.ylabel('Commodity Price(in Crores) per TMT')
plt.title('Energy Commodity Price(in Crores) per TMT over the years')
plt.xticks(index + bar_width, np.unique(data.Year.values))
plt.legend()

plt.tight_layout()

plt.savefig("barplot.png", dpi=200)

plt.show()

