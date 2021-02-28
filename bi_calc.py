import scipy as sp

def binomial_calc(x,N,pi):
    prob = (sp.special.factorial(N)/
           (sp.special.factorial(x)*
           (sp.special.factorial(N-x)))*
           (pi**x)*
           (1-pi)**(N-x))
    return prob
