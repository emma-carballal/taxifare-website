import streamlit as st
import datetime
import requests

'''
# NY taxi
'''
with st.form(key='params_for_api'):
    pickup_date = st.date_input('Date', value=datetime.datetime(2012, 10, 6, 12, 10, 20))
    pickup_time = st.time_input('Time', value=datetime.datetime(2012, 10, 6, 12, 10, 20))
    pickup_datetime = f"{pickup_date} {pickup_time}"
    pickup_long = st.number_input('Pickup longitude', value=40.7614327)
    pickup_lat = st.number_input('Pickup latitude', value=-73.9798156)
    dropoff_long = st.number_input('Dropoff longitude', value=40.6413111)
    dropoff_lat = st.number_input('Dropoff latitude', value=-73.7803331)
    passenger_count = st.number_input('Passengers', value=1, max_value=8, min_value=1)

    st.form_submit_button('Make prediction')

url = 'https://taxifare.lewagon.ai/predict'

params = {"pickup_datetime":pickup_datetime,
        "pickup_longitude":pickup_long,
        "pickup_latitude":pickup_lat,
        "dropoff_longitude":dropoff_long,
        "dropoff_latitude":dropoff_lat,
        "passenger_count":passenger_count
        }

r = requests.get(url = url, params = params).json()
prediction = r['fare']

st.header(f'Your fare will be around ${round(prediction, 2)}')
