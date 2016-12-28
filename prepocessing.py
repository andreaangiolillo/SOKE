import csv
import numpy as np


#@param
#@output:1)kpi:  
#            contiene tutti i valori numeri del file association_score.csv quindi
#            kpi[i,0] = id
#            kpi[i,1] = article_id
#            kpi[i,2] = length
#            kpi[i,3] = relevance_score
#            kpi[i,4] = rarity_score
#            kpi[i,5] = localPageRankMean
#            kpi[i,6] = localHubMean
#            kpi[i,7] = dbpediaPageRankMean
#            kpi[i,8] = path_informativeness
#            kpi[i,9] = path_pattern_informativeness
#            kpi[i,10] = localPageViewMean
#
#        2)data: 
#            e' una lista di liste, dove ogni lista e' una riga del csv
#            (lo usiamo per prendere poi i nomi delle associazioni da mostrare)
#
def download_association_score():

    with open('Date/association_score.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        data = list(spamreader)
        kpi = np.zeros((len(data)-1,11))
         
        i = 0  
        for row in data:    
            if (row[0] != "id"):#elimino la prima riga del csv
                kpi[i, 0] = float(row[0])
                kpi[i, 1] = float(row[1])
                kpi[i, 2] = float(row[8])
                kpi[i, 3] = float(row[9])
                kpi[i, 4] = float(row[10])
                kpi[i, 5] = float(row[11])
                kpi[i, 6] = float(row[12])
                kpi[i, 7] = float(row[13])
                kpi[i, 8] = float(row[14])
                kpi[i, 9] = float(row[15])
                kpi[i, 10] = float(row[16])
                #print kpi[i]
                i = i + 1
            
    return kpi, data

#@param
#@output user: numpy array con le righe del file .csv
def download_user_evaluated_association():
    with open('Date/user_evaluated_association.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        data = list(spamreader)

        user = np.zeros((len(data)-1,4))
        i = 0  
        for row in data:    

            if (row[0] != "user_id"):#elimino la prima riga del csv
                user[i, 0] = float(row[0])
                user[i, 1] = float(row[1])
                user[i, 2] = float(row[2])
                user[i, 3] = float(row[3])
                #print user[i]
                i = i + 1
            
            
            
    return user
#if __name__ == '__main__':
#     kpi, data = download_association_score()
#     evaluated = download_user_evaluated_association()
#     
    
    
    