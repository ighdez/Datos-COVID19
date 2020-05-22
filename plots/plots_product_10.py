# Plots product 10
# By Jose Ignacio Hernandez

# Load packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
inputfile = "../output/producto10/FallecidosEtario_T.csv"
dat = pd.read_csv(inputfile)

# Create variables
date = dat["Grupo de edad"]
cases = dat[["<=39","40-49","50-59","60-69","70-79","80-89",">=90"]].diff()
colsums = cases.sum(axis=1)

group1 = cases["<=39"]#/colsums*100
group2 = cases["40-49"]#/colsums*100
group3 = cases["50-59"]#/colsums*100
group4 = cases["60-69"]#/colsums*100
group5 = cases["70-79"]#/colsums*100
group6 = cases["80-89"]#/colsums*100
group7 = cases[">=90"]#/colsums*100

group1 = group1.fillna(0)
group2 = group2.fillna(0)
group3 = group3.fillna(0)
group4 = group4.fillna(0)
group5 = group5.fillna(0)
group6 = group6.fillna(0)
group7 = group7.fillna(0)
# colsums = colsums.fillna(0)

p1 = plt.bar(date, group1)
p2 = plt.bar(date, group2,bottom=group1)
p3 = plt.bar(date, group3,bottom=group1+group2)
p4 = plt.bar(date, group4,bottom=group1+group2+group3)
p5 = plt.bar(date, group5,bottom=group1+group2+group3+group4)
p6 = plt.bar(date, group6,bottom=group1+group2+group3+group4+group5)
p7 = plt.bar(date, group7,bottom=group1+group2+group3+group4+group5+group6)

plt.ylabel('Casos')
plt.title('Fallecidos diarios por grupo de edad')
plt.xticks(np.arange(0,len(date),len(date)-1))
plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0]), ('<=39', '40-49','50-59','60-69','70-79','80-89','>=90'))
plt.show()
plt.savefig('fallecidos_perc.png')
