#import numpy as np
#import scipy as sp
# from scipy.spatial import Delaunay
# import matplotlib.pyplot as plt
import sqlite3
import os

def hello():
    return "Hello World!"

def simpleSum(a, b):
    return (a+b)

# def spatialDemo():
#     points = np.array([
#         [2,4],
#         [3,4],
#         [3,0],
#         [2,2],
#         [4,1]])
#     simplices = Delaunay(points).simplices
#     plt.triplot(points[:.0], points[:,1], simplices)
#     plt.scatter(points[:,0], points[:,1], color='r')
#     plt.show()
    
def sqlDemoInit():
    os.remove('test.db')
    conn = sqlite3.connect("test.db")
    conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')
    conn.close()
    
def sqlDemoAddData():
    conn = sqlite3.connect('test.db')
    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (55, 'Paul', 32, 'California', 20000.00 )");
    conn.commit()
    conn.close()
    
def sqlDemoReadback():
    conn = sqlite3.connect('test.db')
    cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
    for row in cursor:
        return row[0] # ID
    conn.close()
    