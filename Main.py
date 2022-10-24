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

'''
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
age = np.zeros(20)
interval = 80/20
nan_total = 0 #How many people are unknown
for i in range(0, df.shape[0]):
    if np.isnan(df.loc[i, "Age"]):
        nan_total += 1
    else:
        if int(df.loc[i, "Age"]/interval) == 0:
            age[int(df.loc[i, "Age"]/interval)] += 1
        else:
            if df.loc[i, "Age"]%interval == 0:
                age[int(df.loc[i, "Age"]/interval)-1] += 1
            else:
                age[int(df.loc[i, "Age"]/interval)] += 1

print(age, nan_total)

#Number of survivors and victims in each Pclass
pclass = [[0, 0], [0, 0], [0, 0]] #3Pclass. Every have victims and survivors
for i in range(0, df.shape[0]):
    pclass[int(df.loc[i, "Pclass"])-1][int(df.loc[i, "Survived"])] += 1
print(pclass)
