import csv
import numpy as np

"""
@attention: this method allows to extract data from association_score.csv
@param article: it indicates the article's id. If it is != -1, the method returns only the article's data
@param graph: it is a flag. If it is True the method returns only the data necessary to create the graph
@return: A numpy array with association_score's data
"""
def extract_association_score(article = -1, graph = False):

    with open('../../data/association_score.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
        
    if graph == False:
        kpi = np.zeros((len(data)-1,11))
        i = 0
        for row in data[1:]: #skip first line
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
            i = i + 1    
        if article != -1:
            mask = kpi[:, 1] == article
            kpi = kpi[mask]
        
    elif article != -1:#take only columns for to create graph
        graph = []
        for row in data[1:]:
            if int(row[1]) == article:
                graph.append((row[0],row[2],row[3], row[4],row[6], row[7]))
        kpi = graph
    return kpi
