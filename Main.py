#Example
import matplotlib.pyplot as plt
import matplotlib.style
import pandas as pd
import numpy as np
matplotlib.style.use('ggplot')
df = pd.read_csv('http://bit.ly/kaggletrain')

male = 0 #total number of men
female = 0 #total number of women
age = np.zeros(20)
interval = 80/20 #age interval
nan_total = 0 #How many people are unknown
pclass = [[0, 0], [0, 0], [0, 0]] #3Pclass. Every have victims and survivors

#Base figure
fig, axes = plt.subplots(2, 2)
plt.show()

for i in range(0, df.shape[0]):
    
    #Male/Female total separately
    if df.loc[i, "Sex"]  == "male":
        male += 1
    if df.loc[i, "Sex"] == "female":
        female += 1
        
    #Number of people in each age group
    if np.isnan(df.loc[i, "Age"]):
        nan_total += 1
    else:
        if df.loc[i, "Age"]%interval == 0:
            age[int(df.loc[i, "Age"]/interval)-1] += 1
        else:
            age[int(df.loc[i, "Age"]/interval)] += 1
            
    #Number of survivors and victims in each Pclass
    pclass[int(df.loc[i, "Pclass"])-1][int(df.loc[i, "Survived"])] += 1

#print(male, female)
#print(age, nan_total)
#print(pclass)
