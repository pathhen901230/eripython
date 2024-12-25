#Modulo de clases

import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.api as sm
import numpy as np
import pandas as pd
import os
#Dependencias
#Generar objeto de Odds/Ratio
#Clase estimate_OR 
class estimate_OR:
    def __init__(self,tab):
        a= tab.iloc[1,1]
        b= tab.iloc[1,0]
        c= tab.iloc[0,1]
        d=tab.iloc[0,0]
        #Valoracion de supuesto Fisher
        fish_bool= a>5 and b>5 and c>5 and d>5
        if fish_bool== True:
            #Chi_cuadrada
            self.p=stats.chi2_contingency(tab)[1]
            self.method="Chi Cuadrada"
        else:
            #Prueba exacta de Fisher
            self.p=stats.fisher_exact(tab)[1]
            self.method="Exacta de Fisher"
        tot= a+b+c+d
        OR= (a*d)/(b*c)
        std= np.sqrt((1/a)+(1/+b)+(1/c)+(1/d))
        ic025= np.exp(np.log(OR) - (1.96*std))
        ic975= np.exp(np.log(OR) + (1.96*std))
        self.Pre= (a+b)/tot
        self.OR= OR
        self.ic025= ic025
        self.ic975= ic975
#Prueba estimate_OR    
es=estimate_OR(pd.crosstab(df['DIABETES 0-NO 1-SI '],df['HAS 0-NO 1-SI ']))
#Generar objeto de Riesgo relativo
class estimate_RR:
    def __init__(self,tab):

        a= tab.iloc[1,1]
        b= tab.iloc[1,0]
        c= tab.iloc[0,1]
        d=tab.iloc[0,0]
        #Valoracion de supuesto Fisher
        fish_bool= a>5 and b>5 and c>5 and d>5
        if fish_bool== True:
            #Chi_cuadrada
            self.p=stats.chi2_contingency(tab)[1]
            self.method="Chi Cuadrada"
        else:
            #Prueba exacta de Fisher
            self.p=stats.fisher_exact(tab)[1]
            self.method="Exacta de Fisher"
        Iex= a/(a+b)
        Ienox= c/(c+d)
        tot= a+b+c+d
        RR= Iex/Ienox
        FE= (1-Iex)/a
        SE= (1-Ienox)/c
        std= np.sqrt(FE+SE)
        ic025= np.exp(np.log(RR) - (1.96*std))
        ic975= np.exp(np.log(RR) + (1.96*std))
        self.Iex= a/(a+b)
        self.Ienox= c/(c+d)
        self.RR= RR
        self.ic025= ic025
        self.ic975= ic975
    def printf(self):
        print(('Iex:'+str(self.Iex)+', Ienox:'+str(self.Ienox)
              +' ,RR:'+str(self.RR)+
              ' ,IC025:'+str(self.ic025)+' ,IC975:'+str(self.ic975)))

    
