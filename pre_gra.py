
#Dependencias

#Funciones

def pre_mgra_dist(df):
    col= df.columns
    for i in range(0,len(df.columns)):
        try:
            x= df.iloc[:,i]  
            x= x.sort_values(ascending=True)
            y= stats.norm.pdf(x,np.mean(x),np.std(x))
            plt.plot(x,y)
            plt.xlabel(col[i])
            plt.ylabel('Densidad')
            plt.qqplot
            plt.show()
        except:
            pass
