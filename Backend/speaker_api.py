##############################################################
import streamlit.components.v1 as components

_component_func = components.declare_component(
        "my_component",
        url="http://localhost:3001",
    )

def my_component(nom, key=None):
    component_value = _component_func(nom=nom, key=key, default=0)
    return component_value
###############################################################
import os
import numpy as np
import streamlit as st
import time
#from pre_processing import Processing_sig
from prediction import Predict


nom='hello'

num_clicks = my_component(nom)
st.set_option('deprecation.showfileUploaderEncoding', False)

def main():

    st.sidebar.text('Signle voice or a Conversation !')
    radios=st.sidebar.radio("",("Single","Conversation"))
    st.sidebar.text('How would you like to predict voice ?')
    option = st.sidebar.selectbox('',('Upload', 'Recording'))

    prdd=Predict(sample_rate=16000,model_path="C:/Users/zenno/Downloads/my_model_NN_MFCC_darija94_63.h5")
    if radios=='Conversation' and option == 'Upload':

        uploaded_file = st.file_uploader("")
        if st.button("Predict"):
            if uploaded_file is not None:
                speakers1,speakers2,speakers3 = prdd.predict_from_conversation_file(file=uploaded_file)
                st.success("The speakers Talking in this conversation are : {} , {} and {}".format(speakers1,speakers2,speakers3))
            else:
                st.error(" Warning please Drop or Upload a audio file before !")


    elif radios=='Single' and option=='Upload':

        uploaded_file = st.file_uploader("")
        if st.button("Predict"):
            if uploaded_file is not None:
                 pred,persent = prdd.predict_from_file(file=uploaded_file)
                 st.success("The speaker is {} with a certainty of  {:.1f} %".format(pred,persent))
            else:
                 st.error(" Warning please Drop or Upload a audio file before !")


    elif radios=='Single' and option=="Recording":
       
    
        Duration = st.slider("Set the duration in second (s) please ! ", 20, 60)
       

        if st.button("Start Recording"):
            st.image("wk.128.png",width=50)
            with st.spinner("Recording..."):
	            file=prdd.record(file="pre_reco.wav",duration=Duration)
            st.audio(file)
        if st.button("Predict"):
            pred, persent = prdd.predict_from_file(file="pre_reco.wav")
            st.success("The speaker is {}  with a certainty of {:.1f} %".format(pred, persent))

    else:
      
        Duration = st.slider("Set the duration in second (s) please ! ", 20, 60)
        
        if st.button("Start Recording"):
            st.image("wk.128.png",width=80)
            with st.spinner("Recording..."):
                file = prdd.record(file="pre_reco.wav")
        st.audio(file)
        if st.button("Predict"):
            speaker1, speaker2 =prdd.predict_from_conversation_file(file="pre_reco.wav",duration=Duration)
            st.success("The speakers Talking in this conversation are :  {} and {}".format(speaker1, speaker2))




if __name__ == "__main__":


    main()





