# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 22:19:58 2017  (0)
@Edwin Leonardo 

Modified on Wed Aug 23 22:00:00 2017 (1)
@Artur Benevides


Grupo da disciplina de Geomagnetismo 

Integrantes:
	Artur Benevides
	Edwin Leonardo   (Consultor)
	Israelli Rodrigo
	Katia Jabinschek (Orientadora)
	Rodrigo Melhorato
	Vitor Silveira
	



###################################################################################
##						Objetivos do Código:						   #	
##															   #	
##	Cálcular médias horárias, mensais e anuais para components do campo magnético #
##	utilizando dados do observatório de Vassouras a partir do INTERMAGNET         #
################################################################################### 
"""

'''
Importação das bibliotecas utilizadas pelo programa
'''
import glob
import pandas as pd
import numpy as np
import math as math
import pylab
from matplotlib import pyplot as plt
import os


'''
    Esta parte do código utiliza os dados do ano 2000 e calcula F(x,y,z)
'''
# Entre no diretório dos dados do ano 2000 antes de rodar o programa abaixo
dias = glob.glob('*.min') 
'''Lê todos os arquivos com final .mim'''
mean = np.zeros(len(dias))
'''Definindo a quantidade de dias que hoveram medidas'''

for i in range(len(dias)):
    VSS_datos = pd.read_csv(dias[i], header = 25, delim_whitespace = True)
    '''i no range de (len(dias)) garante que não façamos media com dias que não tiveram medidas'''
    '''Header=25  define que na linha 25 está o nome das colunas.. as colunas serão reunidas em VSS_datos
    Para cada arquivo .min teremos um arquivo dias, por exemplo dias[1] dias[2]'''

    VSS_H = VSS_datos['VSSH']
    ''' Na linha acima VSS_H é definida como uma das colunas de VSS_datos, a VSSH (que estava no header)'''
    VSS_Z = VSS_datos['VSSZ']
    F = np.empty(1440)
    '''Acima Definimos F como um vetor de zeros com tamanho de 1440 (equivalente a 60min*24h)
    a baixo o cálculo de F a partir das componentes do Campo principal.
    '''
    for j in range(1440):
        F[j] =  np.sqrt((VSS_H[j]**2) + (VSS_Z[j]**2))    
        F1 = F[F<30000]
        mean_p = np.mean(F1)
    mean[i] = mean_p



time = range(len(dias))
fig = plt.figure(figsize=(15,4))
plt.plot(time,mean,'-',color='b')
plt.ylabel('Mean Magnetic Field', fontsize=14)
plt.xlabel('Day', fontsize=14)
plt.title ('Mean the magnetic field VSS 2000 ',  fontsize=16)
plt.grid(True)
#plt.xticks(np.arange(1, 32, 1))
#pylab.ylim([23200,24000])
pylab.xlim([0,370])
#plt.savefig('dst_1303.png', bbox_inches='tight',dpi=500)
plt.show()

# Eliminar los "nan" del vector mean 
mean_2000 = [value for value in mean if not math.isnan(value)]

#Calcula la media aritmética del año  
MEAN_2000 = np.mean(mean_2000)
print(MEAN_2000)


'''
    Lee la carpeta de datos del 2001 y calcula F(x,y,z)
'''
# colocar la dir. de la carpeta 2001
dias = glob.glob('*.min')
mean = np.zeros(len(dias))


for i in range(len(dias)):
    VSS_datos = pd.read_csv(dias[i], header = 25, delim_whitespace = True)
    VSS_H = VSS_datos['VSSH']
    VSS_Z = VSS_datos['VSSZ']
    F = np.empty(1440)
    for j in range(1440):
        F[j] =  np.sqrt((VSS_H[j]**2) + (VSS_Z[j]**2))    
        F1 = F[F<30000]
        mean_p = np.mean(F1)
    mean[i] = mean_p



time = range(len(dias))
fig = plt.figure(figsize=(15,4))
plt.plot(time,mean,'-',color='b')
plt.ylabel('Mean Magnetic Field', fontsize=14)
plt.xlabel('Day', fontsize=14)
plt.title ('Mean the magnetic field VSS 2001 ',  fontsize=16)
plt.grid(True)
#plt.xticks(np.arange(1, 32, 1))
#pylab.ylim([23200,24000])
pylab.xlim([0,370])
#plt.savefig('dst_1303.png', bbox_inches='tight',dpi=500)
plt.show()

# Eliminar los "nan" del vector mean 
mean_2001 = [value for value in mean if not math.isnan(value)]

#Calcula la media aritmética del año  
MEAN_2001 = np.mean(mean_2001)
print(MEAN_2001)


'''
    Lee la carpeta de datos del 2002 y calcula F(x,y,z)
'''
# colocar la dir. de la carpeta 2002
dias = glob.glob('*.min')
mean = np.zeros(len(dias))


for i in range(len(dias)):
    VSS_datos = pd.read_csv(dias[i], header = 25, delim_whitespace = True)
    VSS_H = VSS_datos['VSSH']
    VSS_Z = VSS_datos['VSSZ']
    F = np.empty(1440)
    for j in range(1440):
        F[j] =  np.sqrt((VSS_H[j]**2) + (VSS_Z[j]**2))    
        F1 = F[F<30000]
        mean_p = np.mean(F1)
    mean[i] = mean_p



time = range(len(dias))
fig = plt.figure(figsize=(15,4))
plt.plot(time,mean,'-',color='b')
plt.ylabel('Mean Magnetic Field', fontsize=14)
plt.xlabel('Day', fontsize=14)
plt.title ('Mean the magnetic field VSS 2002',  fontsize=16)
plt.grid(True)
#plt.xticks(np.arange(1, 32, 1))
#pylab.ylim([23200,24000])
pylab.xlim([0,370])
#plt.savefig('dst_1303.png', bbox_inches='tight',dpi=500)
plt.show()

# Eliminar los "nan" del vector mean 
mean_2002 = [value for value in mean if not math.isnan(value)]

#Calcula la media aritmética del año  
MEAN_2002 = np.mean(mean_2002)
print(MEAN_2002)

'''
    Lee la carpeta de datos del 2003 y calcula F(h,z)
'''
# colocar la dir. de la carpeta 2003
dias = glob.glob('*.min')
mean = np.zeros(len(dias))


for i in range(len(dias)):
    VSS_datos = pd.read_csv(dias[i], header = 25, delim_whitespace = True)
    VSS_H = VSS_datos['VSSH']
    VSS_Z = VSS_datos['VSSZ']
    F = np.empty(1440)
    for j in range(1440):
        F[j] =  np.sqrt((VSS_H[j]**2) + (VSS_Z[j]**2))    
        F1 = F[F<30000]
        mean_p = np.mean(F1)
    mean[i] = mean_p



time = range(len(dias))
fig = plt.figure(figsize=(15,4))
plt.plot(time,mean,'-',color='b')
plt.ylabel('Mean Magnetic Field', fontsize=14)
plt.xlabel('Day', fontsize=14)
plt.title ('Mean the magnetic field VSS 2003',  fontsize=16)
plt.grid(True)
#plt.xticks(np.arange(1, 32, 1))
#pylab.ylim([23200,24000])
pylab.xlim([0,370])
#plt.savefig('dst_1303.png', bbox_inches='tight',dpi=500)
plt.show()

# Eliminar los "nan" del vector mean 
mean_2003 = [value for value in mean if not math.isnan(value)]

#Calcula la media aritmética del año  
MEAN_2003 = np.mean(mean_2003)
print(MEAN_2003)

'''
    Lee la carpeta de datos del 2004 y calcula F(x,y,z)
'''
# colocar la dir. de la carpeta 2004
dias = glob.glob('*.min')
mean = np.zeros(len(dias))


for i in range(len(dias)):
    VSS_datos = pd.read_csv(dias[i], header = 25, delim_whitespace = True)
    VSS_X = VSS_datos['VSSX']
    VSS_Y = VSS_datos['VSSY']
    VSS_Z = VSS_datos['VSSZ']
    F = np.empty(1440)
    for j in range(1440):
        F[j] =  np.sqrt((VSS_X[j]**2) + (VSS_Y[j]**2) + (VSS_Z[j]**2))    
        F1 = F[F<30000]
        mean_p = np.mean(F1)
    mean[i] = mean_p



time = range(len(dias))
fig = plt.figure(figsize=(15,4))
plt.plot(time,mean,'-',color='b')
plt.ylabel('Mean Magnetic Field', fontsize=14)
plt.xlabel('Day', fontsize=14)
plt.title ('Mean the magnetic field VSS 2004 ',  fontsize=16)
plt.grid(True)
#plt.xticks(np.arange(1, 32, 1))
#pylab.ylim([23200,24000])
pylab.xlim([0,370])
#plt.savefig('dst_1303.png', bbox_inches='tight',dpi=500)
plt.show()

# Eliminar los "nan" del vector mean 
mean_2004 = [value for value in mean if not math.isnan(value)]

#Calcula la media aritmética del año  
MEAN_2004 = np.mean(mean_2004)
print(MEAN_2004)

'''
    Lee la carpeta de datos del 2005 y calcula F(x,y,z)
'''
dias = glob.glob('*.min')
mean = np.zeros(len(dias))
for i in range(len(dias)):
    VSS_datos = pd.read_csv(dias[i], header = 25, delim_whitespace = True)
    VSS_X = VSS_datos['VSSX']
    VSS_Y = VSS_datos['VSSY']
    VSS_Z = VSS_datos['VSSZ']
    F = np.empty(1440)
    for j in range(1440):
        F[j] =  np.sqrt((VSS_X[j]**2) + (VSS_Y[j]**2) + (VSS_Z[j]**2))    
        F1 = F[F<30000]
        mean_p = np.mean(F1)
    mean[i] = mean_p

time = range(len(dias))
fig = plt.figure(figsize=(15,4))
plt.plot(time,mean,'-',color='b')
plt.ylabel('Mean Magnetic Field', fontsize=14)
plt.xlabel('Day', fontsize=14)
plt.title ('Mean the magnetic field VSS 2005 ',  fontsize=16)
plt.grid(True)
#plt.xticks(np.arange(1, 32, 1))
#pylab.ylim([23200,24000])
pylab.xlim([0,370])
#plt.savefig('dst_1303.png', bbox_inches='tight',dpi=500)
plt.show()

# Eliminar los "nan" del vector mean 
#mean_2005 = [value for value in mean if not math.isnan(value)]

#Calcula la media aritmética del año  
MEAN_2005 = np.mean(mean)
print(MEAN_2005)


'''
    Lee la carpeta de datos del 2006 y calcula F(x,y,z)
'''
dias = glob.glob('*.min')
mean = np.zeros(len(dias))
for i in range(len(dias)):
    VSS_datos = pd.read_csv(dias[i], header = 25, delim_whitespace = True)
    VSS_X = VSS_datos['VSSX']
    VSS_Y = VSS_datos['VSSY']
    VSS_Z = VSS_datos['VSSZ']
    F = np.empty(1440)
    for j in range(1440):
        F[j] =  np.sqrt((VSS_X[j]**2) + (VSS_Y[j]**2) + (VSS_Z[j]**2))    
        F1 = F[F<30000]
        mean_p = np.mean(F1)
    mean[i] = mean_p

time = range(len(dias))
fig = plt.figure(figsize=(15,4))
plt.plot(time,mean,'-',color='b')
plt.ylabel('Mean Magnetic Field', fontsize=14)
plt.xlabel('Day', fontsize=14)
plt.title ('Mean the magnetic field VSS 2006 ',  fontsize=16)
plt.grid(True)
#plt.xticks(np.arange(1, 32, 1))
#pylab.ylim([23200,24000])
pylab.xlim([0,370])
#plt.savefig('dst_1303.png', bbox_inches='tight',dpi=500)
plt.show()

# Eliminar los "nan" del vector mean 
mean_2006 = [value for value in mean if not math.isnan(value)]

#Calcula la media aritmética del año  
MEAN_2006 = np.mean(mean_2006)
print(MEAN_2006)



'''
    Lee la carpeta de datos del 2007 y calcula F(x,y,z)
'''
dias = glob.glob('*.min')
mean = np.zeros(len(dias))
for i in range(len(dias)):
    VSS_datos = pd.read_csv(dias[i], header = 25, delim_whitespace = True)
    VSS_X = VSS_datos['VSSX']
    VSS_Y = VSS_datos['VSSY']
    VSS_Z = VSS_datos['VSSZ']
    F = np.empty(1440)
    for j in range(1440):
        F[j] =  np.sqrt((VSS_X[j]**2) + (VSS_Y[j]**2) + (VSS_Z[j]**2))    
        F1 = F[F<30000]
        mean_p = np.mean(F1)
    mean[i] = mean_p

time = range(len(dias))
fig = plt.figure(figsize=(15,4))
plt.plot(time,mean,'-',color='b')
plt.ylabel('Mean Magnetic Field', fontsize=14)
plt.xlabel('Day', fontsize=14)
plt.title ('Mean the magnetic field VSS 2007 ',  fontsize=16)
plt.grid(True)
#plt.xticks(np.arange(1, 32, 1))
#pylab.ylim([23200,24000])
pylab.xlim([0,370])
#plt.savefig('dst_1303.png', bbox_inches='tight',dpi=500)
plt.show()

# Eliminar los "nan" del vector mean 
mean_2007 = [value for value in mean if not math.isnan(value)]

#Calcula la media aritmética del año  
MEAN_2007 = np.mean(mean_2007)
print(MEAN_2007)


'''
    Lee la carpeta de datos del 2008 y calcula F(x,y,z)
'''
dias = glob.glob('*.min')
mean = np.zeros(len(dias))
for i in range(len(dias)):
    VSS_datos = pd.read_csv(dias[i], header = 25, delim_whitespace = True)
    VSS_X = VSS_datos['VSSX']
    VSS_Y = VSS_datos['VSSY']
    VSS_Z = VSS_datos['VSSZ']
    F = np.empty(1440)
    for j in range(1440):
        F[j] =  np.sqrt((VSS_X[j]**2) + (VSS_Y[j]**2) + (VSS_Z[j]**2))    
        F1 = F[F<30000]
        mean_p = np.mean(F1)
    mean[i] = mean_p

time = range(len(dias))
fig = plt.figure(figsize=(15,4))
plt.plot(time,mean,'-',color='b')
plt.ylabel('Mean Magnetic Field', fontsize=14)
plt.xlabel('Day', fontsize=14)
plt.title ('Mean the magnetic field VSS 2008 ',  fontsize=16)
plt.grid(True)
#plt.xticks(np.arange(1, 32, 1))
#pylab.ylim([23200,24000])
pylab.xlim([0,370])
#plt.savefig('dst_1303.png', bbox_inches='tight',dpi=500)
plt.show()

# Eliminar los "nan" del vector mean 
mean_2008 = [value for value in mean if not math.isnan(value)]

#Calcula la media aritmética del año  
MEAN_2008 = np.mean(mean_2008)
print(MEAN_2008)

'''
    Lee la carpeta de datos del 2009 y calcula F(x,y,z)
'''
dias = glob.glob('*.min')
mean = np.zeros(len(dias))
for i in range(len(dias)):
    VSS_datos = pd.read_csv(dias[i], header = 25, delim_whitespace = True)
    VSS_X = VSS_datos['VSSX']
    VSS_Y = VSS_datos['VSSY']
    VSS_Z = VSS_datos['VSSZ']
    F = np.empty(1440)
    for j in range(1440):
        F[j] =  np.sqrt((VSS_X[j]**2) + (VSS_Y[j]**2) + (VSS_Z[j]**2))    
        F1 = F[F<30000]
        mean_p = np.mean(F1)
    mean[i] = mean_p

time = range(len(dias))

fig = plt.figure(figsize=(15,4))
plt.plot(time,mean,'-',color='b')
plt.ylabel('Mean Magnetic Field', fontsize=14)
plt.xlabel('Day', fontsize=14)
plt.title ('Mean the magnetic field VSS 2009 ',  fontsize=16)
plt.grid(True)
#plt.xticks(np.arange(1, 32, 1))
#pylab.ylim([23200,24000])
pylab.xlim([0,370])
#plt.savefig('dst_1303.png', bbox_inches='tight',dpi=500)
plt.show()

# Eliminar los "nan" del vector mean 
mean_2009 = [value for value in mean if not math.isnan(value)]

#Calcula la media aritmética del año  
MEAN_2009 = np.mean(mean_2009)
print(MEAN_2009)


'''
    Lee la carpeta de datos del 2010 y calcula F(x,y,z)
'''
dias = glob.glob('*.min')
meanf = np.zeros(len(dias))
meand = np.zeros(len(dias))
meanx = np.zeros(len(dias))
meany = np.zeros(len(dias))
meanz = np.zeros(len(dias))
meanh = np.zeros(len(dias))
meani = np.zeros(len(dias))

for i in range(len(dias)):
    VSS_datos = pd.read_csv(dias[i], header = 24, delim_whitespace = True)
    VSS_X = VSS_datos['VSSX']
    VSS_Y = VSS_datos['VSSY']
    VSS_Z = VSS_datos['VSSZ']
    F = np.empty(1440)
    D = np.empty(1440)
    H = np.empty(1440)
    I = np.empty(1440)
    VSS_X1 = np.empty(1440)
    VSS_Y1 = np.empty(1440)
    VSS_Z1 = np.empty(1440)
    

    for j in range(1440):
        
        VSS_X1[j]= VSS_X[j]
        
        VSS_Y1[j]= VSS_Y[j]
        
        VSS_Z1[j]= VSS_Z[j]
        
        X =VSS_X1[VSS_X1>0] # condição de NAN
                            
        Y = VSS_Y1[VSS_Y1<0] # Condição de NAN
         
        Z = VSS_Z1[VSS_Z1<0] # Condição de NAN
        
        mean_px = np.mean(X)
        mean_py = np.mean(Y)
        mean_pz = np.mean(Z)
        
        F[j] =  np.sqrt((VSS_X[j]**2) + (VSS_Y[j]**2) + (VSS_Z[j]**2))    
        F1 = F[F<30000] # Condição para F nao pegar um not a number
        mean_pf = np.mean(F1)
    
        D[j] = (np.arctan(VSS_Y[j]/VSS_X[j]))*3600
        D1 = D[D<0] # condição para NAN
       
        mean_pd = np.mean(D1)
    
        H[j] = np.sqrt((VSS_X[j]**2) + (VSS_Y[j]**2))
        
        H1 = H[H<30000] # CONDIÇÃO DE nan
        
        mean_ph = np.mean(H1)
        
        I[j] = (np.arctan(VSS_Z[j]/H[j]))*3600
        
        I1 = I[I<0]
        
        mean_pi = np.mean(I1) 
        

        
    meanx[i] = mean_px
    meany[i] = mean_py
    meanz[i] = mean_pz
    meanf[i] = mean_pf
    meand[i] = mean_pd
    meanh[i] = mean_ph     
    meani[i] = mean_pi  

         
##########################################################################
#time = range(len(dias))
#fig = plt.figure(figsize=(15,4))
#plt.plot(time,meanf,'-',color='b')
#plt.ylabel('Mean Magnetic Field', fontsize=14)
#plt.xlabel('Day', fontsize=14)
#plt.title ('Mean the magnetic field VSS 2010 ',  fontsize=16)
#plt.grid(True)
#plt.xticks(np.arange(1, 32, 1))
#pylab.ylim([23200,24000])
#pylab.xlim([0,370])
#plt.savefig('dst_1303.png', bbox_inches='tight',dpi=500)
#plt.show()
##########################################################################

# Eliminar los "nan" del vector mean 

meanx_2010 = [value for value in meanx if not math.isnan(value)]
meany_2010 = [value for value in meany if not math.isnan(value)]
meanz_2010 = [value for value in meanz if not math.isnan(value)]
meanf_2010 = [value for value in meanf if not math.isnan(value)]
meand_2010 = [value for value in meand if not math.isnan(value)]
meanh_2010 = [value for value in meanh if not math.isnan(value)]
meani_2010 = [value for value in meani if not math.isnan(value)]

#Calcula la media aritmética del año  
MEAN_X_2010 = np.mean(meanx_2010)
MEAN_Y_2010 = np.mean(meany_2010)
MEAN_Z_2010 = np.mean(meanz_2010)
MEAN_F_2010 = np.mean(meanf_2010)
MEAN_D_2010 = np.mean(meand_2010)
MEAN_H_2010 = np.mean(meanh_2010)
MEAN_I_2010 = np.mean(meani_2010)

print(MEAN_X_2010)
print(MEAN_Y_2010)
print(MEAN_Z_2010)
print(MEAN_F_2010)
print(MEAN_D_2010)
print(MEAN_H_2010)
print(MEAN_I_2010)

'''
    Lee la carpeta de datos del 2011 y calcula F(x,y,z)
'''
dias = glob.glob('*.min')
meanf = np.zeros(len(dias))
meand = np.zeros(len(dias))
meanx = np.zeros(len(dias))
meany = np.zeros(len(dias))
meanz = np.zeros(len(dias))
meanh = np.zeros(len(dias))
meani = np.zeros(len(dias))
for i in range(len(dias)):
    VSS_datos = pd.read_csv(dias[i], header = 24, delim_whitespace = True)
    VSS_X = VSS_datos['VSSX']
    VSS_Y = VSS_datos['VSSY']
    VSS_Z = VSS_datos['VSSZ']
    F = np.empty(1440)
    D = np.empty(1440)
    H = np.empty(1440)
    I = np.empty(1440)
    VSS_X1 = np.empty(1440)
    VSS_Y1 = np.empty(1440)
    VSS_Z1 = np.empty(1440)
    
    for j in range(1440):
        VSS_X1[j]= VSS_X[j]
        
        VSS_Y1[j]= VSS_Y[j]
        
        VSS_Z1[j]= VSS_Z[j]
        
        X =VSS_X1[VSS_X1>0] # condição de NAN
                            
        Y = VSS_Y1[VSS_Y1<0] # Condição de NAN
         
        Z = VSS_Z1[VSS_Z1<0] # Condição de NAN
        
        mean_px = np.mean(X)
        mean_py = np.mean(Y)
        mean_pz = np.mean(Z)
        
        F[j] =  np.sqrt((VSS_X[j]**2) + (VSS_Y[j]**2) + (VSS_Z[j]**2))    
        F1 = F[F<30000] # Condição para F nao pegar um not a number
        mean_pf = np.mean(F1)
    
        D[j] = np.arctan(VSS_Y[j]/VSS_X[j])
        D1 = D[D<0] # condição para NAN
       
        mean_pd = np.mean(D1)
    
        H[j] = np.sqrt((VSS_X[j]**2) + (VSS_Y[j]**2))
        
        H1 = H[H<30000] # CONDIÇÃO DE nan
        
        mean_ph = np.mean(H1)
        
        I[j] = np.arctan(VSS_Z[j]/H[j])
        
        I1 = I[I<0]
        
        mean_pi = np.mean(I1) 
        
    
    meanx[i] = mean_px
    meany[i] = mean_py
    meanz[i] = mean_pz
    meanf[i] = mean_pf
    meand[i] = mean_pd
    meanh[i] = mean_ph     
    meani[i] = mean_pi

# Eliminar los "nan" del vector mean 
meanx_2011 = [value for value in meanx if not math.isnan(value)]
meany_2011 = [value for value in meany if not math.isnan(value)]
meanz_2011 = [value for value in meanz if not math.isnan(value)]
meanf_2011 = [value for value in meanf if not math.isnan(value)]
meand_2011 = [value for value in meand if not math.isnan(value)]
meanh_2011 = [value for value in meanh if not math.isnan(value)]
meani_2011 = [value for value in meani if not math.isnan(value)]

#Calcula la media aritmética del año  
MEAN_X_2011 = np.mean(meanx_2011)
MEAN_Y_2011 = np.mean(meany_2011)
MEAN_Z_2011 = np.mean(meanz_2011)
MEAN_F_2011 = np.mean(meanf_2011)
MEAN_D_2011 = np.mean(meand_2011)
MEAN_H_2011 = np.mean(meanh_2011)
MEAN_I_2011 = np.mean(meani_2011)

print(MEAN_X_2011)
print(MEAN_Y_2011)
print(MEAN_Z_2011)
print(MEAN_F_2011)
print(MEAN_D_2011)
print(MEAN_H_2011)
print(MEAN_I_2011)



'''
    Lee la carpeta de datos del 2012 y calcula F(h,z)
'''
dias = glob.glob('*.min')
#
meanf = np.zeros(len(dias))
meand = np.zeros(len(dias))
meanx = np.zeros(len(dias))
meany = np.zeros(len(dias))
meanz = np.zeros(len(dias))
meanh = np.zeros(len(dias))
meani = np.zeros(len(dias))

##

for i in range(len(dias)):
    VSS_datos = pd.read_csv(dias[i], header = 18, delim_whitespace = True)
    VSS_H = VSS_datos['VSSH']
    VSS_D = VSS_datos['VSSD']
    VSS_Z = VSS_datos['VSSZ']
    F = np.empty(1440)
    VSS_D1 = np.empty(1440)
    VSS_H1 = np.empty(1440)
    I = np.zeros(1440)
    X = np.empty(1440)
    Y = np.empty(1440)
    VSS_Z1 = np.empty(1440)
    a=np.empty(1440)
    
    for j in range(1440):
               
        VSS_D1[j]= VSS_D[j]
        
        D1 = VSS_D1[VSS_D1<99999] # condição para NAN
       
        mean_pd = np.mean(D1)
        
        ##
        VSS_H1[j]= VSS_H[j]
        
        H1 = VSS_H1[VSS_H1<99999] # CONDIÇÃO DE nan
        
        mean_ph = np.mean(H1)
        
        
        VSS_Z1[j]= VSS_Z[j]

        Z = VSS_Z1[VSS_Z1<0] # Condição de NAN

        mean_pz = np.mean(Z)
        
                
        X[j] = VSS_H[j]*(np.cos(VSS_D1[j]/3600))
        
        X1 =X [X<90000] # condição de NAN
        
        mean_px = np.mean(X1)
             
        Y[j] = VSS_H[j]*np.sin(VSS_D[j]/3600)
                
        Y1 = Y[Y<0] # Condição de NAN
         

        mean_py = np.mean(Y1)
  
        
        F[j] =  np.sqrt((VSS_H[j]**2) + (VSS_Z[j]**2))    
        F1 = F[F<30000] # Condição para F nao pegar um not a number
        
        mean_pf = np.mean(F1)
    
  
        

        
        I[j] = (np.arctan(VSS_Z[j]/VSS_H[j])*3600)
        
        I1 = I[I<0]
        
        mean_pi = np.mean(I1) 
    
    meanx[i] = mean_px
    meany[i] = mean_py
    meanz[i] = mean_pz
    meanf[i] = mean_pf
    meand[i] = mean_pd
    meanh[i] = mean_ph     
    meani[i] = mean_pi        
        
# Eliminar los "nan" del vector mean 
meanx_2012 = [value for value in meanx if not math.isnan(value)]
meany_2012 = [value for value in meany if not math.isnan(value)]
meanz_2012 = [value for value in meanz if not math.isnan(value)]
meanf_2012 = [value for value in meanf if not math.isnan(value)]
meand_2012 = [value for value in meand if not math.isnan(value)]
meanh_2012 = [value for value in meanh if not math.isnan(value)]
meani_2012 = [value for value in meani if not math.isnan(value)]

#Calcula la media aritmética del año  

MEAN_X_2012 = np.mean(meanx_2012)
MEAN_Y_2012 = np.mean(meany_2012)
MEAN_Z_2012 = np.mean(meanz_2012)
MEAN_F_2012 = np.mean(meanf_2012)
MEAN_D_2012 = np.mean(meand_2012)
MEAN_H_2012 = np.mean(meanh_2012)
MEAN_I_2012 = np.mean(meani_2012)

#

print('X = ',MEAN_X_2012)
print('Y = ',MEAN_Y_2012)
print('Z = ',MEAN_Z_2012)
print('F = ',MEAN_F_2012)
print('D = ',MEAN_D_2012)
print('H = ',MEAN_H_2012)
print('I = ',MEAN_I_2012)



'''
    Lee la carpeta de datos del 2013 y calcula F(x,y,z)
'''


dias = glob.glob('*.min')
meanf = np.zeros(len(dias))
meand = np.zeros(len(dias))
meanx = np.zeros(len(dias))
meany = np.zeros(len(dias))
meanz = np.zeros(len(dias))
meanh = np.zeros(len(dias))
meani = np.zeros(len(dias))

for i in range(len(dias)):
    VSS_datos = pd.read_csv(dias[i], header = 18, delim_whitespace = True)
      
    VSS_X = VSS_datos['VSSX']
    VSS_Y = VSS_datos['VSSY']
    VSS_Z = VSS_datos['VSSZ']
    F = np.empty(1440)
    D = np.empty(1440)
    H = np.empty(1440)
    I = np.empty(1440)
    VSS_X1 = np.empty(1440)
    VSS_Y1 = np.empty(1440)
    VSS_Z1 = np.empty(1440)
    
    for j in range(1440):
        VSS_X1[j]= VSS_X[j]
        
        VSS_Y1[j]= VSS_Y[j]
        
        VSS_Z1[j]= VSS_Z[j]
        
        X =VSS_X1[VSS_X1>0] # condição de NAN
                            
        Y = VSS_Y1[VSS_Y1<0] # Condição de NAN
         
        Z = VSS_Z1[VSS_Z1<0] # Condição de NAN
        
        mean_px = np.mean(X)
        mean_py = np.mean(Y)
        mean_pz = np.mean(Z)
        
        F[j] =  np.sqrt((VSS_X[j]**2) + (VSS_Y[j]**2) + (VSS_Z[j]**2))    
        F1 = F[F<30000] # Condição para F nao pegar um not a number
        mean_pf = np.mean(F1)
    
        D[j] = np.arctan(VSS_Y[j]/VSS_X[j])
        D1 = D[D<0] # condição para NAN
       
        mean_pd = np.mean(D1)
    
        H[j] = np.sqrt((VSS_X[j]**2) + (VSS_Y[j]**2))
        
        H1 = H[H<30000] # CONDIÇÃO DE nan
        
        mean_ph = np.mean(H1)
        
        I[j] = np.arctan(VSS_Z[j]/H[j])
        
        I1 = I[I<0]
        
        mean_pi = np.mean(I1) 
        
    
    meanx[i] = mean_px
    meany[i] = mean_py
    meanz[i] = mean_pz
    meanf[i] = mean_pf
    meand[i] = mean_pd
    meanh[i] = mean_ph     
    meani[i] = mean_pi

# Eliminar los "nan" del vector mean 
meanx_2013 = [value for value in meanx if not math.isnan(value)]
meany_2013 = [value for value in meany if not math.isnan(value)]
meanz_2013 = [value for value in meanz if not math.isnan(value)]
meanf_2013 = [value for value in meanf if not math.isnan(value)]
meand_2013 = [value for value in meand if not math.isnan(value)]
meanh_2013 = [value for value in meanh if not math.isnan(value)]
meani_2013 = [value for value in meani if not math.isnan(value)]

#Calcula la media aritmética del año  
MEAN_X_2013 = np.mean(meanx_2013)
MEAN_Y_2013 = np.mean(meany_2013)
MEAN_Z_2013 = np.mean(meanz_2013)
MEAN_F_2013 = np.mean(meanf_2013)
MEAN_D_2013 = np.mean(meand_2013)
MEAN_H_2013 = np.mean(meanh_2013)
MEAN_I_2013 = np.mean(meani_2013)

print(MEAN_X_2013)
print(MEAN_Y_2013)
print(MEAN_Z_2013)
print(MEAN_F_2013)
print(MEAN_D_2013)
print(MEAN_H_2013)
print(MEAN_I_2013)









'''
    Lee la carpeta de datos del 2014 y calcula F(x,y,z)
'''


dias = glob.glob('*.min')
meanf = np.zeros(len(dias))
meand = np.zeros(len(dias))
meanx = np.zeros(len(dias))
meany = np.zeros(len(dias))
meanz = np.zeros(len(dias))
meanh = np.zeros(len(dias))
meani = np.zeros(len(dias))
for i in range(len(dias)):
    if i < 262:
        VSS_datos = pd.read_csv(dias[i], header = 18, delim_whitespace = True)
        VSS_X = VSS_datos['VSSX']
        VSS_Y = VSS_datos['VSSY']
        VSS_Z = VSS_datos['VSSZ']
        F = np.empty(1440)
        D = np.empty(1440)
        H = np.empty(1440)
        I = np.empty(1440)
        VSS_X1 = np.empty(1440)
        VSS_Y1 = np.empty(1440)
        VSS_Z1 = np.empty(1440)
        for j in range(1440):
            VSS_X1[j]= VSS_X[j]
        
            VSS_Y1[j]= VSS_Y[j]
        
            VSS_Z1[j]= VSS_Z[j]
            
            X =VSS_X1[VSS_X1>0] # condição de NAN
                                
            Y = VSS_Y1[VSS_Y1<0] # Condição de NAN
         
            Z = VSS_Z1[VSS_Z1<0] # Condição de NAN
        
            mean_px = np.mean(X)
            mean_py = np.mean(Y)
            mean_pz = np.mean(Z)
        
            F[j] =  np.sqrt((VSS_X[j]**2) + (VSS_Y[j]**2) + (VSS_Z[j]**2))    
            F1 = F[F<30000] # Condição para F nao pegar um not a number
            mean_pf = np.mean(F1)
    
            D[j] = np.arctan(VSS_Y[j]/VSS_X[j])
            D1 = D[D<0] # condição para NAN
       
            mean_pd = np.mean(D1)
    
            H[j] = np.sqrt((VSS_X[j]**2) + (VSS_Y[j]**2))
        
            H1 = H[H<30000] # CONDIÇÃO DE nan
        
            mean_ph = np.mean(H1)
        
            I[j] = np.arctan(VSS_Z[j]/H[j])
        
            I1 = I[I<0]
        
            mean_pi = np.mean(I1) 
     
        
        meanx[i] = mean_px
        meany[i] = mean_py
        meanz[i] = mean_pz
        meanf[i] = mean_pf
        meand[i] = mean_pd
        meanh[i] = mean_ph     
        meani[i] = mean_pi
    else:
        VSS_datos = pd.read_csv(dias[i], header = 23, delim_whitespace = True)
        VSS_X = VSS_datos['VSSX']
        VSS_Y = VSS_datos['VSSY']
        VSS_Z = VSS_datos['VSSZ']
        F = np.empty(1440)
        D = np.empty(1440)
        H = np.empty(1440)
        I = np.empty(1440)
        VSS_X1 = np.empty(1440)
        VSS_Y1 = np.empty(1440)
        VSS_Z1 = np.empty(1440)
        for j in range(1440):
            VSS_X1[j]= VSS_X[j]
        
            VSS_Y1[j]= VSS_Y[j]
        
            VSS_Z1[j]= VSS_Z[j]
        
            X =VSS_X1[VSS_X1>0] # condição de NAN
                            
            Y = VSS_Y1[VSS_Y1<0] # Condição de NAN
         
            Z = VSS_Z1[VSS_Z1<0] # Condição de NAN
        
            mean_px = np.mean(X)
            mean_py = np.mean(Y)
            mean_pz = np.mean(Z)
            
            F[j] =  np.sqrt((VSS_X[j]**2) + (VSS_Y[j]**2) + (VSS_Z[j]**2))    
            F1 = F[F<30000] # Condição para F nao pegar um not a number
            mean_pf = np.mean(F1)
    
            D[j] = np.arctan(VSS_Y[j]/VSS_X[j])
            D1 = D[D<0] # condição para NAN
       
            mean_pd = np.mean(D1)
    
            H[j] = np.sqrt((VSS_X[j]**2) + (VSS_Y[j]**2))
        
            H1 = H[H<30000] # CONDIÇÃO DE nan
        
            mean_ph = np.mean(H1)
        
            I[j] = np.arctan(VSS_Z[j]/H[j])
        
            I1 = I[I<0]
        
            mean_pi = np.mean(I1) 
    
        meanx[i] = mean_px
        meany[i] = mean_py
        meanz[i] = mean_pz
        meanf[i] = mean_pf
        meand[i] = mean_pd
        meanh[i] = mean_ph     
        meani[i] = mean_pi

# Eliminar los "nan" del vector mean 
meanx_2014 = [value for value in meanx if not math.isnan(value)]
meany_2014 = [value for value in meany if not math.isnan(value)]
meanz_2014 = [value for value in meanz if not math.isnan(value)]
meanf_2014 = [value for value in meanf if not math.isnan(value)]
meand_2014 = [value for value in meand if not math.isnan(value)]
meanh_2014 = [value for value in meanh if not math.isnan(value)]
meani_2014 = [value for value in meani if not math.isnan(value)]

#Calcula la media aritmética del año  
MEAN_X_2014 = np.mean(meanx_2014)
MEAN_Y_2014 = np.mean(meany_2014)
MEAN_Z_2014 = np.mean(meanz_2014)
MEAN_F_2014 = np.mean(meanf_2014)
MEAN_D_2014 = np.mean(meand_2014)
MEAN_H_2014 = np.mean(meanh_2014)
MEAN_I_2014 = np.mean(meani_2014)

print(MEAN_X_2014)
print(MEAN_Y_2014)
print(MEAN_Z_2014)
print(MEAN_F_2014)
print(MEAN_D_2014)
print(MEAN_H_2014)
print(MEAN_I_2014)






'''
    Lee la carpeta de datos del 2015 y calcula F(x,y,z)
'''


dias = glob.glob('*.min')
meanf = np.zeros(len(dias))
meand = np.zeros(len(dias))
meanx = np.zeros(len(dias))
meany = np.zeros(len(dias))
meanz = np.zeros(len(dias))
meanh = np.zeros(len(dias))
meani = np.zeros(len(dias))
for i in range(len(dias)):
    VSS_datos = pd.read_csv(dias[i], header = 23, delim_whitespace = True)
    VSS_X = VSS_datos['VSSX']
    VSS_Y = VSS_datos['VSSY']
    VSS_Z = VSS_datos['VSSZ']
    F = np.empty(1440)
    D = np.empty(1440)
    H = np.empty(1440)
    I = np.empty(1440)
    VSS_X1 = np.empty(1440)
    VSS_Y1 = np.empty(1440)
    VSS_Z1 = np.empty(1440)
    for j in range(1440):
        VSS_X1[j]= VSS_X[j]
        
        VSS_Y1[j]= VSS_Y[j]
        
        VSS_Z1[j]= VSS_Z[j]
        
        X =VSS_X1[VSS_X1>0] # condição de NAN
                            
        Y = VSS_Y1[VSS_Y1<0] # Condição de NAN
         
        Z = VSS_Z1[VSS_Z1<0] # Condição de NAN
        
        mean_px = np.mean(X)
        mean_py = np.mean(Y)
        mean_pz = np.mean(Z)
            
        F[j] =  np.sqrt((VSS_X[j]**2) + (VSS_Y[j]**2) + (VSS_Z[j]**2))    
        F1 = F[F<30000] # Condição para F nao pegar um not a number
        mean_pf = np.mean(F1)
    
        D[j] = np.arctan(VSS_Y[j]/VSS_X[j])
        D1 = D[D<0] # condição para NAN
       
        mean_pd = np.mean(D1)
   
        H[j] = np.sqrt((VSS_X[j]**2) + (VSS_Y[j]**2))
        
        H1 = H[H<30000] # CONDIÇÃO DE nan
        
        mean_ph = np.mean(H1)
        
        I[j] = np.arctan(VSS_Z[j]/H[j])
        
        I1 = I[I<0]
        
        mean_pi = np.mean(I1) 

    meanx[i] = mean_px
    meany[i] = mean_py
    meanz[i] = mean_pz
    meanf[i] = mean_pf
    meand[i] = mean_pd
    meanh[i] = mean_ph     
    meani[i] = mean_pi

# Eliminar los "nan" del vector mean 
meanx_2015 = [value for value in meanx if not math.isnan(value)]
meany_2015 = [value for value in meany if not math.isnan(value)]
meanz_2015 = [value for value in meanz if not math.isnan(value)]
meanf_2015 = [value for value in meanf if not math.isnan(value)]
meand_2015 = [value for value in meand if not math.isnan(value)]
meanh_2015 = [value for value in meanh if not math.isnan(value)]
meani_2015 = [value for value in meani if not math.isnan(value)]

#Calcula la media aritmética del año  
MEAN_X_2015 = np.mean(meanx_2015)
MEAN_Y_2015 = np.mean(meany_2015)
MEAN_Z_2015 = np.mean(meanz_2015)
MEAN_F_2015 = np.mean(meanf_2015)
MEAN_D_2015 = np.mean(meand_2015)
MEAN_H_2015 = np.mean(meanh_2015)
MEAN_I_2015 = np.mean(meani_2015)

print('X = ',MEAN_X_2015)
print('Y = ',MEAN_Y_2015)
print('Z = ',MEAN_Z_2015)
print('F = ',MEAN_F_2015)
print('D = ',MEAN_D_2015)
print('H = ',MEAN_H_2015)
print('I = ',MEAN_I_2015)
