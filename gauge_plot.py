import os, sys
import matplotlib
from matplotlib import cm
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Wedge, Rectangle


def degree_range(n): 
    start = np.linspace(0,180,n+1, endpoint=True)[0:-1]
    end = np.linspace(0,180,n+1, endpoint=True)[1::]
    mid_points = start + ((end-start)/2.)
    print ("START AND END")
    print (start,end)
    print (np.c_[start, end])
    return np.c_[start, end], mid_points


def degree_range_2(n): 
    start = np.linspace(0,180,n+1, endpoint=True)[0:-1]
    end = np.linspace(0,180,n+1, endpoint=True)[1::]
    mid_points = start + ((end-start)/2.)
    return np.c_[start, end], mid_points


def rot_text(ang): 
    rotation = np.degrees(np.radians(ang) * np.pi / np.pi - np.radians(90))
    return rotation

def gauge(labels=['','',''],colors='jet_r', arrow=1, title='', fname=False): 
    N = 3*len(labels)   
    if arrow > N: 
        raise Exception("\n\nThe category ({}) is greated than the length\nof the labels ({})".format(arrow, N))     
    if isinstance(colors, str):
        cmap = cm.get_cmap(colors, N)
        cmap = cmap(np.arange(N))
        colors = cmap[::-1,:].tolist()
    if isinstance(colors, list): 
        if len(colors) == N:
            colors = colors[::-1]
        else: 
            raise Exception("\n\nnumber of colors {} not equal to number of categories{}\n".format(len(colors), N))  
    fig, ax = plt.subplots()
    ang_range, mid_points = degree_range(N)
    labels = labels[::-1]   
    patches = []
    for ang, c in zip(ang_range, colors): 
        # sectors
        patches.append(Wedge((0.,0.), .4, *ang, facecolor='w', lw=2))
        # arcs
        patches.append(Wedge((0.,0.), .4, *ang, width=0.10, facecolor=c, lw=2, alpha=0.5))    
    [ax.add_patch(p) for p in patches]   
    for mid, lab in zip(mid_points, labels): 
        ax.text(0.35 * np.cos(np.radians(mid)), 0.35 * np.sin(np.radians(mid)), lab, 
            horizontalalignment='center', verticalalignment='center', fontsize=14, 
            fontweight='bold', rotation = rot_text(mid))
    r = Rectangle((-0.4,-0.1),0.8,0.1, facecolor='w', lw=2)
    ax.add_patch(r)
    ax.text(0, -0.05, title, horizontalalignment='center', 
         verticalalignment='center', fontsize=22, fontweight='bold')  
    pos = mid_points[abs(arrow - N)]    
    ax.arrow(0, 0, 0.225 * np.cos(np.radians(pos)), 0.225 * np.sin(np.radians(pos)), 
                 width=0.02, head_width=0.04, head_length=0.05, fc='k', ec='k')  
    #ax.add_patch(Circle((0, 0), radius=0.02, facecolor='k'))
    #ax.add_patch(Circle((0, 0), radius=0.01, facecolor='w', zorder=11))  
    ax.set_frame_on(False)
    ax.axes.set_xticks([])
    ax.axes.set_yticks([])
    ax.axis('equal')
    plt.tight_layout()
    if fname:
        fig.savefig(fname, dpi=200)

levels = [0.4531559840832568,0.48976001666666663,0.49721371666666664]
levels_array = np.array(levels)*100
arrowi = []
names = ["test_source.pdf","test_target_1.pdf","test_target_4.pdf"]
titles = ['Cumulative charge source [Ah]','Cumulative charge target 1 [Ah]','Cumulative charge target 4 [Ah]']
for i in levels_array:
    if i < 12:
        arrowi.append(1)
    elif i > 12.1 and i < 22:
        arrowi.append(2)
    elif i > 22.1 and i < 33:
        arrowi.append(3)
    elif i > 33.1 and i < 44:
        arrowi.append(4)
    elif i > 44.1 and i < 55:
        arrowi.append(5)
    elif i > 55.1 and i < 66:
        arrowi.append(6)
    elif i > 66.1 and i < 77:
        arrowi.append(7)
    elif i > 77.1 and i < 88:
        arrowi.append(8)
    elif i > 88.1:
        arrowi.append(9)

for i in range(len(arrowi)): 
    gauge(labels=['','',''], 
      colors=['#007A00','#007A00','#007A00','#FFCC00','#FFCC00','#FFCC00','#ED1C24','#ED1C24','#ED1C24'], arrow=arrowi[i], title=titles[i],fname=names[i])



