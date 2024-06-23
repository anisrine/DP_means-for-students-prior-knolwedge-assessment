import math
import pandas as pd
import numpy as np
from matplotlib import style
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


style.use('ggplot')


class DPMEANS:
    def __init__(self, londa, max_iter=1):
        self.londa = londa
        self.max_iter = max_iter

    def fit(self, data):

        self.u = {}
        self.l = {}
        self.s_l={}
        self.z = {}
        self.k = 1

        for i in range(len(data)):
                self.z[i] = 1

        self.u[0] = np.mean(data, axis=0)      


        for i in range(1, self.max_iter+1):

                for index in range(len(data)):
                   
                    distances = [np.linalg.norm(data[index]-self.u[c]) for c in range(self.k)]
                    distances_array = np.array(distances)
                    
                    if min(distances) > self.londa:
                        
                        self.k = self.k+1
                        self.z[index] = self.k
                        self.u[self.k-1] = data[index]

                    else:
                        self.z[index] = distances_array.argmin()+1 #distances.index(min(distances))  #self.k #min(distances)
                        
                    distances.clear()

                # the output  here is k and the clusters indexes
                # Generate the clusters
                for j in range(1, self.k+1):
                    list = []
                    list_s = []
                    for i in range(len(data)):
                        if self.z[i] == j:
                            list.append(data[i])
                            list_s.append(i)

                    self.l[j] = list
                    self.s_l[j] = list_s

if __name__ == '__main__':

    # Read data from the excel file
    df = pd.read_excel('ClusteringStudents_1.xlsx')
    data = df.values
    df_score = pd.read_excel('psottestscore.xlsx')
    data_score = df_score.values
    students_ids = {}
    students_posttest = {}
    scores_index = {}
    

    for i in range(len(data_score)):
         students_ids[i] = data_score[i][0]
         students_posttest[i] = data_score[i][1]
   
    #Apply PCA to data
    pca = PCA().fit(data)
    X = pca.transform(data)
    
    #Instantiate DPMEANS with alpha=3.2 ( the best value after many experiments)
    DF = DPMEANS(3.2, 100)
    
    # Apply DP-means algorithm on the data
    DF.fit(X)
    
    #print the number of clusters
    print("number of clusters:",DF.k)
    print("clusters indexers:")

   #print clusters indicators
    print(DF.z)

    print("posttest scores in this cluster:")

    for j in range(1, len(DF.s_l)+1):
        scores = []
        for item in DF.s_l[j]:
           scores.append(students_posttest[item])
        scores_index[j] = np.mean(scores)

    print(scores_index)


