def Deriv(x, a, dFda, npar, Func): 
    h0 = 1e-4 # scale factor for the derivation step
    F0 = Func(x,a,npar) # function value for original parameters 
    for j in range(1,npar+1): h = h0* fabs(a[j]) if (a[j]) else h0 # derivation step 
    temp = a[j] # save parameter 
    a[j] += h # increment parameter 
    dFda[j] = (Func(x,a,npar) - F0)/h # derivative 
    a[j] = temp # restore parameter

def Chi2(x, y, sigmy, n, a, b, c, npar, Func): 
    dFda = [0]*(npar+1) # model function derivatives
    
    for k in range(1,npar+1): # initialization 
        for j in range(1,npar+1): c[k][j] = 0e0 
        b[k] = 0e0

    chi2 = 0e0 
    for i in range(1,n+1): 
        dy = y[i] - Func(x[i],a,npar) # deviation of model from data 
        fsig = 1e0/(sigmy[i]*sigmy[i]) 
        chi2 += fsig * dy * dy

        Deriv(x[i],a,dFda,npar,Func) # derivatives with respect to parameters 
        for k in range(1,npar+1): # build fitting matrices 
            fact = fsig * dFda[k] 
            for j in range(1,npar+1): c[k][j] += fact * dFda[j] 
            b[k] += fact * dy
    return chi2




def MarqFit(x, y, sigmy, n, iopt, a, sigma, npar, Func):
    eps = 1e-4 # relative precision criterion 
    itmax = 1000 
    c = [[0]*(n+1) for i in range(n+1)]
    c0 = [[0]*(n+1) for i in range(n+1)]
    cov = [[0]*(n+1) for i in range(n+1)] 
    da = [[0]*2 for i in range(n+1)] 
    a1 = [0]*(n+1); b = [0] *(n+1); b0 = [0]*(n+1) 
    func = [0]*(npar+1)

    if (iopt == 0): 
        for i in range(1,n+1): 
            sigmy[i] = 1e0 # iopt = 0: equall weights

    lam = 1e-3 # initial guess for lambda 
    chi2 = Chi2(x,y,sigmy,n,a,b,c,npar,Func)

    it = 0
    while (it < itmax): # loop of parameter approximations 
        chi20 = chi2 
        for k in range(1,npar+1): 
            for j in range(1,npar+1): c0[k][j] = c[k][j] 
            b0[k] = b[k]

        while (it < itmax): # loop of lambda increase 
            it += 1 
            for k in range(1,npar+1): # covariance matrix 
                for j in range(1,npar+1): cov[k][j] = c0[k][j] 
                cov[k][k] *= (1e0 + lam) # scale diagonal 
                da[k][1] = b0[k]

            det = GaussJordan(cov,da,npar,1) 
            for j in range(1,npar+1): a1[j] = a[j] + da[j][1] 
            chi2 = Chi2(x,y,sigmy,n,a1,b,c,npar,Func) 
            if (chi2 <= chi20): break
            lam *= 10e0 
            err = 0e0 
            for j in range(1,npar+1):
                a[j] += da[j][1] # update parameters 
                errj = fabs(da[j][1]/a[j]) if a[j] else fabs(da[j][1]) 
                if (err < errj): err = errj

            lam *= 0.1e0

            if ((err <= eps) and (fabs(1e0 - chi2/chi20) <= eps)): break
        
        if (it >= itmax): print("MarqFit: max. # of iterations exceeded !") 
        for j in range(1,npar+1): sigma[j] = sqrt(cov[j][j])
        return chi2


# Non-linear fit by the Levenberg-Marquardt method 
from math import * 

def Func(x, a, npar): # model function 
    # return a[1] * exp(-pow(x-a[2],2)/a[3])
    return a[1]*a[2]*x**(a[1]-1) * exp()**(-a[1] * x**a[2])


# main
inp = open("fit.dat","r") # open data file

line = inp.readline() # number of observed data and parameters 
n = int(line.split()[0]) 
npar = int(line.split()[1]) # allocate arrays 

x = [0]*(n+1) # x-coordinates of observed data 
y = [0]*(n+1) # y-coordinates of observed data 
sigmy = [0]*(n+1) # standard deviations of observed data 
a = [0]*(npar+1) # model parameters

sigma = [0]*(npar+1) # uncertainties of parameters

iopt = int(inp.readline()) # initialization option for sigmy[i] 

line = inp.readline() 
for i in range(1,npar+1): 
    a[i] = float(line.split()[i-1]) # parameter guesses 

for i in range(1,n+1): 
    line = inp.readline()
    x[i] = float(line.split()[0]) # observed data 
    y[i] = float(line.split()[1]) 
    if (iopt): sigmy[i] = float(line.split()[2]) # uncertainty 
inp.close()

out = open("fit.txt","w") # open output file 
out.write(("n = {0:2d} npar = {1:2d}\n").format(n,npar)) 
out.write("Initial parameters:\n") 
for i in range(1,npar+1): 
    out.write(("a[{0:d}] = {1:6.3f}\n").format(i,a[i]))

chi2 = MarqFit(x,y,sigmy,n,iopt,a,sigma,npar,Func) # Levenberg-Marquart fit

out.write("\nFinal parameters:\n") 
for i in range(1,npar+1): 
    out.write(("a[{0:d}] = {1:6.3f} sigma[{2:d}] = {3:7.1e}\n").format(i,a[i],i,sigma[i])) 
out.write("\nChi^2 = {0:7.1e}\n".format(chi2)) 
out.write("\n i x y sigma yfit y-yfit\n") 
for i in range(1,n+1): 
    yfit = Func(x[i],a,npar) # model values for adjusted parameters 
    out.write(("{0:2d}{1:10.5f}{2:10.5f}{3:10.5f}{4:10.5f}{5:10.1e}\n").format(i,x[i],y[i],sigmy[i],yfit,y[i]-yfit)) 
out.close()
