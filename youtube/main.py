import datetime
import streamlit as st
import time

st.title('Streamlit Web App')
st.subheader('sub header')
st.header('header')
st.text('text text text')

st.markdown("[markdownguide link](https://www.markdownguide.org/cheat-sheet)")
st.markdown("**Bold** *italic* word")
st.markdown("---")

# st.caption("Hi I am Caption")

st.markdown("[katex link](https://katex.org/docs/supported)")
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")

json = {"a": "1,2,3", "b": "4,5,6"}
st.json(json)


code = """
print("hello world")
def funct():
    return 0;
"""

st.code(code, language="python")
