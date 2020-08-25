import librosa
import numpy as np
from audiolazy import lpc


class Features_extractor:

    def __init__(self, sample_rate=16000, frame_duration=0.025, frame_shift=0.010,n_mel=128,n_mfcc=20,duration=30,
                 mfcc_delta=False,mfcc_delta_delta=False,order=13):

        self.sample_rate = sample_rate
        self.n_fft = int(np.floor(frame_duration * sample_rate))
        self.hop_length = int(np.floor(frame_shift * sample_rate))
        self.n_mel = n_mel
        self.n_mfcc = n_mfcc
        self.sample = int((duration*sample_rate)/3)
        self.mfcc_delta = mfcc_delta
        self.mfcc_delta_delta = mfcc_delta_delta
        self.order=order


    def get_MFCCs(self,signal):

        if len(signal) >= self.sample:
            signal = signal[:self.sample]
        mfcc = librosa.feature.mfcc(signal, n_mfcc=self.n_mfcc, hop_length=self.hop_length,
                                    n_fft=self.n_fft)
        if self.mfcc_delta:
                mfcc=librosa.feature.delta(mfcc,order=1)

        elif self.mfcc_delta_delta:
                mfcc=librosa.feature.delta(mfcc,order=2)

        mfcc_features = np.mean(mfcc, 1)
        mfcc_features = (mfcc_features - np.mean(mfcc_features)) / np.std(mfcc_features)

        return mfcc_features.T

    def LPC(self,signal):

        filt = lpc(signal, self.order)
        lpc_features = filt.numerator[1:]

        return np.array(lpc_features)