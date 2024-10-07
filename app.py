# from datetime import datetime
import streamlit as st
import pandas as pd

row = pd.DataFrame()
data = pd.read_csv('data.csv')
st.title('Form Thing')

dt = st.date_input('Pick a Date')

hr = st.time_input('Pick a Time', step=3600)

with st.form('Input Data'):
    notes = st.text_area('Notes')
    left, right = st.columns(2)
    num1 = left.number_input('Number 1', step=1)
    num2 = right.number_input('Number 2', step=1)
    if st.form_submit_button('Submit', use_container_width=True):
        row = pd.DataFrame({'Date': [dt],
                            'Time': [hr],
                            'Notes': [notes],
                            'Num 1': [num1],
                            'Num 2': [num2]})
        data = pd.concat([data, row])
        data.to_csv('data.csv', index=False)
        data = pd.read_csv('data.csv')

if len(row) > 0:
    st.dataframe(data, use_container_width=True, hide_index=True)
