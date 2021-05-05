# -*- coding: utf-8 -*-

import PdfReader
import Graph


def calculateScore(index,df, min_max):
    buyPrice = df.iloc[index].Price.replace(',','')
    if (df.iloc[index].Type == 'Mua'):
        return 1-(float(buyPrice) - min_max[0])/min_max[0]
    else:
        return (min_max[1] - float(buyPrice))/min_max[1]

