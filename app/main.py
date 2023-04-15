import datetime
import streamlit as st
from utils import set_bg, head, footer, body, read_data


import time

st.set_page_config(page_title='MyApp', page_icon='assets/icon.png')

ss = st.session_state
set_bg('assets/background.png')


st.title('Streamlit Web App')
st.subheader('sub header')
st.header('header')
st.text('text text text')

head()

if 'prob_click' not in ss:
    ss['prob_click'] = False

if st.button('Bring it on!'):
    ss['prob_click'] = True
    ss['report_click'] = False
    df = read_data('data/sample.csv')
    # choice = df.sample(1)
    choice = df.columns
    print(choice)
    ss['sample'] = choice
    body(choice)

if ss['prob_click'] and ss['report_click']:
    body(ss['sample'])
    footer(ss['sample'])
elif ss['prob_click']:
    footer(ss['sample'])
    ss['report_click'] = True

