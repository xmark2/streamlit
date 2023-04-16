import datetime
import time
import streamlit as st
from utils import set_bg, head, footer, file_uploader, selection_box

st.set_page_config(page_title='MyApp', page_icon='assets/icon.png')

ss = st.session_state
set_bg('assets/background.png')

head()
# file_uploader()
# with st.spinner("Loading..."):
#     time.sleep(5)

features = ['Please choose a feature', 'FileUploader', 'Empty']

selectedApp = selection_box('select a feature', features)

if selectedApp == features[0]:
    st.write(None)
elif selectedApp == features[1]:
    file_uploader()
else:
    st.write(selectedApp)


# with st.sidebar:
#     with st.echo():
#         st.write("This code will be printed to the sidebar.")
#
#     with st.spinner("Loading..."):
#         time.sleep(5)
#     st.success("Done!")
# tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
# with tab1:
#     st.header("A cat")
#
# with tab2:
#     st.header("A dog")
#
# with tab3:
#     st.header("A owl")

