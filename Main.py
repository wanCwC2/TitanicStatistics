#Example
import matplotlib.pyplot as plt
import matplotlib.style
import pandas as pd
import numpy as np
matplotlib.style.use('ggplot')
df = pd.read_csv('http://bit.ly/kaggletrain')

male = 0 #total number of men
female = 0 #total number of women

#Male/Female total separately
for i in range(0, df.shape[0]):
    if df.loc[i, "Sex"]  == "male":
        male += 1
    if df.loc[i, "Sex"] == "female":
        female += 1
print(male, female)


#Find max age
#For calculate the interval
max = 0
min = 100
min_i = 0
for i in range(0, df.shape[0]):
    if max < df.loc[i, "Age"]:
        max = df.loc[i, "Age"]
    if min > df.loc[i, "Age"]:
        min = df.loc[i, "Age"]
        min_i = df.loc[i, "Age"]
print(max, min)
        
    
'''
#Number of people in each age group
for i in range(0, df.shape[0]):
    interval = 80/20
'''