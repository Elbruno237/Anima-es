import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import PillowWriter

%matplotlib qt

metadata = dict(title ='Movie', artist = 'Bruno')
writer = PillowWriter(fps = 15, metadata = metadata )

fig, ax = plt.subplots()
#ln, = ax.plot([],[],'w-')

xlist = np.linspace(0, 500, 100)

def func(x):
    return np.log(x)*2

with writer.saving(fig, 'anime.gif', 100):
    for x in xlist:
        #print(x)
        y = func(x)
        ax.clear()
        ax.plot(x, y, 'ro')
        ax.set_xlim(0,500)
        ax.set_ylim(0,20)
        
        fig.canvas.draw()  
        writer.grab_frame()
        
with writer.saving(fig, 'anime2.gif', 100):
    for i, x in enumerate(xlist):
        y = func(x)
        ax.clear()
        ax.plot(xlist[:i+1], func(xlist[:i+1]), 'r-')  # Plota a linha até o ponto atual
        ax.plot(x, y, 'ro')  # Plota o ponto atual
        ax.set_xlim(0, 500)
        ax.set_ylim(0, 20)
        
        fig.canvas.draw()
        writer.grab_frame()

ax.clear()
with writer.saving(fig, 'anime3.gif', 100):
    for x in xlist:
        #print(x)
        y = func(x)
        #ax.clear()
        ax.plot(x, y, 'ro')
        ax.set_xlim(0,500)
        ax.set_ylim(0,20)
        
        fig.canvas.draw()  
        writer.grab_frame()
