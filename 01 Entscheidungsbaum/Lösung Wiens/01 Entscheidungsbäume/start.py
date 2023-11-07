import numpy as np
import func

''' CSV laden '''
data = np.genfromtxt('ape.csv',delimiter=',',dtype=str) 

''' Allgemeiner Gini-Koeffizient '''
# Zeilen & Spalten
row,col = data.shape
# Entscheidungen & Häufigkeit
decision,index,decisionCount = np.unique(data[1:row,col-1],return_counts=True,return_index=True) 
# Gini-Koeffizient
GiniCoefficient = func.gini(decisionCount,row-1)

''' Der spezifische/gewichtete Gini-Koeffizient '''
sort = -1
GiniSpecific = np.zeros(col-1)

for l in range(col-1):
    sort = sort + 1
    Decision, Index, DecisionCount = np.unique(data[1:row,sort],return_counts=True,return_index=True)
    often = np.zeros((np.size(Decision),np.size(decision)))
    summe = np.zeros(np.size(Decision))
    for n in range(np.size(Decision)):
        for m in range(np.size(decision)):
            for k in range(row-1):
                if (data[k+1,sort]==Decision[n]): 
                    if (data[k+1,col-1]==decision[m]):
                        often[n,m] = often[n,m] + 1
                        
        summe[n] = summe[n] + func.gini(often[n,0:col],DecisionCount[n])
        GiniSpecific[l] = GiniSpecific[l] + DecisionCount[n]/(row-1) * summe[n]



''' Print Gini '''
print('Der allgemeine Gini-Koeffizient lautet:', GiniCoefficient)
print('Für den gewichteten/spezifischen Gini lautet die Reihenfolge:')
sort = np.argsort(GiniSpecific)
for j in range(col-1):
    order = np.where(sort == j)[0]
    print(data[0][order])















