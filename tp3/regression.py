# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import math
import random

taille_sample = 90

def datagen():
    #x = np.linspace(0,5,90)
    x = np.linspace(-10,10,taille_sample)
    y = []
    Xtr = []
    Xte = []
    Ytr = []
    Yte = []

    for i in range(len(x)):
        #y.append(np.random.normal(2*x[i]+1,0.2))
        y.append(np.random.normal(math.sin(x[i]) / x[i],0.2))       
        #y.append(math.sin(x[i]) / x[i])       
        
        if (i % 3 != 0):
            Xtr.append(x[i])
            Ytr.append(y[i])
        else:
            Xte.append(x[i])
            Yte.append(y[i])
            
    return(Xtr,Xte,Ytr,Yte)
    
def theta_etoile(x,y):    
    X_plus = np.c_[x,np.ones(len(x))].T    
    x_xt_1 = np.linalg.inv(np.dot(X_plus,X_plus.T))
    tmp = np.dot(x_xt_1,X_plus)  
    return np.dot(tmp,y)
    
    
def polyreg(x,y,puissance):
    X_power = np.zeros((puissance+1,len(x)))
    
    for i in range(0,puissance+1):
        X_power[i,:] = np.power(x,puissance - i)
        
    x_xt_1 = np.linalg.inv(np.dot(X_power,X_power.T))
    tmp = np.dot(x_xt_1,X_power)  
  
    return np.dot(tmp,y)
    
    
def montrer(X_train, X_test, Y_train, Y_test, fct=None):
    for i in range(len(X_train)):
        plt.plot(X_train[i],Y_train[i],'ro')
        
    for i in range(len(X_test)):
        plt.plot(X_test[i],Y_test[i],'bo')
            
    if (fct != None):
        x = np.linspace(-10,10,taille_sample)
        y = 0
        
        for p in range(len(fct)):
            a = fct[p]
            y += (a * np.power(x,len(fct) - p - 1))
        
        plt.plot(x,y,'g--')

    plt.show()
    
    
    
    
def main():
    X_train, X_test, Y_train, Y_test = datagen()    
    droite = polyreg(X_train,Y_train,8)
    montrer( X_train, X_test, Y_train, Y_test, droite)
   
if __name__ == "__main__":
    main()