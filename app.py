import streamlit as st

# attribute is a string
attribute = st.selectbox('Choose attribute', ['Sector', 'Revenue'])

if attribute == 'Sector':
    sector = st.selectbox('Choose sector', ["sector 1", "sector 2"])

if attribute == 'Revenue':
    revenue = st.selectbox('Choose revenue', ["revenue 1", "revenue 2"])

"---"

# attributes is an array
attributes = st.multiselect('Choose attributes', ['Sector', 'Revenue'])

if "Sector" in attributes:
    sector = st.multiselect('Choose sectors', ["sector 1", "sector 2"])

if "Revenue" in attributes:
    revenue = st.multiselect('Choose revenues', ["revenue 1", "revenue 2"])