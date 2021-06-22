import scipy.io.wavfile as wavfile
import numpy as np
import matplotlib.pyplot as plt
import glob
import subprocess

plt.figure(figsize=(10, 2))
for f in glob.glob("*.wav"):
    prefix = f[0:-4]
    fs, x = wavfile.read(f)
    x = x/32768
    t = np.arange(x.size)/fs
    plt.clf()
    plt.plot(x)
    plt.xlim([0, 2000])
    plt.xlabel("Array Index")
    plt.ylabel("Value")
    plt.title(prefix)
    plt.savefig("%s.svg"%prefix, bbox_inches='tight')
    subprocess.call(["ffmpeg", "-i", f, "%s.mp3"%prefix])