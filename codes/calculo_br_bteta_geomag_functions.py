import numpy as np

def compB(g10,g11,h11,theta,phi):
    Br = -2*(g10*np.cos(theta) + (g11*np.cos(phi)+h11*np.sin(phi))*np.sin(theta))
    Bt = g10*np.sin(theta) - (g11*np.cos(phi) + h11*np.sin(phi))*np.cos(theta)
    Bp = g11*np.sin(phi) - h11*np.cos(phi)

    return Br, Bt, Bp