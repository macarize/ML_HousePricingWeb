import numpy as np



class Loadcvs:
    def Loadcvs(self, path):
        matrix = np.loadtxt(path, delimiter=",", dtype=np.float32)
        return matrix
