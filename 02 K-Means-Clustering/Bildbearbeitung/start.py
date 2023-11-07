''' Import Bibliotheken '''
import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np
import random

''' Import Bild '''
img = img.imread('fox.jpg')
plt.imshow(img)
plt.axis('off')
plt.show()

''' K-Means-Clustering Algorithmus '''
row,col,tiefe = np.shape(img)
imgNew = img*0
k = 3
kRed = np.zeros(k)
kGreen = np.zeros(k)
kBlue = np.zeros(k)

kRedOld = np.zeros(k)
kGreenOld = np.zeros(k)
kBlueOld = np.zeros(k)

sumRed = np.zeros(k)
sumGreen = np.zeros(k)
sumBlue = np.zeros(k)

nextRed = np.zeros(k)
nextGreen = np.zeros(k)
nextBlue = np.zeros(k)

kRedDifference = np.zeros(k)
kGreenDifference = np.zeros(k)
kBlueDifference = np.zeros(k)

distanc = np.zeros(k)
error = 1
loops = 0

print('##############################################################')
for i in range(k):
    kRed[i] = random.randint(0,255)
    kGreen[i] = random.randint(0,255)
    kBlue[i] = random.randint(0,255)
    print() 
    print('k:',i+1)      
    print() 
    print('Erster rot-Wert:', kRed[i])
    print('Erster blau-Wert:', kBlue[i])
    print('Erster grün-Wert:', kGreen[i])
        
while (error):
    error = 0
    loops = loops + 1
    for r in range(row):
        for c in range(col):
            '''Red'''
            for l in range(k):
                distanc[l] = np.linalg.norm(kRed[l]-img[r,c,0])
                
            if (distanc[0]<distanc[1] and distanc[0]<distanc[2]):
                imgNew[r][c][0] = kRed[0]
            elif (distanc[1]<distanc[2]):
                imgNew[r][c][0] = kRed[1]
            else:
                imgNew[r][c][0] = kRed[2]
            '''Green'''
            for l in range(k):
                distanc[l] = np.linalg.norm(kGreen[l]-img[r,c,1])
                
            if (distanc[0]<distanc[1] and distanc[0]<distanc[2]):
                imgNew[r][c][1] = kGreen[0]
            elif (distanc[1]<distanc[2]):
                imgNew[r][c][1] = kGreen[1]
            else:
                imgNew[r][c][1] = kGreen[2] 
            '''Blue'''  
            for l in range(k):
                distanc[l] = np.linalg.norm(kBlue[l]-img[r,c,2])
                
            if (distanc[0]<distanc[1] and distanc[0]<distanc[2]):
                imgNew[r][c][2] = kBlue[0]
            elif (distanc[1]<distanc[2]):
                imgNew[r][c][2] = kBlue[1]
            else:
                imgNew[r][c][2] = kBlue[2] 
                   
    '''Centering'''
    for r in range(row):
        for c in range(col):
            for l in range(k):

                if (imgNew[r][c][0] == kRed[l]):
                   sumRed[l] = sumRed[l] + img[r][c][0]
                   nextRed[l] = nextRed[l] + 1

                if (imgNew[r][c][1] == kGreen[l]):
                   sumGreen[l] = sumGreen[l] + img[r][c][1]
                   nextGreen[l] = nextGreen[l] + 1

                if (imgNew[r][c][2] == kBlue[l]):
                   sumBlue[l] = sumBlue[l] + img[r][c][2]
                   nextBlue[l] = nextBlue[l] + 1
    print()               
    print('Loop:',loops,'##############################################################')
    print()  
    for i in range(k):  
        print() 
        print('k:',i+1)  
        print()     
        
        kRedOld[i] = kRed[i]
        if (nextRed[i]>0):
            kRed[i] = round(sumRed[i]/nextRed[i])
        kRedDifference[i] = kRed[i]-kRedOld[i]
        if (kRedDifference[i]!=0):
            error = error + 1
        print('Neuer rot-Wert:', kRed[i],'Änderung:',kRedDifference[i])
        
        kGreenOld[i] = kGreen[i]
        if (nextGreen[i]>0):
            kGreen[i] = round(sumGreen[i]/nextGreen[i])
        kGreenDifference[i] = kGreen[i]-kGreenOld[i]
        if (kGreenDifference[i]!=0):
            error = error + 1
        print('Neuer grün-Wert:', kGreen[i],'Änderung:',kGreenDifference[i])
        
        kBlueOld[i] = kBlue[i]
        if (nextBlue[i]>0):
            kBlue[i] = round(sumBlue[i]/nextBlue[i])
        kBlueDifference[i] = kBlue[i]-kBlueOld[i]
        if (kBlueDifference[i]!=0):
            error = error + 1
        print('Neuer blau-Wert:', kBlue[i],'Änderung:',kBlueDifference[i])
        
    ''' Neues Bild '''
    plt.imshow(imgNew)
    plt.axis('off')
    plt.show()
    
    
    
    
    
    
    
    
    










