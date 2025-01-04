
#Programa para hacer operaciones de probabilidad


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
        
