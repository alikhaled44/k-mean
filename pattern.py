#plotting is used for explanation in the site in which the original code is located , But his steps were also explained

## Initialisation

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline


# Create DataFrame
df = pd.DataFrame({
    'x': [12, 20, 28, 18, 29, 33, 24, 45, 45, 52, 51, 52, 55, 53, 55, 61, 64, 69, 72],
    'y': [39, 36, 30, 52, 54, 46, 55, 59, 63, 70, 66, 63, 58, 23, 14, 8, 19, 7, 24]
})


#generate the same random number every time with the same seed value
np.random.seed(200)

#Number of clusters K
k = 3

# centroids[i] = [x, y]
# np.random.randint(0, 80) => Generated random number will be between 0 to 80 
centroids = {
    i+1: [np.random.randint(0, 80), np.random.randint(0, 80)]
    for i in range(k)
}


#using for plotting

#set figure size 
fig = plt.figure(figsize=(5, 5))

#Give each centroid a different color
plt.scatter(df['x'], df['y'], color='k')
colmap = {1: 'r', 2: 'g', 3: 'b'}
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
#set the x,y limits    
plt.xlim(0, 80)
plt.ylim(0, 80)
#display figure
plt.show()

#-----------------------------------------------------------------------------

## Assignment Stage

def assignment(df, centroids):
    for i in centroids.keys():
        # calculate the minimum distance
        # sqrt((x1 - x2)^2 - (y1 - y2)^2)
        df['distance_from_{}'.format(i)] = (
            np.sqrt(
                (df['x'] - centroids[i][0]) ** 2
                + (df['y'] - centroids[i][1]) ** 2
            )
        )
     #create table with following elements 
    centroid_distance_cols = ['distance_from_{}'.format(i) for i in centroids.keys()]
    df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis=1)
    df['closest'] = df['closest'].map(lambda x: int(x.lstrip('distance_from_')))
    df['color'] = df['closest'].map(lambda x: colmap[x])
    return df
#print first five items as example
         #   x   y  distance_from_1  distance_from_2  distance_from_3  closest color
#0  12  39        26.925824        56.080300        56.727418              1     r
#1  20  36        20.880613        48.373546        53.150729              1     r
#2  28  30        14.142136        41.761226        53.338541              1     r
#3  18  52        36.878178        50.990195        44.102154              1     r
#4  29  54        38.118237        40.804412        34.058773              3     b
print(df.head())

#using for plotting    

#set figure size 
fig = plt.figure(figsize=(5, 5))
#plot data points on horizontal and vertical axis
plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
#set the x,y limits        
plt.xlim(0, 80)
plt.ylim(0, 80)
#display figure
plt.show()

#-----------------------------------------------------------------------------

## Update Stage

import copy
#copy centroids 
old_centroids = copy.deepcopy(centroids)
#update centroids 
def update(k):
    for i in centroids.keys():
        centroids[i][0] = np.mean(df[df['closest'] == i]['x'])
        centroids[i][1] = np.mean(df[df['closest'] == i]['y'])
    return k

centroids = update(centroids)
#using for plotting
#set figure size
fig = plt.figure(figsize=(5, 5))
# set full window axes to ax 
ax = plt.axes()
#plot data points on horizontal and vertical axis
plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
#set the x,y limits       
plt.xlim(0, 80)
plt.ylim(0, 80)
#Draw an arrow from the old location to the new one
for i in old_centroids.keys():
    old_x = old_centroids[i][0]
    old_y = old_centroids[i][1]
    dx = (centroids[i][0] - old_centroids[i][0]) * 0.75
    dy = (centroids[i][1] - old_centroids[i][1]) * 0.75
    ax.arrow(old_x, old_y, dx, dy, head_width=2, head_length=3, fc=colmap[i], ec=colmap[i])
#display figure
plt.show()
#-----------------------------------------------------------------------------
## Repeat Assigment Stage

df = assignment(df, centroids)

#using for plotting
#set figure size
fig = plt.figure(figsize=(5, 5))
#plot data points on horizontal and vertical axis
plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
#set the x,y limits       
plt.xlim(0, 80)
plt.ylim(0, 80)
#display figure
plt.show()

#-----------------------------------------------------------------------------
