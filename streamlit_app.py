import streamlit as st
import pandas as pd
import numpy as np

st.title("The BIG 10 Conference As It Should Be")

st.write("Here are the original 10 teams of the BIG 10 Conference")
st.write(pd.DataFrame({
  'BIG 10 teams': ['Illinois', 'Indiana', 'Iowa', 'Michigan', 'Michigan State',
                  'Minnesota', 'Northwestern', 'Ohio State', 'Purdue', 'Wisconsin']
}))
st.dataframe(data)
