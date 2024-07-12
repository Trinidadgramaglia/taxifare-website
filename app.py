import streamlit as st
import datetime
import requests

'''
# TaxiFareModel front
'''


url = 'https://taxifare.lewagon.ai/predict'

d = st.date_input(
    "Date",
    datetime.date(2019, 7, 6))

t = st.time_input('Time')


plo = st.number_input('Pickup longitude')

pla = st.number_input('Pickup latitude')

dlo = st.number_input('Dropoff longitude')

dla = st.number_input('Dropoff latitude')

pc = st.selectbox('Passenger count', [1,2,3,4,5])

X_pred = {
    'pickup_datetime':(f'{d} {t}'), #corregir esta
    'pickup_longitude':plo,
    'pickup_latitude':pla,
    'dropoff_longitude':dlo,
    'dropoff_latitude':dla,
    'passenger_count':pc
}

response = requests.get(url, params=X_pred)
res=response.json()

txt = st.text_area('Prediccion', f'''{res['fare']}
    ''')


#if url == 'https://taxifare.lewagon.ai/predict':

#    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')
