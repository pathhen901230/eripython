#Modulo de clases

import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.api as sm
import numpy as np
import pandas as pd
import os
#Dependencias
#Generar objeto de Odds/Ratio
class estimate_OR:
    def __init__(self,tab):
        a= tab.iloc[1,1]
        b= tab.iloc[1,0]
        c= tab.iloc[0,1]
        d=tab.iloc[0,0]
        tot= a+b+c+d
        OR= (a*d)/(b*c)
        std= np.sqrt((1/a)+(1/+b)+(1/c)+(1/d))
        ic025= np.log(OR) - (1.96*std)
        ic975= np.log(OR) + (1.96*std)
        self.Iex= (a+b)/tot
        self.Ienox= (c+d)/tot
        self.OR= OR
        self.ic025= ic025
        self.ic975= ic975

#Clase estimate RR. Requiere aportar una tabla de contingencias
class estimate_RR:
    def __init__(self,tab):
        a= tab.iloc[1,1]
        b= tab.iloc[1,0]
        c= tab.iloc[0,1]
        d=tab.iloc[0,0]
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

    
