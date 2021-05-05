# -*- coding: utf-8 -*-

from pandas.tseries.offsets import BDay
import os, tabula
from datetime import datetime


# os.chdir('E:\Drive FPT\Project\Source Code')

#Define pdf file to read
file = 'SampleVCBS.pdf'

#Read pdf
def read_file(file):
    return tabula.read_pdf(file, pages='all', multiple_tables=True)

# read_file(file)

def feature_engineering(file):
    tables = read_file(file)
#%% Feature Engineering

    df = tables[0].dropna()

    #Relabel columns
    df = df.rename(columns={df.columns[0]:'ID',df.columns[1]:'Date',df.columns[2]:'StockCode',df.columns[3]:'Type',df.columns[8]:'Price',df.columns[10]:'Status'})

    #Filter out completed order
    df.loc[df['Status'] == 'Hoàn thành']

    #Filter out zero value orders
    df = df[df.Price !='0']

    #Drop unnecessary columns
    df = df[['Date','StockCode','Type','Price']]
    
    return df

df = feature_engineering(file)
#%% Looping and accessing the rows in report

# for index in range(len(df)):
    
    # params(index)
    

#%% Building parameters
def params(index, df):
    access_key = '25bf49a4b5db583d2265b2bef1e90a09'
    symbols = df.iloc[index].StockCode
    fromDate = datetime.strptime(df.iloc[index].Date,"%d/%m/%Y") - BDay(4)  #Using Pandas BDay for business days
    toDate = datetime.strptime(df.iloc[index].Date,"%d/%m/%Y") + BDay(4)
    from_str = fromDate.strftime("%Y-%m-%d")
    to_str = toDate.strftime("%Y-%m-%d")
    return {'access_key': access_key,
  'symbols': symbols+'.XSTC',
  'date_from': from_str,
  'date_to': to_str,
        }
