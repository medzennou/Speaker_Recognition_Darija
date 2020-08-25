import json
import numpy as np
import librosa
import streamlit as st
import soundfile as sf
import sounddevice as sd
import tensorflow as tf
import time
from pre_processing import Processing_sig

class Predict:

    def __init__(self,model_path="C:/Users/zenno/Downloads/my_model_NN_MFCC_darija95_10.h5",sample_rate=16000, 
                 json_path="C:/Users/zenno/OneDrive/Bureau/json_data_mffcs_darija2.json",duration=30):
       
        self.model       = tf.keras.models.load_model(model_path)
        self.sample_rate = sample_rate
        self.json_path   = json_path
        self.duration    = duration

    def predict_from_file(self,file):
        pre=Processing_sig(preemphasis=0.95)
        unknow_speaker = pre.pre_process(file=file)
        speaker = np.array(unknow_speaker)
        speaker=speaker[np.newaxis,...]
        speaker=speaker[...,np.newaxis]
        prdict = self.model.predict([speaker])
        prd = np.argmax(prdict)
        with open(self.json_path, "r") as jp:
            data = json.load(jp)
        speaker_json = data["speakers"]
        return speaker_json[prd],np.max(prdict) * 100

    def predict_from_conversation_file(self,file):
        pre=Processing_sig(preemphasis=0.95)
        unknow_speaker = pre.pre_process(file=file)
        speaker = np.array(unknow_speaker)
        speaker=speaker[np.newaxis,...]
        speaker=speaker[...,np.newaxis]
        prdict = self.model.predict([speaker])
        ar = prdict.flatten()
        indx = ar.argsort()[-3:][::-1]
        with open(self.json_path, "r") as jp:
            data = json.load(jp)
        speakers = data["speakers"]
        return speakers [indx[0]],speakers [indx[1]],speakers [indx[2]]
    
    
    def record(self,file):
        # Add a placeholder
        #latest_iteration = st.empty()
        bar = st.progress(0)
            #while self.duration:
            #mins, secs = divmod(0,duration)
            #timer = '{:02d}:{:02d}'.format(mins, secs)
        for i in range(100):    
            #st.write(timer, end="\r")
            #time.sleep(0.1)
            #duration -= 1
        #st.write('Blast Off!!!')
        
            # Update the progress bar with each iteration.
            #latest_iteration.text(f'Iteration {i + 1}')
            bar.progress(i + 1)
            time.sleep(0.1)
        my_rec = sd.rec(int(self.sample_rate * self.duration), samplerate=self.sample_rate, channels=1, blocking=True)

        sd.wait()
        
        sf.write(file, my_rec, self.sample_rate)

        return file
