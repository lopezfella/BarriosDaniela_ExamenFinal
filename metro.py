import numpy as np
import matplotlib.pyplot as plt
#lista = []
#datos = open("valores.txt", "r")
#val = datos.readlines()
#lista = [float(d) for d in val]
#lista.append(val)

#lista2= 2.031331588946557076e+00, 5.886777538940683563e+00, 2.195744759275823021e+00, 6.821886748452244298e+00, 8.793952398085184141e-01, 2.951577398416659559e+00, 4.454332895499525158e+00, -1.804396045394615955e+00, -5.841925974092386120e+00, -1.113495627653518838e+00

file= open("valores.txt", "r")
dat = file.readlines()
file.close
lista = [float(d) for d in dat]

def densidad(lista, sigma):
    sigma = 1
    for j in lista:
        return (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-0.5*(j**2/(sigma**2)))
    
N=100000
x_list=[np.random.random()*5]
y_list=[np.random.random()*5]


for i in range(1,N):
    x=x_list[i-1]+np.random.normal(loc=0.0, scale=1)
    y=y_list[i-1]+np.random.normal(loc=0.0, scale=1)

plt.figure()                  
_ = plt.hist2d(x_list, y_list, bins=50)
plt.savefig("sigma.png")
