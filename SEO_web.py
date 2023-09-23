import streamlit as st
from ecommercetools import SEO
st.markdown("<h1 style='text-align: center; color: gray;'>SEOptimizer</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white;'>SEOptimizer</h1>", unsafe_allow_html=True)
value = st.selectbox('Navigation', ['Key word generator', 'Check webpage vital'])
if value == 'Key word generator':
    x = st.text_input("Input any word to generate search engine ideas")
    df = (seo.google_autocomplete(x, include_expanded= True))
    value_2 = st.multiselect("Keyword filter", ["medium tail", "short tail"])
    if len(value_2) > 0:
        filt = (df['term'].str.count(" ") >= 2 if value_2[0] == 'medium tail' else df['term'].str.count(" ") == 1)
        df['relevance'] = (df['relevance']).astype(int)
        y = st.slider('Filter by relevance', int(df['relevance'].min(axis=0)), int(df['relevance'].max(axis=0)))
        filt_2 = (df['relevance'] >= 0)
        st.write(df[filt][filt_2])
else:
    x = st.text_input("Enter the url of the website you wish to track (this takes a few seconds)", 'Search site vitals')
    if len(x) > 0 and x != 'Search site vitals':
       df =  seo.get_core_web_vitals('AIzaSyC21cZLw5VaF73ihV4SPeSiFOZnbu78D20', [str(x)] if "," not in str(x) else str(x).split(","))
       st.write(df.head())
