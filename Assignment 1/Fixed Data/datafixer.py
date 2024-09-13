import numpy as np

name = 'Upstream Drag'
data = np.genfromtxt('Assignment 1/Fixed Data/'+name+'.csv', delimiter=',', skip_header=1)
np.savetxt('Assignment 1/Fixed Data/'+name+'.txt', data, delimiter=' ', fmt='%s')
