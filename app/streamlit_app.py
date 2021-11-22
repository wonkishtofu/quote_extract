import streamlit as st
import spacy
import textacy.extract 
nlp = spacy.load('en_core_web_lg')
from newspaper import Article

nlp = spacy.load('en_core_web_lg')
nlp.add_pipe("merge_entities")

st.title("News Article Quote Extraction Tool")

url = 'https://www.straitstimes.com/singapore/spore-to-relook-long-term-approach-to-land-use-planning-engagement-for-review-to-start'

url = st.text_input('Input your URL here:') 


if url:
    st.header("Extracted quotes from: "+url)


    article = Article(url)
    article.download()
    article.parse()

    doc = nlp(article.text)


    new_words = [token.text if token.text!="'" else "`" for token in doc]
    

    dq = textacy.extract.direct_quotations(doc)

    for statement in dq:
        speaker, sig, stmt = statement
        st.markdown(f" > {speaker}: {stmt}")