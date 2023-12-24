from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import streamlit as st
import string
import pickle
import nltk


def transform_text(text):
    ps = PorterStemmer()
    text = text.lower()
    text = nltk.word_tokenize(text)

    text_d1 = []

    # Removing all non alpha numeric characters
    for i in text:
        if i.isalnum():
            text_d1.append(i)

    text_d2 = text_d1[:]
    text_d1.clear()

    # Remove punctuation and stopword
    for i in text_d2:
        if i not in stopwords.words('english') and i not in string.punctuation:
            text_d1.append(i)

    text_d2 = text_d1[:]
    text_d1.clear()

    # Covert all similar words to base form
    for i in text_d2:
        text_d1.append(ps.stem(i))

    return " ".join(text_d1)

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title('Email/SMS Spam Classifier')

input_sms = st.text_area('Enter the message')

if st.button('Predict'):
    # 1. Preprocess
    transformed_sms = transform_text(input_sms)
    # 2. Vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3.Predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.header('Spam')
    else:
        st.header('Not Spam')