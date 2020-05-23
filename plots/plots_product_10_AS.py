# Plot Product 10
# By Alvaro Silva
# May, 2020

# Load Packages
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load Data

inputfile = '../output/producto10/FallecidosEtario_T.csv'

# Getting it as a panda frame.

dat = pd.read_csv(inputfile)
dat['Total'] = dat.sum(axis=1)

# Creating Color Palette

purple_pal = ["#f3edfd", "#d0b9fa", 
              "#ad85f6", "#8950f2", "#661cef", 
              "#4e0dc5", "#330980"]

pink_pal = [ '#fce4ed','#f9bdd4',
             '#f696ba','#f36fa0',
             '#f04886','#ed216c',
             '#d31159']

# Note for every Graph.

notes='Fuente: Elaboración propia en base a datos COVID-19 MinCiencia. Autores: José Ignacio Hernández y Álvaro Silva.'

# Getting data to be plotted.

toplotdta =  [dat.loc[:,'<=39'],dat.loc[:,'40-49'],
              dat.loc[:,'50-59'],dat.loc[:,'60-69'],
              dat.loc[:,'70-79'], dat.loc[:,'80-89'],
              dat.loc[:,'>=90']]
dat['Grupo de edad'] = dat['Grupo de edad'].str[5:10]

# Plotting Deaths per age-cohort.

plt.stackplot(dat.loc[:, 'Grupo de edad'],
              toplotdta, colors = pink_pal,
              labels=['$\leq 39$','$40-49$','$50-59$'
                      ,'$60-69$', '$70-79$', '$80-89$', 
                      '$\geq 90$'])

# Graph Options 

plt.ylabel('Numero Fallecidos')
plt.tick_params(labelsize=8)
plt.legend(loc='upper left')
ax = plt.axes()
my_xticks = ax.get_xticks()
plt.xticks([my_xticks[0], my_xticks[6], my_xticks[12],
            my_xticks[12], my_xticks[18], my_xticks[24],
            my_xticks[30], my_xticks[36], my_xticks[-1]])
plt.margins(0,0)
plt.xlabel(notes, fontsize=7)
plt.title('Fallecidos por Edad', fontsize = 14)

# Exporting Graph
plt.savefig('fallecidos_edad.pdf', 
            bbox_inches = 'tight',
            pad_inches = 0)
