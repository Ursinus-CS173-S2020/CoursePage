import numpy as np
import scipy.io as sio
import scipy.io.wavfile


Fs = 44100
L = 115
N = 2*Fs
x = np.zeros(N)
x[0:L*2] = np.random.rand(L*2) - 0.5
decay = 0.98
for i in range(Fs):
    x[i+L] = decay*0.5*(x[i]+x[i+1])
sio.wavfile.write("out.wav", Fs, x)
