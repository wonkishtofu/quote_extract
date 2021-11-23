import streamlit as st
import spacy
import textacy.extract 
from newspaper import Article
import pandas as pd 

nlp = spacy.load('en_core_web_lg')
st.title("News Article Quote Extraction Tool")


url = st.text_input('Input your URL here:') 

if url:
    st.header("Extracted quotes from: "+url)

    article = Article(url)
    article.download()
    article.parse()

    doc = nlp(article.text.replace("'"," "))


    dq = textacy.extract.direct_quotations(doc)

    dq2 = textacy.extract.direct_quotations(doc)


    df = pd.DataFrame(dq2, columns=['speaker', 'verb', 'statement' ])

    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')


    # st.dataframe(df)

    csv = convert_df(df)

    for statement in dq:
        speaker, sig, stmt = statement
        st.markdown(f" > {speaker}: {stmt}")

    st.download_button(
    "Press to Download",
    csv,
    "quotes.csv",
    "text/csv",
    key='download-csv'
    )
    
    
    



    