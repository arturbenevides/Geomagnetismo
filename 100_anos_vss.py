# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 03:17:40 2017

@author: Artur Benevides
"""
"""

###############################################################################

        Objetivos do código
        
Plotar os dados referente aos 100 anos de VSS

###############################################################################

"""
#Bibliotecas importadaas

import glob
import pandas as pd
import numpy as np
import math as math
import pylab
from matplotlib import pyplot as plt
import os
##########################################################################
"""
        Armazenamento das variáveis

Cem irá armazenar o arquivo vss2.min que abriga os médias anuais calculadas com 
Os dados do observatório de vassouras
"""
cem = glob.glob('VSS2.min') 
"""
Vassouritas irá armazenar o arquivo vassouritas.txt que é referente aos dados
do modelo IGRF
"""
vassouritas = glob.glob('vassouritas.txt')
##########################################################################
#mean = np.zeros(len(dias))



'''Definindo a quantidade de dias que hoveram medidas, header=1 significa que o nome das coordenadas esta na linha 1'''
'''Definindo as variáveis para o IGRF. ( Dvas= Declinação, INCvas=INclinação
 Xvas, Yvas, Zvas componentes X,Y e Z, Fvas= intensidade do campo, Hvas= H '''
for k in range(len(vassouritas)):
    vassourita_dados = pd.read_csv(vassouritas[k], header = 1, delim_whitespace = True)
    
    Dvas= vassourita_dados['D']
    
    INCvas= vassourita_dados['Inc']
    
    Xvas= vassourita_dados['X']
    
    Yvas= vassourita_dados['Y']
    
    Zvas= vassourita_dados['Z']
    
    Fvas= vassourita_dados['F']
    
    Hvas= vassourita_dados['H']
  
'''Definindo as variáveis para os dadaos de vassouras'''  
for i in range(len(cem)):
    VSS_datos = pd.read_csv(cem[i], header = 0, delim_whitespace = True)


    year = VSS_datos['YEAR']
    ''' Na linha acima VSS_H é definida como uma das colunas de VSS_datos, a VSSH (que estava no header)'''
    D = VSS_datos['D']

    I = VSS_datos['I']
    
    D1 = np.zeros(len(D))
    
    I1 = np.empty(101)
    
    for j in range(0,len(D)):
        D1[j] = D[j]/60
    
        I1[j] = I[j]/60
    
    H = VSS_datos['H']
    
    X = VSS_datos['X']
    
    Y = VSS_datos['Y']
    
    Z = VSS_datos['Z']
    
    F = VSS_datos['F']
    
 





    "determine secular variation for components of geomagnetic field."
    '''
    a - column data
    '''

    
def secular(a):
    N = a.size
    sv = np.zeros(N)
    
    for i in range(N-1):
        sv[i+1] = a[i+1] - a[i]
    
    return sv

svD1=secular(D1)
svI=secular(I)
svF=secular(F)
svX=secular(X)
svY=secular(Y)
svZ=secular(Z)
svH=secular(H)


svDIGRF=secular(Dvas)
svINIGRF=secular(INCvas)
svFIGRF=secular(Fvas)
svHIGRF=secular(Hvas)
svXIGRF=secular(Xvas)
svYIGRF=secular(Yvas)
svZIGRF=secular(Zvas)










###############################################################

fig1 = plt.figure(figsize=(15,4))
plt.scatter(year, Z , 4, label="VSS", color='black')
plt.plot(year, Zvas,'-', label="IGRF", linestyle='solid', color='black', linewidth=2)
plt.ylabel('Z ($nT$)', fontsize=14)
plt.xlabel('Years', fontsize=14)
#plt.legend([VSS], ["VSS"])
plt.legend()
#plt.title ('Mean the magnetic field VSS 2000 ',  fontsize=16)
plt.grid(True)
plt.xticks(np.arange(1915, 2015, 10))
#pylab.ylim([15000,25000])
pylab.xlim([1915,2015])
plt.savefig('Z_1915-2015.png', bbox_inches='tight',dpi=500)
#plt.show()


###############################################################
fig1 = plt.figure(figsize=(15,4))
plt.scatter(year, H , 4, label="Vass", color='black')
plt.plot(year, Hvas,'-',label="IGRF",linestyle='solid', color='black', linewidth=2)
plt.ylabel('H ($nT$)', fontsize=14)
plt.xlabel('Years', fontsize=14)
#plt.legend([VSS], ["VSS"])
plt.legend()
#plt.title ('Mean the magnetic field VSS 2000 ',  fontsize=16)
plt.grid(True)
plt.xticks(np.arange(1915, 2015, 10))
#pylab.ylim([15000,25000])
pylab.xlim([1915,2015])
plt.savefig('H_1915-2015.png', bbox_inches='tight',dpi=500)
#plt.show()


###############################################################


fig1 = plt.figure(figsize=(15,4))
plt.scatter(year, I1 , 4, label="Vass", color='black')
plt.plot(year, INCvas,'-',label="IGRF", linestyle='solid', color='black', linewidth=2)
plt.ylabel('I ($^\circ$)', fontsize=14)
plt.xlabel('Years', fontsize=14)

plt.legend()
#plt.title ('Mean the magnetic field VSS 2000 ',  fontsize=16)
plt.grid(True)
plt.xticks(np.arange(1915, 2015, 10))
#pylab.ylim([15000,25000])
pylab.xlim([1915,2015])
plt.savefig('I_1915-2015.png', bbox_inches='tight',dpi=500)
#plt.show()


###############################################################


##########################################################
fig1 = plt.figure(figsize=(15,4))
plt.scatter(year, Y , 4, label="Vass", color='black')
plt.plot(year, Yvas,'-',label="IGRF", linestyle='solid', color='black', linewidth=2)
plt.ylabel('Y ($nT$)', fontsize=14)
plt.xlabel('Years', fontsize=14)
#plt.title ('Mean the magnetic field VSS 2000 ',  fontsize=16)
plt.grid(True)
plt.legend()
plt.xticks(np.arange(1915, 2015, 10))
#pylab.ylim([15000,25000])
pylab.xlim([1915,2015])
plt.savefig('Y_1915-2015.png', bbox_inches='tight',dpi=500)
#plt.show()


###############################################################
#time = range(len(year))
fig1 = plt.figure(figsize=(15,4))
plt.scatter(year, X , 4, label="Vass", color='black')
plt.plot(year, Xvas,'-',label="IGRF", linestyle='solid', color='black', linewidth=2)
plt.ylabel('X ($nT$)', fontsize=14)
plt.xlabel('Years', fontsize=14)
#plt.title ('Mean the magnetic field VSS 2000 ',  fontsize=16)
plt.grid(True)
plt.legend()

plt.xticks(np.arange(1915, 2015, 10))
#pylab.ylim([15000,25000])
pylab.xlim([1915,2015])
plt.savefig('X_1915-2015.png', bbox_inches='tight',dpi=500)
#plt.show()


###################################################################
#time = range(len(year))
fig1 = plt.figure(figsize=(15,4))
plt.scatter(year, F , 4, label="Vass", color='black')
plt.plot(year, Fvas,'-',label="IGRF", linestyle='solid', color='black', linewidth=2)
plt.ylabel('F ($nT$)', fontsize=14)
plt.xlabel('Years', fontsize=14)
plt.legend()
#plt.title ('Mean the magnetic field VSS 2000 ',  fontsize=16)
plt.grid(True)
plt.xticks(np.arange(1915, 2015, 10))
#pylab.ylim([15000,25000])
pylab.xlim([1915,2015])
plt.savefig('F_1915-2015.png', bbox_inches='tight',dpi=500)
#plt.show()

######################################################################3
#time = range(len(year))
fig1 = plt.figure(figsize=(15,4))
plt.scatter(year, D1 , 4, label="Vass", color='black')
plt.plot(year, Dvas,'-',label="IGRF", linestyle='solid', color='black', linewidth=2)
plt.ylabel('D ($^\circ$)', fontsize=14)
plt.xlabel('Years', fontsize=14)
plt.legend()
#plt.title ('Mean the magnetic field VSS 2000 ',  fontsize=16)
plt.grid(True)
plt.xticks(np.arange(1915, 2015, 10))
#pylab.ylim([15000,25000])
pylab.xlim([1915,2015])
plt.savefig('D_1915-2015.png', bbox_inches='tight',dpi=500)
#plt.show()

# Eliminar los "nan" del vector mean 
    #mean_2000 = [value for value in mean if not math.isnan(value)]

#Calcula la media aritmética del año  
#MEAN_2000 = np.mean(mean_2000)
#print(MEAN_2000)
