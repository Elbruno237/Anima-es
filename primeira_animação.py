import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import PillowWriter


metadata = dict(title ='Movie', artist = 'Bruno')
writer = PillowWriter(fps = 15, metadata = metadata )


fig, ax = plt.subplots()
#ln, = ax.plot([],[],'w-')

xlist = np.linspace(0, 500, 100)

def func(x):
    return np.log(x)*2

with writer.saving(fig, 'anime.gif',100):
    for x in xlist:
        print(x)
        y = func(xlist)
        
        ax.plot(x, y, 'ro')
        ax.set_xlim(0,500)
        ax.set_ylim(0,20)
        
        writer.grab_frame()
        
