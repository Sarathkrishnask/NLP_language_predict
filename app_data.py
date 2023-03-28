#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pickle
import string
import streamlit as st
import webbrowser
import googletrans
from googletrans import Translator


# print(googletrans.LANGUAGES)
# translator = Translator()
# global translator
global Lrdetect_Model

LrdetectFile = open('model.pckl','rb')
Lrdetect_Model = pickle.load(LrdetectFile)
LrdetectFile.close()
st.title("Language Detection Tool")
input_test = st.text_input("provide your text input here", 'Hello my name is jay ')

button_clicked = st.button("Get Language Name")

if button_clicked:
    lang =googletrans.LANGUAGES
    st.text(Lrdetect_Model.predict([input_test]))
    val = Lrdetect_Model.predict([input_test])
#     st.text_area(label="Output Data:", value=Lrdetect_Model.predict([input_test]), height=350)
    translator = Translator()
#     if lang.values() == Lrdetect_Model.predict([input_test]):
    result=translator.translate(input_test, src='en', dest='ta')
    st.text_area(label="Output Data:", value=result.text, height=350)
#         st.text_area(label="Output Data:", value=result.text, height=350)

#     print(result.text)
#     st.text_area(label="Output Data", value=translator.translate(input_test,src=Lrdetect_Model.predict([input_test]),dest='ta'),height=300)

    

# In[ ]:





# In[ ]:




