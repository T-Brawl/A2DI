# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

pct_sample = 80
taille = 100
nbTests = 10

def genere_points(dimension):
    return np.random.random((taille,dimension))    
    
def classe(tab):
    lesClasses = []
    for point in tab:
        lesClasses.append(1) if ( (-0.5 * point[0] + 0.75) <= point[1]) else lesClasses.append(-1)
    newTab = np.c_[tab,lesClasses]
    return newTab

def montrer(tab,tabbis,fct):
    for point in tab:
        plt.plot(point[0],point[1],'bo' if (point[-1] > 0) else 'ro')
        
    for point in tabbis:
        plt.plot(point[0],point[1],'b.' if (point[-1] > 0) else 'r.')
        
    x = np.linspace(0,1,100)
    y = -1 * ( (fct[0] * x + fct[2]) / fct[1]) 
    plt.plot(x,y,'g--')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.show()
    
def setup_data(tab,sample=pct_sample):    
    
    np.random.shuffle(tab)
    combien = (int) ((sample/100)*taille)    
    data_app = tab[:combien]
    data_test = tab[combien:]
    return(data_app,data_test)
    
def ptest(vecteur,theta):
    x_plus = np.append(vecteur[:-1],1)
    return np.sign(np.transpose(theta).dot(x_plus))
    
def ptrain(data_app):
    theta = np.random.random((len(data_app[0]),))
    
    incorrect = True
    
    while incorrect:
        for vecteur in data_app:
            x_plus = np.append(vecteur[:-1],1)
            f_x = np.transpose(theta).dot(x_plus)
            if(np.sign(vecteur[-1]) != np.sign(f_x)):
                theta = np.add(theta,vecteur[-1] * x_plus)
            
        incorrect = False
   
        for vecteur in data_app:
           if (vecteur[-1] != ptest(vecteur,theta)):
               incorrect = True
               break
           
    return theta


def erreur(data,theta):
    erreur = 0
    for vecteur in data:
        if(vecteur[-1] != ptest(vecteur,theta)):
            erreur = erreur +1
    return (erreur / len(data))
    
def main():
    data = classe(genere_points(2))
    (train,test) = setup_data(data)
    theta =  ptrain(train)
    print(theta)
    montrer(train,test,theta)
    """
    lesX = []
    lesY = []
    for i in range(2,20):
        erreur_moyenne = 0
        for c in range(0,nbTests):
            data = classe(genere_points(i))
            (train,test) = setup_data(data)
            theta = ptrain(train)
            erreur_moyenne = erreur_moyenne + 1 - erreur(test,theta)
        print(i)
        lesX.append(i)
        lesY.append(erreur_moyenne / nbTests)
    
    plt.plot(lesX,lesY,'b--')
    plt.show()
    """
   
if __name__ == "__main__":
    main()