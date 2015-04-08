# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 12:01:19 2015

@author: aloverso
"""
import matplotlib.pyplot as plt
import numpy as np

                          #[1,m,a,p,e,m,c,h,u,d,r,p,m,s,e,i,t,w]
classes = { 'desnat':      [1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,1,1],
            'softdes':     [1,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,1,0],
            'modsim':      [1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            'instrum':     [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            'grandes':     [0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,1],
                          #[1,m,a,p,e,m,c,h,u,d,r,p,m,s,e,i,t,w]
            'apps':        [0,0,0,1,0,0,0,1,1,1,1,0,1,0,0,0,1,1],
            'calc1':       [1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
            'electrical':  [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            'motion':      [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0],
            'datasci':     [0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
                          #[1,m,a,p,e,m,c,h,u,d,r,p,m,s,e,i,t,w]
            'procfab':     [0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0],
            'calc2':       [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            'matsci':      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0],
            'biotech':     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
            'nandtetris':  [0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
                          #[1,m,a,p,e,m,c,h,u,d,r,p,m,s,e,i,t,w]
            'modcon':      [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            'em':          [0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            'techent':     [0,0,0,0,0,0,0,0,1,0,1,1,1,1,1,1,1,1],
            'socialntwk':  [0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0,1],
            'heattrans':   [0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0],
                          #[1,m,a,p,e,m,c,h,u,d,r,p,m,s,e,i,t,w]
            'agilecollab': [0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1],
            'cloud':       [0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
            'webtech':     [0,0,1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0],
            'embedded':    [0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
                          #[1,m,a,p,e,m,c,h,u,d,r,p,m,s,e,i,t,w]
            'softsol':     [0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            'bigdata':     [0,1,0,1,0,1,1,0,0,0,1,0,0,1,0,0,0,0],
            'digitalgames':[0,0,0,1,0,0,0,1,1,0,0,1,0,0,0,0,1,0],
            'designcomp':  [0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0],
                          #[1,m,a,p,e,m,c,h,u,d,r,p,m,s,e,i,t,w]
            'hackertech':  [0,0,1,1,0,0,1,0,0,0,0,0,0,1,1,0,0,1],
            'supercomp':   [0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
            'virtreal':    [0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,1,0],
            'robo':        [0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0],
            'thinkos':     [0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0]}

original = [['desnat','softdes','modsim','instrum','grandes'],
      ['datasci','calc1','apps','motion','electrical'],
    ['procfab','calc2','matsci','biotech','nandtetris'],
    ['modcon','em','techent','socialntwk','heattrans'],
    ['agilecollab','cloud','webtech','embedded'],
    ['softsol','bigdata','digitalgames','designcomp'],
    ['hackertech','supercomp','virtreal','robo']]

'''
We designed this one based on adding a thinkOS clas that has to come
before supercomputing. We moved ACD earlier, but it could be switched with
NAND/Tetris.  WebTech is alos earlier to spread out social networks and 
heat transfer in later semesters.  ThinkOS, cloud comp, and embedded comp
are all together to give a spanning look at computing, which is good coming
right after NAND/tetris.
'''
horizcontent = [['desnat','softdes','modsim','instrum','grandes'],
      ['datasci','calc1','apps','motion','electrical'],
    ['procfab','calc2','matsci','biotech','agilecollab'],
    ['modcon','em','techent','nandtetris','webtech'],
    ['thinkos','cloud','heattrans','embedded'],
    ['softsol','bigdata','digitalgames','socialntwk'],
    ['hackertech','supercomp','designcomp','robo']]
    
initial = [['desnat','softdes','modsim','instrum','grandes'],
      ['datasci','calc1','apps','motion','electrical'],
    ['procfab','calc2','matsci','nandtetris','agilecollab'],
    ['modcon','em','techent','designcomp','softsol'],
    ['biotech','cloud','webtech','embedded','socialntwk'],
    ['heattrans','bigdata','digitalgames','hackertech'],
    ['supercomp','virtreal','robo']]


Z = np.zeros((18,7))
curr = horizcontent
sem=0
comp=0
for semester in curr:
    for course in semester:
        compet = classes[course]
        for val in compet:
            Z[comp][sem]+=val
            comp+=1
        comp=0
    sem+=1
    
print(Z)

column_labels = ['l2l','math','analysis/alg','prog','circuits/ee','mem/storage','conn/netwoks','hci',
                 'users','design proc','req spec','prod dev','market aware',
                 'social/hist','ethics','inter-discp','teamwork','written/oral']
row_labels = list('1234567')

fig, ax = plt.subplots()
heatmap = ax.pcolor(Z, cmap=plt.cm.Blues)

# put the major ticks at the middle of each cell
ax.set_xticks(np.arange(Z.shape[1])+0.5, minor=False)
ax.set_yticks(np.arange(Z.shape[0])+0.5, minor=False)

# want a more natural, table-like display
ax.invert_yaxis()
ax.xaxis.tick_top()
#
ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(column_labels, minor=False)
plt.show()
