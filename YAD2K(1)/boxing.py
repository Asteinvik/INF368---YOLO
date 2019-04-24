import os
import random
from PIL import Image
from math import floor, sqrt
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans






boxx = []
boxy = []
boxes = []
with open('boxes.txt','r') as f:
	file = f.read()
	lines = file.split('\n')

	for line in lines:
		row = line.split(",")
		posx0= int(row[1])
		posy0= int(row[2])
		posx= int(row[3])-posx0
		posy= int(row[4])-posy0
		boxx.append(posx)
		boxy.append(posy)
		boxes.append([posx,posy])


kmeans = KMeans(n_clusters=4, random_state=0).fit(boxes)
print(kmeans.cluster_centers_)

plt.figure(1)
plt.scatter(boxx,boxy)
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1])
plt.title('Sice of boxes')
plt.ylabel('Y')
plt.xlabel('X')
plt.savefig('box'+'.png')
#plt.show()
plt.close()
