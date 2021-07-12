# %% Imports

# Don't see a "Run Cell" option above "# %% Imports" ?
# Try VS Code!

import numpy as np
import sounddevice as sd
import re
import matplotlib.pyplot as plt
from pylab import *
import time
import soundfile as sf
import math

# Set up empty arrays for the temps
date = []
cpu = []
gpu = []
system1 = []



# %% Fill the arrays with the values.

# Depending on your setup, you might want to change this to
# different columns and assign it to different arrays.
with open("data.csv", "r") as f:
    for line in f:
        values = line.split(",")
        cpu.append(values[19])
        gpu.append(values[13])
        system1.append(values[17])



# %% Custom function to scale an array up by a factor of 2

def make_bigger(np_array):
    length = len(np_array) * 2
    new = np.zeros(length)
    for i in range(len(np_array)):
        new[2*i] = np_array[i]
        if i+1 < len(np_array):
            new[2*i+1] = (np_array[i] + np_array[i+1])/2
        else:
            new[2*i+1] = np_array[i]
    return new



# %% (optional) Test if the custom fuction works

x = np.array([1,0,-1])
print(make_bigger(x))



# %% Generate new arrays where the modified data is stored

m = max(len(cpu), len(gpu), len(system1)) # get max lenght, just for beinf sure
s_cpu = np.zeros((m, ))
s_gpu = np.zeros((m, ))
s_sys = np.zeros((m, ))



# %% Convert to float & scale the temps to a better sounding range

# you might want to modify this depending on your temps
base = -0
fact = 6

# Trim the spaces from the csv to convert from strings to floats
for i in range(m):
    s_cpu[i] = (float(re.sub("\\n", "", cpu[i])) + base) * fact
    s_gpu[i] = (float(re.sub("\\n", "", gpu[i])) + base) * fact
    s_sys[i] = (float(re.sub("\\n", "", system1[i])) + base) * fact



# %% (optional) See where the min and max values are & max range

print(min(s_cpu), max(s_cpu))
print(min(s_gpu), max(s_gpu))
print(min(s_sys), max(s_sys))

print(max(s_cpu)-min(s_cpu))
print(max(s_gpu)-min(s_gpu))
print(max(s_sys)-min(s_sys))



# %% Generate the sounds

SR = 44100
length_sec = 5

n = SR * length_sec # number of points

# Scale the array up once and assign it to a frequence_device array
f_cpu = make_bigger(s_cpu)
f_gpu = make_bigger(s_gpu)
f_sys = make_bigger(s_sys)

# Some math to get the correct sine wave
t = linspace(0,length_sec,len(f_cpu))
dt = t[1] - t[0] # needed for integration

phi_cpu = 2 * math.pi * cumsum(f_cpu) * dt # integrate to get phase
phi_gpu = 2 * math.pi * cumsum(f_gpu)* dt # integrate to get phase
phi_sys = 2 * math.pi * cumsum(f_sys)* dt # integrate to get phase

wave_cpu = sin(phi_cpu)
wave_gpu = sin(phi_gpu)
wave_sys = sin(phi_sys)



# %% Generate a plot and play each sound

plot(t, wave_cpu)
xlabel('Time (s)')
ylim([-1.2, 1.2])
grid()
show()
sd.play(wave_cpu, 44100)
sd.wait()

time.sleep(3)

plot(t, wave_gpu)
xlabel('Time (s)')
ylim([-1.2, 1.2])
grid()
show()
sd.play(wave_gpu, 44100)
sd.wait()

time.sleep(3)

plot(t, wave_sys)
xlabel('Time (s)')
ylim([-1.2, 1.2])
grid()
show()
sd.play(wave_sys, 44100)
sd.wait()

# %% (optional) Save to soundfiles
 
sf.write("Apfel.wav", wave_cpu, SR)
sf.write("Banane.wav", wave_gpu, SR)
sf.write("Kiwi.wav", wave_sys, SR)
# %%
