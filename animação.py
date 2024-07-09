'''
Animação
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
#from matplotlib.animation import FFMpegWriter

plt.style.use('default')

%matplotlib qt

fig = plt.figure()

ln, = plt.plot([], [], 'k-')
ln2, = plt.plot([],[], 'm--')

plt.xlim(-5,5)
plt.ylim(-5,5)

def func(x):
    return np.sin(x)*3

def func2(x):
    return np.cos(x)*3


metadata = dict(title='Movie', artist ='Elbruno')
#writer = FFMpegWriter(fps=15, metadata=metadata)
writer = PillowWriter(fps=15, metadata=metadata)

xlist = []
ylist = []

x2list = []
y2list = []

with writer.saving(fig, "sinWave.gif",100):
    for xval in np.linspace(-5,5,100):
        xlist.append(xval)
        ylist.append(func(xval))
        
        x2list.append(xval)
        y2list.append(func2(xval))

        ln.set_data(xlist,ylist)
        ln2.set_data(x2list,y2list)
        writer.grab_frame()










