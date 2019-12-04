import numpy as np
import matplotlib.pyplot as plt

file = np.genfromtxt("monthrg.dat")

def k(N):
    k=[]
    for i in range(N+1):
        k.append(i)
    return k

def fourier(x,k):
    xk=[]
    v=len(k)
    u=len(x)
    for i in range(v):
        cont=0
        for j in range(0,u):
            cont+= x[j]*np.exp(1j*(-2*np.pi/u)*k[i]*j)
        xk.append(cont)
    return (np.abs(xk))
    
año=file[:,0]
mes = file[:,1]
dias = file[:,2]
manchas = file[:,3]


def s(t):
    return np.sin(t)
t=np.linspace(1,4*np.pi,100)
plt.figure()
plt.plot(año, manchas, color='red')
plt.plot(año, fourier(s(t),k(len(manchas)-1)), color='green')
plt.title("Gráfico Promedio de manchas vs año .verde es la transf.")
plt.xlabel("Año")
plt.ylabel("Manchas solares")
plt.xlim([1900,1995])
plt.ylim([0,250])
plt.savefig("solar.png")

