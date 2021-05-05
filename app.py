# -*- coding: utf-8 -*-

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import PdfReader
import SessionState
import MarketstackApi
import Graph, Calculate

Session_state = SessionState.get(index='')

st.title("Evaluate your stock buy and sell orders")

st.subheader("First, Please upload your report pdf:")

uploaded_file = st.file_uploader("Only accept VCBS-generated report", type="pdf")

if uploaded_file is not None:
    df = PdfReader.feature_engineering(uploaded_file)

#Order list
st.subheader("Your processed order list is as followed:")
st.dataframe(df, width=690)

#Order select
st.subheader("Order currently being inspected:")
if (Session_state.index == '') or (Session_state.index == len(df)):
    Session_state.index = 0
    
if st.button("Next Order"):
    st.write(df.iloc[Session_state.index])
    Session_state.index = Session_state.index + 1

#Inspect order
if st.button("Analyze"):
    st.write(df.iloc[Session_state.index-1])
    data = MarketstackApi.requestData(Session_state.index-1,df)
    x = Graph.axis_generate(data)[0]
    y = Graph.axis_generate(data)[1]
    xlabel = Graph.axis_generate(data)[2]
    
    myline = np.linspace(0, 7, 200)                 #Curve line
    mymodel = np.poly1d(np.polyfit(x, y, 3))        #3rd degree model
    
#Draw Matplotlib chart
    fig = plt.figure()
    plt.xticks(x, np.flip(xlabel))
    plt.title('Weighted-price of ' + df.iloc[Session_state.index-1].StockCode)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.scatter(x, y, label = 'Weighted prices')
    plt.plot(myline, mymodel(myline), label = 'Best fit line')
    # plt.scatter(3,df.iloc[Session_state.index-1].Price, marker = 'o', color='r', label = "Order Price")
    plt.legend(loc=4)
    st.pyplot(fig)
    
#Find Critical values:
    min_max = Graph.find_min_max(mymodel,y)
    Score = Calculate.calculateScore(Session_state.index-1,df, min_max)
    st.subheader("This order rating is:")
    st.subheader(Score)