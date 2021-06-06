import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#USE: Create an array structure for rings.
#INPUT: a df of row length 1 with the first column as the current metric value and the second colum is the target metric value
#OUTPUT: an aray of arrays representing each ring
def calculate_rings(df,i):
  if df.iloc[i,0] < df.iloc[i,1]:
    rings=[[df.iloc[i,0],df.iloc[i,1]-df.iloc[i,0]],[0,0]]
  elif df.iloc[i,0] / df.iloc[0,1] < 2:
    rings=[[df.iloc[i,0],0],[df.iloc[i,0] % df.iloc[i,1], df.iloc[i,1]-df.iloc[i,0] % df.iloc[0,1]]]
  else:
    rings = [[0,0],[0,0]]
  return rings
#USE: Create a center label in the middle of the radial chart.
#INPUT: a df of row length 1 with the first column as the current metric value and the second column is the target metric value
#OUTPUT: the proper text label
def add_center_label(df,i):
    percent = str(int(1.0*df.iloc[i, 0]/df.iloc[i, 1]*100)) + '%'
    return plt.text(0,
           0.2,
           percent,
           horizontalalignment='center',
           verticalalignment='center',
           fontsize = 40,
           family = 'sans-serif')
#USE: Create a dynamic outer label that servers a pointer on the ring.
#INPUT: a df of row length 1 with the first column as the current metric value and the second column is the target metric value
#OUTPUT: the proper text label at the apropiate position
def add_sub_center_label(df,i):
    amount = str(int(df.CHARGE_FOIL.iloc[i])) + " uAh" 
    return plt.text(0,
            -.1,
            amount,
            horizontalalignment='center',
            verticalalignment='top',
            fontsize = 22,family = 'sans-serif')

def add_sub_sub_center_label(df,i):
    amount = "Foil " + str(int(df.FOIL.iloc[i])) + " T " + str(int(df.TARGET.iloc[i]))
    #amount = "Max: 109.8 Ah"
    return plt.text(0,
            -.4,
            amount,
            horizontalalignment='center',
            verticalalignment='top',
            fontsize = 22,family = 'sans-serif')

def create_radial_chart(df,ind, color_theme = 'Red'):
  # base styling logic
  color = plt.get_cmap(color_theme + 's')
  ring_width = 0.3
  outer_radius = 1.5
  inner_radius = outer_radius - ring_width
  # set up plot
  ring_arrays = calculate_rings(df,ind)
  fig, ax = plt.subplots()
  if df.iloc[0, 0] > df.iloc[0, 1]:
    ring_to_label = 0
    outer_edge_color = None
    inner_edge_color = 'white'
  else:
    ring_to_label = 1
    outer_edge_color, inner_edge_color = ['white', None]
  # plot logic
  outer_ring, _ = ax.pie(ring_arrays[0],radius=1.5,
                    colors=[color(0.7), color(0.15)],
                    startangle = 90,
                    counterclock = False)
  plt.setp( outer_ring, width=ring_width, edgecolor=outer_edge_color)
  inner_ring, _ = ax.pie(ring_arrays[1],
                         radius=inner_radius,
                         colors=[color(0.55), color(0.05)],
                         startangle = 90,
                         counterclock = False)
  plt.setp(inner_ring, width=ring_width, edgecolor=inner_edge_color)
    # add labels and format plots
  add_center_label(df,ind)
  add_sub_center_label(df,ind)
  add_sub_sub_center_label(df,ind)
  ax.axis('equal')
  plt.margins(0,0)
  plt.autoscale('enable')
  return plt
