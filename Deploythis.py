# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 21:27:07 2022

@author: MONIT
"""

import numpy as np
import pickle
import pandas as pd
from xgboost import XGBClassifier
import streamlit as st 

from PIL import Image

st.set_page_config(layout="centered")



pickle_in = open("XGBintel1.pkl","rb")
XGBintel1 = pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def resort_data(hotel,lead_time,deposit_type,customer_type,agent,adr):
    
   
   
    prediction = XGBintel1.predict([[hotel,lead_time,deposit_type,customer_type,agent,adr]])
    print(prediction)
    return prediction



def main():
    
    html_temp = """
    <div style="background-color:#17A589;padding:10px">
    <h2 style="color:white;text-align:center;">Hotel Churn Prediction App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    hotel = st.sidebar.radio("Hotel",[0,1])
    st.sidebar.success('Resort Hotel' if  hotel == 1  else 'City Hotel')
    lead_time = st.number_input('Lead Time',step=1.,format="%.2f")
    st.write(f' Lead Time :{lead_time}')
    deposit_type = st.sidebar.selectbox('Deposit Type',(0,1,2,3))
    
    customer_type = st.sidebar.selectbox('Customer type',(0,1,2))
    agent = st.number_input('Enter Agent',step=1.,format="%.2f")
    adr = st.number_input('Enter adr',step=1.,format="%.2f")
    
    result=""
    if st.button("Predict"):
        result=resort_data(hotel,lead_time,deposit_type,customer_type,agent,adr)    
        st.success('Yes,Booking is canceled' if format(result) == [1] else 'No, Booking is not canceled')


if __name__=='__main__':
    main()