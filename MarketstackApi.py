# -*- coding: utf-8 -*-

from PdfReader import params
import requests
# import os

# os.chdir('E:\Drive FPT\Project\Source Code')

# parameters = {
#   'access_key': '25bf49a4b5db583d2265b2bef1e90a09',
#   'symbols': 'MSN.XSTC',
#   'date_from': '2020-10-14',
#   'date_to': '2020-10-15'
# }

# response = requests.get('http://api.marketstack.com/v1/tickers/MSN.XSTC/eod/2020-10-15')
def requestData(index,df):
    response = requests.get('http://api.marketstack.com/v1/eod', params=params(index,df))

    return response.json()

#Calculate weighted price
def price_weight(index,data):
    if index == 0:
        return data['data'][index]['close']
    else:
    #Getting volume of 2 consecutive days
        V2 = data['data'][index]['volume']
        V1 = data['data'][index-1]['volume']
        
    #Get close price and intraday price range
        P = data['data'][index]['close']
        votality = data['data'][index]['high'] - data['data'][index]['low']
        # print('osc range:' + str(votality))
    
        # print('%shift:'+str((V2-V1)/V1*100))
        shift = votality * ((V2-V1)/V1)
        # print('shift range:' + str(shift))
    
    #Calculate newly weighted price
        P = P+shift
        # print(data['data'][index]['close'])
        return P
    