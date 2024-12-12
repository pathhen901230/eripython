# -*- coding: utf-8 -*-
#Experimental
def sum(x,y):
    z= x+y
    return(z)

sum(1,2)
sum(3,4)

def prime(x):
    if x==2:
        return(True)
    elif x==3:
        return(True)
    for i in range(2,x-1):
        out= x % i
        if out==0:
            return(False)
    return(True)    

prime(7)

#Funciones para hacer calculos

#Funcion de asociacion
    #Devuelve OR e intervalo de confianza
def pre_esti_AS(cr):
    a= cr.loc[1,1]
    b= cr.loc[0,1]
    c= cr.loc[1,0]
    d= cr.loc[0,0]
    OR= (a*d)/(c*b)
    Iex= str(a)+ "/" + str(a+b)
    Ienox= str(c) + "/" + str(c+d)
    errstd= np.sqrt((1/a)+(1/b)+(1/c)+(1/d))
    C025= np.exp(np.log(OR)-(1.96*errstd))
    C975= np.exp(np.log(OR)+(1.96*errstd))
    out= pd.DataFrame([{'Iex':Iex,'Ienox':Ienox,'OR':OR,'C025':C025,'C975':C975}])
    return(out)
#Función de prueba diagnóstica
    #Devuelve la sensibilidad, especificidad, valor predictivo positivo, valor predictivo negativo, precision y J
def pre_pdiag(cr):
    Sens=  cr.loc[1,1]/(cr.loc[1,1]+cr.loc[0,1])
    Esp= cr.loc[0,0]/(cr.loc[0,0]+cr.loc[1,0])
    VPP= cr.loc[1,1]/(cr.loc[1,1]+cr.loc[1,0])
    VPN= cr.loc[0,0]/(cr.loc[0,0]+cr.loc[0,1])
    Acc= (cr.loc[1,1]+cr.loc[0,0])/(cr.loc[1,1]+cr.loc[0,0]+cr.loc[0,1]+cr.loc[1,0])
    J= Sens+Esp-1
    DOR= (cr.loc[1,1]*cr.loc[0,0])/(cr.loc[1,0]*cr.loc[0,1])
    Out = pd.DataFrame([{"Sensibilidad": Sens, "Especificidad": Esp, "VPP":VPP, "VPN":VPN,
           "Precision":Acc,"J":J,"DOR":DOR}])
    return(Out)
#Funcion media y desviación estandar
    #Devuelve la media y la desviación estándar del data.frame
def pre_medsd(df):
    med= round(df.mean(),4)
    sd= round(df.std(),4)
    d= {'Media':med,'Desviacion':sd}
    dictio = pd.DataFrame([d])
    return(dictio)
#Funcion para devolver media y desviación estándar de todo el data.frame
def pre_tab_medf(df):
    di= pd.DataFrame([{'Col':'NA','Media':'NA','Sd':'NA'}])
    for i in range(0,len(df.columns)):
        try:
            out= pre_medsd(df.iloc[:,i])
            apt= pd.DataFrame([{'Col':df.columns[i],
                           'Media':out.iloc[0,0],
                           'Sd':out.iloc[0,1]}])
            di= di._append(apt)
            print(df.columns[i])
            print(pre_medsd(df.iloc[:,i]))
        except:
            print(df.columns[i])
            print('NA')
    di= di.iloc[1:len(df)]
    di.to_csv("Out.csv")
#    

