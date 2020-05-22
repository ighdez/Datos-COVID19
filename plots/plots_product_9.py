# Plots product 9
# By Jose Ignacio Hernandez

# Load packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
inputfile = "../output/producto9/HospitalizadosUCIEtario_T.csv"
dat = pd.read_csv(inputfile)

# Create variables
date = dat["Grupo de edad"]
cases = dat[["<=39","40-49","50-59","60-69",">=70"]]
colsums = cases.sum(axis=1)
percentages = cases

group1 = dat["<=39"]/colsums*100
group2 = dat["40-49"]/colsums*100
group3 = dat["50-59"]/colsums*100
group4 = dat["60-69"]/colsums*100
group5 = dat[">=70"]/colsums*100

p1 = plt.bar(date, group1)
p2 = plt.bar(date, group2,bottom=group1)
p3 = plt.bar(date, group3,bottom=group1+group2)
p4 = plt.bar(date, group4,bottom=group1+group2+group3)
p5 = plt.bar(date, group5,bottom=group1+group2+group3+group4)

plt.ylabel('Casos')
plt.title('Pacientes en UCI diarios por grupo de edad')
plt.xticks(np.arange(0,len(date),len(date)-1))
plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0]), ('<=39', '40-49','50-59','60-69','>=70'))
# plt.show()
plt.savefig('uci_perc.png')