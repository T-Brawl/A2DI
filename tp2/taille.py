# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

taille_h = np.loadtxt("taille_h.txt")
taille_f = np.loadtxt("taille_f.txt")
taille_all = np.concatenate((taille_h, taille_f), axis=0)

p_h = 0.505
p_f = 0.495

def histo(data):
    plt.hist(data,bins=range(int(data.min()), int(data.max()) + 1, 1),color='green',histtype='step')
    

def marginal(homme=taille_h,femme=taille_f):
    stats = np.zeros((2,250))
    for taille in homme:
        stats[0][int(taille)] = stats[0][int(taille)] + 1
    for taille in femme:
        stats[1][int(taille)] = stats[1][int(taille)] + 1
        
    toshow = (stats[0]+stats[1])
    echantillon = len(homme) + len(femme)
    for i in range(0,len(toshow)):
        toshow[i] = toshow[i] / echantillon 
        
    print(sum(toshow))
    plt.plot(range(0,250),toshow,'g-')


def main():
    marginal()
    #histo(taille_all)

if __name__ == "__main__":
    main()