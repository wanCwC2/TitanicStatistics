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
pclass = [[0,0,0],[0,0,0]] #3Pclass. Every have victims and survivors
r_dead = [[], []] #relationship between money and life, dead
r_live = [[], []] #relationship between money and life, live

#Base figure
fig, axes = plt.subplots(2, 2) #2columns, 2rows

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
    pclass[int(df.loc[i, "Survived"])][int(df.loc[i, "Pclass"])-1] += 1
    
    #relationship between money and life
    if int(df.loc[i, "Survived"]) == 0: #Dead
        r_dead[0].append(df.loc[i, "Age"])
        r_dead[1].append(df.loc[i, "Fare"])
    elif int(df.loc[i, "Survived"]) == 1: #Live
        r_live[0].append(df.loc[i, "Age"])
        r_live[1].append(df.loc[i, "Fare"])

#Draw Male/Female figure
axes[0][0].set_yticks([0, 100, 200, 300, 400, 500, 600]) #set axis scales
axes[0][0].bar([1, 2], [male, female], tick_label=['male', 'female'])

#Draw age interval figure
axes[0][1].set_yticks([0, 20, 40, 60, 80, 100]) #set axis scales
axes[0][1].bar([i for i in range(0, 80, int(interval))], age, width = interval)

#Draw survivors/victims figure
axes[1][0].set_yticks([0, 50, 100, 150, 200, 250, 300, 350]) #set axis scales
x = [1, 2, 3] #x coordinate
width = 0.4
axes[1][0].bar(x ,pclass[0], width = width, tick_label=['PClass1', 'PClass2', 'PClass3'], label = 'Dead')
x2 = [num + width for num in x]
axes[1][0].bar(x2 ,pclass[1], width = width, label = 'Live')

#Draw the relationship between money and life
axes[1][1].set_yticks([0, 100, 200, 300, 400, 500]) #set axis scales
axes[1][1].scatter(r_dead[0], r_dead[1], marker='x', label='Dead')
axes[1][1].scatter(r_live[0], r_live[1], marker='s', label='Live')

plt.show()

#print(male, female)
#print(age, nan_total)
#print(pclass)