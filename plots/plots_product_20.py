# Plots product 20
# By Jose Ignacio Hernandez

# Load packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
inputfile = "../output/producto20/NumeroVentiladores_T.csv"
dat = pd.read_csv(inputfile)

# Create variables
date = dat["Ventiladores"]
total = dat["total"]
disp = dat["disponibles"]/total*100
ocupados = dat["ocupados"]/total*100

plt.figure(figsize=(10,9))
p1 = plt.bar(date, ocupados)
p2 = plt.bar(date, disp,bottom=ocupados)

plt.ylabel('Porcentaje')
plt.title('Disponibilidad de ventiladores')
plt.xticks(np.arange(0,len(date),len(date)-1))
plt.legend((p1[0], p2[0]), ('Utilizados', 'Disponibles'))
plt.annotate('Fuente: Elaboración propia en base a datos COVID-19 MinCiencia. Autores: José Ignacio Hernández y Álvaro Silva.',
            xy=(0.25, 0), xytext=(0, 10),
            xycoords=('axes fraction', 'figure fraction'),
            textcoords='offset points',
            size=8, ha='center', va='bottom')
# plt.show()
plt.savefig('ventiladores_perc.png')