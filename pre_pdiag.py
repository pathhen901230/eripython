
#Dependencias
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.api as sm
import sklearn as sk
from sksurv.nonparametric import kaplan_meier_estimator
import numpy as np
import pandas as pd
import os
#Clase prueba diagnostica
#cr indica tabla de contingencia(2x2)
class pre_pdiag:
    def __init__(self,cr):
        coconta= len(cr)==2 and len(cr.columns)==2
        cotab= cr.iloc[1,1]>0 and cr.iloc[0,1]>0 and cr.iloc[0,0]>0 and cr.iloc[1,0]>0
        if coconta==True and cotab==True:
            a= cr.iloc[1,1] 
            b= cr.iloc[1,0]
            c= cr.iloc[0,1]
            d= cr.iloc[0,0]            
            self.Prev= (a+c)/(a+b+c+d)
            self.Sens=  cr.iloc[1,1]/(cr.iloc[1,1]+cr.iloc[0,1])
            self.Esp= cr.iloc[0,0]/(cr.iloc[0,0]+cr.iloc[1,0])
            self.VPP= cr.iloc[1,1]/(cr.iloc[1,1]+cr.iloc[1,0])
            self.VPN= cr.iloc[0,0]/(cr.iloc[0,0]+cr.iloc[0,1])
            self.Acc= (cr.iloc[1,1]+cr.iloc[0,0])/(cr.iloc[1,1]+cr.iloc[0,0]+cr.iloc[0,1]+cr.iloc[1,0])
            self.J= self.Sens+self.Esp-1
            self.DOR= (cr.iloc[1,1]*cr.iloc[0,0])/(cr.iloc[1,0]*cr.iloc[0,1])
            self.LLR= self.Sens/(1-self.Esp)
            self.LLN= (1-self.Sens)/self.Esp
    def dfe(self):
           Out = pd.DataFrame([{'Prevalencia':self.Prev,"Sensibilidad": self.Sens, 
                                "Especificidad": self.Esp, "VPP":self.VPP, 
                                "VPN":self.VPN,
                  "Precision":self.Acc,"J":self.J,"DOR":self.DOR,
                  'LLR':self.LLR,'LLN':self.LLN}])
           return(Out)

