
#Dependencias

import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.api as sm
import numpy as np
import pandas as pd
import os

#Funcion para buscar outliers en data.frames    
#df es el data frame
def pre_dfm_out(df):
    mediana= np.median(df)
    qmed= np.quantile(df,0.5)
    pcu= np.quantile(df,0.25)
    tcu= np.quantile(df,0.75)
    iqr= tcu-pcu
    up= tcu +(1.5*iqr)
    down= pcu-(1.5*iqr)
    cond1= df[(df > up) | (df< down)]
    print(len(cond1))
    return(['Se detectaron',len(cond1),'outliers',cond1])
#   
