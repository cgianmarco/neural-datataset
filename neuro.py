import scipy.io
import numpy as np
from matplotlib import pyplot as plt
import time

mat = scipy.io.loadmat('/Users/gianmarco/Downloads/crcns-ringach-data/neurodata/ac1/ac1_u004_000.mat')

frame = 1

electrod = 1

pepANA = mat['pepANA']

dataset = pepANA[0][0]

frame_record = dataset['listOfResults'][0][frame]

repeat_record = frame_record[0][0]['repeat'][0][0]

electrode_data = dataset['listOfResults'][0][frame][0][0]['repeat'][0][0]['data'][0][0][0][electrod]

intervals = dataset['listOfResults'][0][frame][0][0]['repeat'][0][0]['data'][0][0][0][electrod][0][0]

values = dataset['listOfResults'][0][frame][0][0]['repeat'][0][0]['data'][0][0][0][electrod][0][1]

values = np.transpose(values)

for i in range(len(values)):
    fig = plt.figure(i)
    plt.ylim([-150,150])
    plt.plot(values[i])    
    # time.sleep(1)
    fig.savefig('plots/img' + str(i) + ".png")
    print i
    
    
