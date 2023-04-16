import json
import base64
import pandas as pd
import streamlit as st
from io import StringIO
from io import BytesIO
from datetime import datetime
from pathlib import Path


# @st.cache(suppress_st_warning=True)
# def read_data(path):
#     return pd.read_csv(path)


# @st.cache(allow_output_mutation=True)
# def get_base64(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()


def set_bg(png_file):
    with open(png_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()

    # bin_str = get_base64(png_file)
    page_bg_img = """
        <style>
        .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        }
        </style>
    """ % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)


def head():
    st.title('Streamlit Web App')
    # st.subheader('sub header')
    # st.header('header')
    # st.text('text text text')
    # st.markdown("<p style='text-align: center;'>Markdown</p>",
    #             unsafe_allow_html=True)

    # file_uploader()

    # st.markdown("<h1 style='text-align: center; margin-bottom: -35px;'>Math Problem Generator</h1>", unsafe_allow_html=True)
    # st.caption("<p style='text-align: center'>by <a href='https://medium.com/geoclid'>Geoclid</a></p>", unsafe_allow_html=True)
    # st.write("Feeling overwhelmed by your daily grind? Looking for something fun to do? Click the button for a random math problem \U0001F642.")


def selection_box(txt_selection, mylist):
    # st.write(sample)
    # st.dataframe(sample)

    option = st.selectbox(
        txt_selection,
        mylist
        # ('Email', 'Home phone', 'Mobile phone')
    )

    # st.write('You selected:', option)
    return option

    # name = sample.iloc[0, 0]
    # link = sample.iloc[0, 1]
    # prob = sample.iloc[0, 2]
    # st.info(f'### {name}')
    # st.write(prob)
    # st.caption(f'[source]({link})')
    # st.markdown('---')


def footer(sample):
    st.text('footer text text')


# def footer(sample):
# st.caption("Support us by either reporting this problem for bad $\LaTeX$ formatting or buying a coffee!")
# col1, col2 = st.columns([1,8])
# col1.button('Report', on_click=report, args=(sample, ))
# col2.markdown("""
#     <a href="https://www.buymeacoffee.com/geoclid" target="_blank">
#     <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png"
#         width="136"
#         height="36"
#         alt="Buy Me A Coffee">
#     </a>
# """, unsafe_allow_html=True)


# def report():
#     print('test')


def convert_file_to_df(uploaded_file):
    if uploaded_file.type == 'text/csv':
        df = pd.read_csv(uploaded_file, encoding='latin-1')
        return df

    elif 'application' in uploaded_file.type:
        df = pd.ExcelFile(uploaded_file)
        sheet = selection_box('select a sheet', df.sheet_names)
        return df.parse(sheet)


def file_uploader():
    uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True, type={"csv", "xlsx"})
    # uploaded_files_new = [x for x in uploaded_files]
    # uploaded_files_dedupe = []

    for uploaded_file in uploaded_files:
        st.write("filename:", uploaded_file.name, "type:", uploaded_file.type)
        st.write(convert_file_to_df(uploaded_file))
        # uploaded_files_dedupe.append(uploaded_file)

# def report(sample):
# Authenticate to Firestore with the JSON account key.
# key_dict = json.loads(st.secrets['textkey'])
# creds = service_account.Credentials.from_service_account_info(key_dict)
# db = firestore.Client(credentials=creds)
#
# # Create a reference to the Google post.
# doc_ref = db.collection('defect').document(str(datetime.now()))
#
# # And then uploading some data to that reference
# idx = sample.index.item()
# doc_ref.set({'id': idx, 'status': True})
