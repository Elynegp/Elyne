import streamlit as st
import pandas as pd
import numpy as np
voc= pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vTQWNRrz_DSqnKmiBDmNiaFtncC26BXjf92jxIObq8hlTlgs8a8LiZXh1GXMIBxMk2EuRPy7s19WKeG/pub?output=csv")
st.dataframe(voc)
l= voc.shape[0]
i=np.random.choice(range(l))
word_fr= voc["Définition"].values[i]
word_chi=voc["Pinyin"].values[i]
st.write(word_frt""+word_chi)
