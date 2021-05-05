# -*- coding: utf-8 -*-

from PdfReader import df
from Graph import min_max



def calculateScore(index):
    buyPrice = df.iloc[index].Price.replace(',','')
    if (df.iloc[index].Type == 'Mua'):
        return 1-(float(buyPrice) - min_max[0])/min_max[0]
    else:
        return (min_max[1] - float(buyPrice))/min_max[1]

print(calculateScore(0))
