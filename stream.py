import numpy as np
import pickle
import pandas as pd

import streamlit as st 

from PIL import Image

pickle_in = open("sal.pkl","rb")
classifier=pickle.load(pickle_in)




def predict_note_authentication(YearsExperience):
    try:
        YearsExperience = float(YearsExperience)
    except ValueError:
        raise ValueError("Input must be a numeric value.")
    prediction = classifier.predict([[YearsExperience]])
    return prediction



def main():
    st.title("Salary Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Salary Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    YearsExperience = st.text_input("Experience","Type Here")

    result=""
    if st.button("Predict"):
        result=predict_note_authentication(YearsExperience)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    