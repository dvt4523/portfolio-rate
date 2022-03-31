# -*- coding: utf-8 -*-

import MarketstackApi, PdfReader
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
# import os
# from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import PolynomialFeatures

# os.chdir('E:\Drive FPT\Project\Source Code')

#Datetime Reformat
def dateShorten(dateString):
    dt = datetime.strptime(dateString,'%Y-%m-%dT%H:%M:%S%z')
    return dt.strftime('%d/%m')

data = MarketstackApi.requestData(0,PdfReader.df)

def axis_generate(data):
    x = []
    xlabel = []
    y = []
    for index in range(data['pagination']['count']-1):
        x = np.append(x,index)
        y = np.append(y,[MarketstackApi.price_weight(index,data)])
        xlabel = np.append(xlabel,[dateShorten(data['data'][index]['date'])])
    y = np.flip(y)
    
    return [x,y,xlabel]

def graph_generate(data):
    x = axis_generate(data)[0]
    y = axis_generate(data)[1]
    xlabel = axis_generate(data)[2]
    myline = np.linspace(0, 7, 200)                 #Curve line
    mymodel = np.poly1d(np.polyfit(x, y, 3))        #3rd degree model
    plt.xticks(x, np.flip(xlabel))
    plt.scatter(x, y)
    plt.plot(myline, mymodel(myline))

# graph_generate(data)
# print(xlabel)
# print(x)
# print(y)
 
# plt.scatter(np.flip(xlabel),np.flip(y)) #Reverse the array order to match real-time
# plt.show()

#%% Not enough datapoints to use this
# x = x[:, np.newaxis]
# y = y[:, np.newaxis]

# polynomial_features = PolynomialFeatures(degree=2)
# x_poly = polynomial_features.fit_transform(x)

# model = LinearRegression()
# model.fit(x_poly, y)
# y_poly_pred = model.predict(x_poly)
# plt.scatter(x, y, s=10)
# plt.plot(x, y_poly_pred, color='m')
# plt.show()
#%%


def find_min_max(model,y):
    derivative = model.deriv(1)                 #Take derivative of graph
    critical_values = np.roots(derivative.coef) #Finding 2 inflecton points of graph

    #Check if 
    if (type(critical_values[0])!=np.float64) or (type(critical_values[1])!=np.float64):
        return [np.amin(y), np.amax[y]]
    else:
        return [model(critical_values[0]),model(critical_values[1])]

# min_max = find_min_max(mymodel,y)

