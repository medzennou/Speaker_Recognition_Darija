import librosa
import librosa.display
import numpy as np
import pandas as pd
from features_extraction import Features_extractor

class Processing_sig:

    def __init__(self, sample_rate=16000, frame_duration=0.025, frame_shift=0.010, preemphasis=0.97,
                 e=0.0000001):
        self.sample_rate = sample_rate
        self.win_size = int(np.floor(frame_duration * sample_rate))
        self.win_shift = int(np.floor(frame_shift * sample_rate))
        self.preemphasis = preemphasis
        self.hamwin = np.hamming(self.win_size)
        self.e=e

    def dither(self, signal):
        n = 2*np.random.rand(signal.shape[0])-1
        n *= 1/(2**15)

        return wav + n

    def pre_emphasis(self,signal):
        emphasized_signal = np.append(signal[0], signal[1:] - self.preemphasis * signal[:-1])

        return emphasized_signal

    def framing(self,signal):
        signal_length = len(signal)
        num_frames = int(np.ceil(float(np.abs(signal_length - self.win_size) / self.win_shift)))
        frames = np.zeros([self.win_size, num_frames])
        indices = np.tile(np.arange(0, self.win_size), (num_frames, 1)) + np.tile(
            np.arange(0, num_frames * self.win_shift, self.win_shift), (self.win_size, 1)).T
        frames = signal[indices]
        frames = frames * self.hamwin

        return frames

    def deframing(self,frames):
        num_frames = frames.shape[0]
        indices = np.tile(np.arange(0, self.win_size), (num_frames, 1)) + np.tile(
            np.arange(0, num_frames * self.win_shift, self.win_shift), (self.win_size, 1)).T
        padlen = (num_frames - 1) * self.win_shift + self.win_size
        nwsignal = np.zeros(padlen)
        remv_win = np.zeros(padlen)
        for i in range(num_frames):
            remv_win[indices[i, :]] = remv_win[indices[i, :]] +self.hamwin + self.e
            nwsignal[indices[i, :]] = nwsignal[indices[i, :]] + frames[i, :]
        nwsignal = nwsignal / remv_win

        return nwsignal

    def short_time_Energy(self,frames):

        return sum([abs(x) ** 2 for x in frames])

    def Zero_crossing_rate(self,frame):
        zr = 0
        for k in range(1, len(frame)):
            if (0.5 * abs(np.sign(frame[k]) - np.sign(frame[k - 1]))) == 1:
                zr += 1

        return zr / len(frame)

    def VAD(self,signal):
        frames = self.framing(signal)
        framess = np.array([])
        index = []
        for i, f in enumerate(frames):
            if (self.short_time_Energy(f) < 0.005 and self.Zero_crossing_rate(f) > 0.10):
                index.append(i)
        framess = np.delete(frames, index, 0)
        new_signal = self.deframing(framess)

        return new_signal


    def pre_process(self,file):

        signal, sample_rate = librosa.load(file, sr=self.sample_rate)

    # normalise the signal
    #signal = signal / np.mean(signal)

    # Pre_emphasis
        signal = self.pre_emphasis(signal)

    # VAD
        signal = self.VAD(signal)

    # extract MFCC
        feat=Features_extractor()
        mfcc_features = feat.get_MFCCs(signal)

        return mfcc_features.T