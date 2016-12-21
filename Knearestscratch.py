import numpy as np 
from math import sqrt
import matplotlib.pyplot as plt 
from matplotlib import style 
from collections import Counter 
import warnings 

style.use('fivethirtyeight')

dataset = {'k':[[1,2],[2,3],[3,1]],'r' : [[6,5],[7,7],[8,6]]}
new_features = [5,7]

#iterating through a 2D array 
for i in dataset:
	for ii in dataset[i]:
		plt.scatter(ii[0],ii[1], s=100, color=i)

plt.show()