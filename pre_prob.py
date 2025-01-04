
#Programa para hacer operaciones de probabilidad
#Dependencias
import matplotlib.pyplot as plt
import scipy
import scipy.stats as stats
import statsmodels.api as sm
import sklearn as sk
from sksurv.nonparametric import kaplan_meier_estimator
import numpy as np
import pandas as pd
import os
import random as rd
#

class pre_prob_combno:
    def __init__(self,n,k):
        self.n= n
        self.k= k
        self.comb= scipy.special.factorial(n)/(scipy.special.factorial(k)*(scipy.special.factorial(n-k)))
        print(int(self.comb))
        
class pre_prob_permno:
    def __init__(self,n,k):
        self.n=n
        self.k=k
        self.perm= scipy.special.factorial(n)/(scipy.special.factorial(n-k))
        print(int(self.perm))
        
