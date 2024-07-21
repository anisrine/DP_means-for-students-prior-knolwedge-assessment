<h2>  DP-Means Algorithm for Students Prior Knolwedge Assessment</h2>

<h3>Description </h3>
This is the Python implementation of DP-means algorithm as described in the paper " Clustering Students Based on Their Prior Knowledge".
The DP-means algorithm, as described by Kullis & Jordan  <a href="https://arxiv.org/abs/1111.0352">[Kullis et al.,2012]</a> , is a hard-clustering approximation of nonparametric Bayesian models.
The input consists of pre-test answer choices of the students. Since the pre-test contains 35 questions, each such response vector 
contains 35 entries corresponding to each answer choice picked by a student.

<h3>Usage</h3> 

    import pandas as pd
    #Read data from the excel file
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

<h3>Citation</h3>
@Misc{EDM2019,
      authors= {Nisrine Ait Khayi, Vasile Rus},
      title = {Clustering Students Based on Their Prior Knowledge},
      howpublished={\url{https://files.eric.ed.gov/fulltext/ED599189.pdf}},
      year={2019}
      }
