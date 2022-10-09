import sounddevice
from scipy.io.wavfile import write
import time

begining = 3
#sample rate
fs=44100

second = int(input("Enter the recording Time in second : "))
for i in range(3) :
    print("The record will begin in ", i, "s")
    time.sleep(5)
print("Recording......\n")
record_voice=sounddevice.rec(int(second * fs), samplerate=fs, channels=2)
sounddevice.wait()
write("Myrecording.wav",fs,record_voice)
print("Recording is done please check your folder to listen recording")