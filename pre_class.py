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

#Estimacion de proporciones
class estimate_prop:
    def __init__(self, phat, n,method="Wald"):
    #Evaluar condiciones
        if phat>=1:
            sys.exit('Numero no es una proporcion, debe ser menor a 1')
        else:
            if method=="Wald":
            #Calculo Wald
               self.p= phat
               q= 1-phat
               std= np.sqrt((phat*q)/n)
               self.ic025= phat - 1.96*std
               self.ic975= phat + 1.96*std
            #Calculo 

#
class estimate_cor:
    def __init__(self,df1,df2):
        #Estimacion de correlacion con grafica
        #df1 es data frame x 
        #df2 es data frame y
        pdf= pd.concat([df1,df2],axis=1)
        pdf= pdf.sort_values(by=str(pdf.columns[0]),ascending=True)
        pdf= pdf.dropna()
        print(pdf.columns[0])
        ar1 = pdf.iloc[:,0]
        ar2 = pdf.iloc[:,1]
        de=stats.pearsonr(ar1,ar2)
        self.cor= np.round(de[0],4)
        self.p= np.round(de[1],4)
        plt.plot(pdf.iloc[:,0],pdf.iloc[:,1],'o')
        #Modelo de regresion lineal#
        self.x= pdf.iloc[:,0]
        self.y= pdf.iloc[:,1]
        self.x= sm.add_constant(self.x)
        mod=sm.OLS(self.y,self.x).fit()
        plt.plot(self.x,mod.predict(self.x))
        #
        plt.title('Correlacion='+str(self.cor)+' ,p='+str(self.p))
        plt.xlabel(str(pdf.columns[0]))
        plt.ylabel(str(pdf.columns[1]))
        plt.show()
    def printf(self):
        dfe= pd.DataFrame([{'Correlacion':self.cor,'p':self.p}])
        return(dfe)
        print(len(isq['GLU_ANGIO']))    
#    
