import streamlit as st
import spacy
import textacy.extract 
from newspaper import Article
import nltk
import pandas as pd 

nlp = spacy.load('en_core_web_lg')
st.title("News Article Quote Extraction Tool")


url = st.text_input('Input your URL here:') 

if url:
    st.header("Keywords and Extracted Quotes from: "+url)

    article = Article(url)
    article.download()
    article.parse()

    article.nlp()
    st.code(article.keywords)
    st.header('Summary: ')
    st.write(article.summary)

    doc = nlp(article.text.replace("'"," "))


    dq = textacy.extract.direct_quotations(doc)

    dq2 = textacy.extract.direct_quotations(doc)


    df = pd.DataFrame(dq2, columns=['speaker', 'verb', 'statement'])
    df['source'] = url

    def convert_df(df):
        return df.to_csv().encode('utf-8')


    csv = convert_df(df)
    st.header("Direct Quotes:")


    for statement in dq:
        speaker, sig, stmt = statement
        st.markdown(f" > {speaker}: {stmt}")

    st.download_button(
    "Click Here to Download Quotes",
    csv,
    article.title+".csv",
    "text/csv",
    key='download-csv'
    )
    
    
    



    