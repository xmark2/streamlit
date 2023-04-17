import json
import base64
import pandas as pd
import streamlit as st


def set_bg(png_file):
    with open(png_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()

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


def selection_box(txt_selection, mylist):

    option = st.selectbox(
        txt_selection,
        mylist
    )
    return option


def convert_file_to_df(uploaded_file):
    if uploaded_file.type == 'text/csv':
        df = pd.read_csv(uploaded_file, encoding='latin-1')
        multiselect('my fields', df.columns)
        # st.write(df)
        # return df

    elif 'application' in uploaded_file.type:
        df = pd.ExcelFile(uploaded_file)
        ch = checkbox(df.sheet_names)
        mydict = dict(zip(df.sheet_names, ch))
        for sheet in df.sheet_names:
            if mydict[sheet]:
                multiselect('my fields', df.parse(sheet).columns)
                # st.write(df.parse(sheet))
                # return df.parse(sheet)
        # sheet = selection_box('select a sheet', df.sheet_names)
        # return df.parse(sheet)


def checkbox(mylist):
    checked_list = []
    for elem in mylist:
        checked_list.append(st.checkbox(elem))
    return checked_list


def file_uploader():
    uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True, type={"csv", "xlsx"})

    for uploaded_file in uploaded_files:
        st.write("filename:", uploaded_file.name, "type:", uploaded_file.type)
        convert_file_to_df(uploaded_file)

        # multiselect('my fields', df.columns)

        # st.write(convert_file_to_df(uploaded_file))


def multiselect(multi_text, fields):
    options = st.multiselect(
        multi_text,
        fields)

    st.write('You selected:', ' | '.join(options))
