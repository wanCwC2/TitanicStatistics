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
#pclass = np.zeros(6) #3Pclass. Every have victims and survivors
#pclass = [[0, 0], [0, 0], [0, 0]]
pclass = [[0,0,0],[0,0,0]]

#Base figure
fig, axes = plt.subplots(2,2) #2rows, 2columns

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
    #pclass[1+(int(df.loc[i, "Pclass"])-1)*2+int(df.loc[i, "Survived"])-1] += 1
    #pclass[int(df.loc[i, "Pclass"])-1][int(df.loc[i, "Survived"])] += 1
    pclass[int(df.loc[i, "Survived"])][int(df.loc[i, "Pclass"])-1] += 1
    
    #Draw the relationship between money and life
    if int(df.loc[i, "Survived"]) == 0: #Dead
        axes[1][1].scatter(df.loc[i, "Age"], df.loc[i, "Fare"], c = 'orangered', marker='x', label='Dead')
    elif int(df.loc[i, "Survived"]) == 1: #Live
        axes[1][1].scatter(df.loc[i, "Age"], df.loc[i, "Fare"], c = 'steelblue', marker='s', label='Live')

#Draw Male/Female figure
axes[0][0].bar([1, 2], [male, female], tick_label=['male', 'female'])

#Draw age interval figure
axes[0][1].bar([i for i in range(0, 80, int(interval))], age)

#Draw survivors/victims figure
x = [1, 2, 3]
width = 0.4
axes[1][0].bar(x ,pclass[0], width = width, tick_label=['PClass1', 'PClass2', 'PClass3'], label = 'Dead')
x2 = [num + width for num in x]
axes[1][0].bar(x2 ,pclass[1], width = width, label = 'Live')

plt.show()


#print(male, female)
#print(age, nan_total)
#print(pclass)
