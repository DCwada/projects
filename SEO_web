import streamlit as st
from ecommercetools import seo
st.title('SEO Information')
value = st.selectbox('Navigation', ['Vitals', 'Keys'])
if value == 'Vitals':
    x = st.text_input("Enter url(s)", 'Search site vitals')
    if len(x) > 0 and x != 'Search site vitals':
       df =  seo.get_core_web_vitals('AIzaSyC21cZLw5VaF73ihV4SPeSiFOZnbu78D20', [str(x)] if "," not in str(x) else str(x).split(","))
       st.write(df.head())
else:
    x = st.text_input("Input keyword phrase")
    df = (seo.google_autocomplete(x, include_expanded= False))
    value_2 = st.multiselect("Keyword filter",["medium tail", "short tail"])
    if len(value_2) > 0:
        filt = (df['term'].str.count(" ") >= 2 if value_2[0] == 'medium tail' else df['term'].str.count(" ") == 1)
        df['relevance'] = (df['relevance']).astype(int)
        y = st.slider('Filter by relevance', int(df['relevance'].min(axis=0)), int(df['relevance'].max(axis=0)))
        filt_2 = (df['relevance'] >= y)
        st.write(df[filt][filt_2])

