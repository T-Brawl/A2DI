# -*- coding: utf-8 -*-
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
import time

db=datasets.load_iris()
data_tp = np.c_[db['data'],db['target']]
taille = len(data_tp)

voisinage = -1
pct_sample = 80
dimension = len(db['data'][0])

nbTests = 10

def setup_data(sample=pct_sample):    
    #print("Nombre d'exemples : {}".format(len(db['data'])))
    #print("Nombre d'attributs : {}".format(len(db['data'][0])))
    #print("Nombre de classes : {}".format(len(db['target_names'])))
    #print("Voisinage : {}".format(voisinage))
    
    np.random.shuffle(data_tp)
    combien = (int) ((sample/100)*taille)    
    data_app = data_tp[:combien]
    data_test = data_tp[combien:]
    return(data_app,data_test)


def kppv(exemple,apprentissage,nbVoisins):
    lesDistances = []   
    
    for vecteur in apprentissage:
        lesDistances.append(np.linalg.norm(exemple[:dimension]-vecteur[:dimension]))
        
    #lesQuels = np.array(lesDistances)    
    lesQuels = np.argsort(lesDistances)
    lesQuels = lesQuels[:nbVoisins]
    #Ici, lesQuels renvoient pour l'instant les indices des k voisins les plus proches
    
    for i in range(0,len(lesQuels)):
        lesQuels[i] = apprentissage[lesQuels[i]][dimension]
        #lesQuels <- classe du vecteur
        
    return np.argmax(np.bincount(lesQuels))
    
    
    
def erreurVoisinage(voisinage):
    erreur = 0   
    for i in range(nbTests):
        (data_app,data_test) = setup_data()  
        for vecteur in data_test:
            if(kppv(vecteur,data_app,voisinage) != vecteur[dimension]):
                erreur = erreur + 1       
    return (erreur / (nbTests * len(data_test)))
       
    
def main(maxVoisins=100):
    lesY = []  
      
    for i in range(1,maxVoisins+1):
        pctCorrect = 1 - erreurVoisinage(i)
        lesY.append(pctCorrect)
        print("{}\t{}".format(i,pctCorrect))
        
    plt.plot(range(1,maxVoisins+1), lesY)
    plt.show()
    best = np.argsort(np.array(lesY))[len(lesY) - 1]
    print("Voisinage de taille {} : {} % de bonne classification".format(best+1,lesY[best]*100))
    

def time_kppv():
    lesY = [] 
    tests = 500
    for i in range(20,100,5):
        duration = 0
        for appel in range(0,tests):
            (train,test) = setup_data(i)
            debut = time.time()
            kppv(test[np.random.randint(len(test))],train,15)
            end = time.time()
            duration += ((end - debut) / tests)
        lesY.append(duration)
        print(i)
    
    plt.plot(range(20,100,5),lesY,'go',range(20,100,5),lesY,'k')
    plt.show()
    
if __name__ == "__main__":
    #main()
    time_kppv()