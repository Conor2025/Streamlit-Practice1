import streamlit as st
import pandas as pd

st.title("Power 5 Conferences as they should be")

st.write("Here are the rightfull teams of the each Power 5 Conference")
data = pd.DataFrame({
  'BIG 10 Conference': ['Illinois', 'Indiana', 'Iowa', 'Michigan', 'Michigan State',
                  'Minnesota', 'Northwestern', 'Ohio State', 'Penn State', 'Purdue', 'Wisconsin'],
  'BIG 12 Conference': ['Baylor', 'Colorado', 'Iowa State', 'Kansas', 'Kansas State', 'Missouri',
                       'Nebraska', 'Oklahoma', 'Oklahoma State', 'Texas', 'Texas A&M', 'Texas Tech'],
  'ACC Conference': ['Boston College', 'Clemson', 'Duke', 'Florida State', 'Georgia Tech', 'Maryland',
                    'Miami', 'NC State', 'North Carolina', 'Virginia', 'Virginia Tech', 'Wake Forest'],
  'PAC 10 Conference': ['Arizona', 'Arizona State', 'California', 'Oregon', 'Oregon State',
                       'Stanford', 'UCLA', 'USC', 'Washington', 'Washington State'],
  'SEC Conference': ['Alabama', 'Arkansas', 'Auburn', 'Florida', 'Georgia', 'Kentucky',
                    'LSU', 'Mississippi State', 'Ole Miss', 'South Carolina', 'Tennessee', 'Vanderbilt']
})
st.write(data)
