# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

dimension = 2
pct_sample = 80
taille = 100

def genere_points():
    return np.random.random((taille,2))    
    
def classe(tab):
    lesClasses = []
    for point in tab:
        print(point)
        lesClasses.append(1) if ( (-0.5 * point[0] + 0.75) <= point[1]) else lesClasses.append(-1)
    newTab = np.c_[tab,lesClasses]
    return newTab

def montrer(tab,fct):
    for point in tab:
        print(point)
        plt.plot(point[0],point[1],'bo' if (point[2] > 0) else 'ro')
        
    x = np.linspace(0,1,100) # 100 linearly spaced numbers
    y = -1 * ( (fct[0] * x + fct[2]) / fct[1])
    plt.plot(x,y,'black')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.show()
    
def setup_data(tab,sample=pct_sample):    
    
    np.random.shuffle(tab)
    combien = (int) ((sample/100)*taille)    
    data_app = tab[:combien]
    data_test = tab[combien:]
    return(data_app,data_test)
    
def ptrain(data_app):
    #theta = np.random.random((dimension + 1,))
    theta = [0,0,0]
    for vecteur in data_app:
        x_plus = np.append(vecteur[:dimension],1)
        f_x = np.transpose(theta).dot(x_plus)
        if(np.sign(vecteur[dimension]) != np.sign(f_x)):
            theta = np.add(theta,vecteur[dimension] * x_plus)
            
    return theta
    
def main():
    data = classe(genere_points())
    montrer(data,ptrain(data))
    
if __name__ == "__main__":
    main()