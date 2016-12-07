# -*- coding: utf-8 -*-
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

taille_h = np.loadtxt("taille_h.txt")
taille_f = np.loadtxt("taille_f.txt")
taille_all = np.concatenate((taille_h, taille_f), axis=0)
taille_max = int(max(np.max(taille_h),np.max(taille_f)))

p_h = 0.505
p_f = 0.495
"""
bins = np.arange(100,np.ceil(taille_max+1))-0.5
bins_centers = bins[:-1]+0.5
(pX1h,bins_out) = np.histogram(taille_h,bins=bins)
plt.figure()
plt.bar(bins_centers,pX1h,width=1.0,color='blue')

(pX1f,bins_out) = np.histogram(taille_f,bins=bins)
plt.figure()
plt.bar(bins_centers,pX1f,width=1.0,color='pink')


pX1 = pX1h * p_h + pX1f * pX1f
plt.figure()
plt.bar(bins_centers,pX1,width=1.0,color='green')
"""
def histo(data):
    plt.hist(data,bins=range(int(data.min()), int(data.max()) + 1, 1),color='green',histtype='step')
    

def marginal(tab):
    stats = np.zeros((taille_max+1,))
    for taille in tab:
        stats[int(taille)] += 1
        
    elem = len(tab)
        
    return stats / elem
    
def mode(tab):
    
    stats = np.zeros((taille_max+1,))
    for taille in tab:
        stats[int(taille)] += 1
            
    
    cm = "null"
    occurence = -1
    
    for i in range(0,len(stats)):
        if (stats[i] > occurence):
            occurence = stats[i]
            cm = i
    
    return cm
    
def moyenne(tab):
    return np.mean(tab)
    
def mediane(tab):
    return np.median(tab)
    
def variance(tab):
    return np.var(tab)

def ecart_type(tab):
    return np.std(tab)

def skew(tab):
    return sc.stats.skew(tab)
    
def gauss(mu,sigma,size):
    return np.random.normal(mu, sigma, size)

def main():
    pX1 = np.array((marginal(taille_h) * p_h + marginal(taille_f) * p_f))
    #print(pX1)    
    print("Mode {}".format(mode(taille_all)))  
    print("Variance {}".format(variance(taille_all)))  
    print("Ecart type {}".format(ecart_type(taille_all)))  
    print("Skew {}".format(skew(taille_all)))
    s = taille_h
    
    binss = np.arange(100,np.ceil(taille_max+1))-0.5
    count, bins, ignored = plt.hist(s, bins=binss, normed=True)
    
    
    
    mu, sigma = moyenne(taille_h), ecart_type(taille_h)
    gauss_bins = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) )
    
    print(count - gauss_bins)
    plt.plot(bins, gauss_bins, linewidth=2, color='r')
    plt.show()
    #histo(taille_all)"""

if __name__ == "__main__":
    main()