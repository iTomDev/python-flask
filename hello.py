import numpy as np
import scipy as sp
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

def hello():
    return "Hello World!"
def simpleSum(a, b):
    return a+b

def spatialDemo():
    points = np.array([
        [2,4],
        [3,4],
        [3,0],
        [2,2],
        [4,1]])
    simplices = Delaunay(points).simplices
    plt.triplot(points[:.0], points[:,1], simplices)
    plt.scatter(points[:,0], points[:,1], color='r')
    plt.show()