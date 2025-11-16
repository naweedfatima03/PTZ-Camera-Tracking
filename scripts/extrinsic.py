# strore the extrinsic parameters of the camera 
# the function returns extrinsic parameters in other files

import numpy as np

def Rotx(theta_x):
    return  np.array([
            [1,     0,                              0], 
            [0,     np.cos(theta_x), -np.sin(theta_x)], 
            [0,     np.sin(theta_x),  np.cos(theta_x)]
            ])

def Roty(theta_y):
    return  np.array([
            [np.cos(theta_y),       0,  np.sin(theta_y)], 
            [0,                     1,                0], 
            [-np.sin(theta_y),      0,  np.cos(theta_y)]
            ])

def Rotz(theta_z):
    return  np.array([
            [np.cos(theta_z), -np.sin(theta_z),  0], 
            [np.sin(theta_z),  np.cos(theta_z),  0], 
            [0,                              0,  1]
            ])

def exMat(theta_x, theta_y, theta_z, tx, ty, tz):
    R = np.multiply(Rotx(theta_x), np.multiply(Roty(theta_y), Rotz(theta_z)))
    t = np.array([tx, ty, tz]).reshape(3,1)
    v = np.array([0, 0, 0, 1])
    return np.vstack((np.hstack((R,t)), v))
    

