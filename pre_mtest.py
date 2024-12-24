
#Librerias
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
import pandas as pd
import os
#

#Funcion para determina prueba para variables continuas
#No se requiren dependencias mas que librerias
def pre_mtest_cont(cont,factor):
    #Dos grupos
    factor=factor.astype('category')
    levels= factor.cat.categories
    g1=  cont[factor==levels[0]]
    g2=  cont[factor==levels[1]]
    #Estadistica descriptiva
    g1_mean= round(np.mean(g1),4)
    g1_sd= round(np.std(g1),4)
    g2_mean= round(np.mean(g2),4)
    g2_sd= round(np.std(g2),4)
    dif_me= g1_mean-g2_mean
    test= 'NA'
    #Valoracion de supuestos
     #Normalidad
    p_shap= stats.shapiro(cont)[1]
     #Homogeneidad de varianzas
    p_var= stats.levene(g1,g2)[1]
    if p_shap>0.05:
        if p_var<0.05:
            pv=stats.ttest_ind(g1, g2,equal_var=False)
            test='Welch T de Student'
        else:
            pv=stats.ttest_ind(g1, g2,equal_var=True)
            test='T de Student de Grupos Independientes'
    else:
        pv=stats.mannwhitneyu(g1, g2)[1]
        test= 'Mann U Whitney'
        dic= pd.DataFrame([{'Media1':g1_mean,'DE':g1_sd,
                'Media2':g2_mean,'DE2':g2_sd,'p':pv,
                'Test':test}])
    return(dic)

pre_mtest_cont(df['EDAD'],df['NACIMIENTO <34 SEMANAS 0. NO 1. SI'])
