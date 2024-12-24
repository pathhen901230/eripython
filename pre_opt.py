
#Librerias

import matplotlib.pyplot as plt
import scipy.stats as sp
import numpy as np
import pandas as pd
import os

#Prueba diagnostica(requerida para optimizacion de corte)

def pre_pdiag(cr):
    coconta= len(cr)==2 and len(cr.columns)==2
    cotab= cr.iloc[1,1]>0 and cr.iloc[0,1]>0 and cr.iloc[0,0]>0 and cr.iloc[1,0]>0
    if coconta==True and cotab==True:
        Sens=  cr.iloc[1,1]/(cr.iloc[1,1]+cr.iloc[0,1])
        Esp= cr.iloc[0,0]/(cr.iloc[0,0]+cr.iloc[1,0])
        VPP= cr.iloc[1,1]/(cr.iloc[1,1]+cr.iloc[1,0])
        VPN= cr.iloc[0,0]/(cr.iloc[0,0]+cr.iloc[0,1])
        Acc= (cr.iloc[1,1]+cr.iloc[0,0])/(cr.iloc[1,1]+cr.iloc[0,0]+cr.iloc[0,1]+cr.iloc[1,0])
        J= Sens+Esp-1
        DOR= (cr.iloc[1,1]*cr.iloc[0,0])/(cr.iloc[1,0]*cr.iloc[0,1])
        Out = pd.DataFrame([{"Sensibilidad": Sens, "Especificidad": Esp, "VPP":VPP, "VPN":VPN,
               "Precision":Acc,"J":J,"DOR":DOR}])
    else:
        Out= pd.DataFrame([{"Sensibilidad": 'NA', "Especificidad": 'NA', "VPP":'NA', "VPN":'NA',
               "Precision":'NA',"J":'NA',"DOR":'NA'}])    
    return(Out)

#Funcion de punto de corte mas optimo
#Dependencias pre_pdiag
def pre_opt_belog(cat,con,dire=">"):
    #Dependencias requeridas
    #pre_pdiag
        dic= pd.DataFrame([{'Corte':[],'Sensibilidad':[],
              'Especificidad':[],'VPP':[],'VPN':[],
              'DOR':[],'J':[],'Acc':[]}])
        for i in range(0,len(cat)):
                try:
                    if dire==">":
                            tab=pd.crosstab(con>con[i],cat)
                            tab.t= tab.iloc[0,0]>0 and tab.iloc[1,1]>0 and tab.iloc[0,1]>0 and tab.iloc[1,0]>0 
                            if tab.t==True:
                                od= pre_pdiag(tab)
                                di= pd.DataFrame([{'Corte': con[i]
                                                    ,'Sensibilidad': od.iloc[0,0]
                                      ,'Especificidad':od.iloc[0,1]
                                      ,'VPP': od.iloc[0,2]
                                      ,'VPN' :od.iloc[0,3]
                                      ,'DOR':od.iloc[0,6]
                                      ,'J':od.iloc[0,5]
                                      ,'Acc':od.iloc[0,4]}])
                                dic=pd.concat([dic,di])   
                    else:
                            tab= pd.crosstab(con<con[i],cat)
                except:
                    pass

        return(dic.iloc[1:len(dic.index)])   

#



