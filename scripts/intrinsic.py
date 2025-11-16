# strore the intrinsic parameters of the camera 
# the function returns intrinsic parameters in other files

import numpy as np

f = 0
m_x = 0
m_y = 0
p_x = 0
p_y = 0

def inMat():
    return np.array([
      [m_x*f,   0,      p_x],
      [0,       m_y*f,  p_y],
      [0,       0,      1]  
    ])