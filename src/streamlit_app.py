import streamlit as st
import service as ser
import constants as const


import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
st.title("Ask any thing about Devi")

st.warning("I am still under training, so don't expect a good response.")

prompt=st.text_input("", placeholder="Enter your Prompt")
if st.button("submit"):
    st.write("user: "+str(prompt))

    out_put=ser.get_output(prompt)
    st.write("AI: "+str(out_put))

# st.write(out_put)


