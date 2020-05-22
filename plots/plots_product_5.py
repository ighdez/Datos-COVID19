# Plots product 20
# By Jose Ignacio Hernandez

# Load packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
inputfile = "../output/producto5/TotalesNacionales_T.csv"
dat = pd.read_csv(inputfile)

# Confirmados

# Create variables
date = dat["Fecha"]
new_sympt = dat["Casos nuevos con sintomas"]
new_nosympt = dat["Casos nuevos sin sintomas"]
new_nosympt = new_nosympt.fillna(0)

plt.figure(figsize=(10,9))
p1 = plt.bar(date, new_sympt)
p2 = plt.bar(date, new_nosympt,bottom=new_sympt)

plt.ylabel('Casos totales')
plt.title('Casos confirmados nacionales')
plt.xticks(np.arange(0,len(date),5),rotation=45,fontsize=8)
plt.legend((p1[0], p2[0]), ('Con sintomas', 'Sin sintomas'))
plt.annotate('Fuente: Elaboración propia en base a datos COVID-19 MinCiencia. Autores: José Ignacio Hernández y Álvaro Silva.',
            xy=(0.25, 0), xytext=(0, 10),
            xycoords=('axes fraction', 'figure fraction'),
            textcoords='offset points',
            size=8, ha='center', va='bottom')
# plt.show()
plt.savefig('confirmados.png')

# Fallecidos
# Create variables
dead = dat["Fallecidos"].diff()
dead = dead.fillna(0)

plt.figure(figsize=(10,9))
p1 = plt.bar(date, dead)

plt.ylabel('Casos totales')
plt.title('Fallecidos diarios')
plt.xticks(np.arange(0,len(date),5),rotation=45,fontsize=8)
plt.annotate('Fuente: Elaboración propia en base a datos COVID-19 MinCiencia. Autores: José Ignacio Hernández y Álvaro Silva.',
            xy=(0.25, 0), xytext=(0, 10),
            xycoords=('axes fraction', 'figure fraction'),
            textcoords='offset points',
            size=8, ha='center', va='bottom')
# plt.show()
plt.savefig('fallecidos_diarios.png')
