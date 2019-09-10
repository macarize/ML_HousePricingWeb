import numpy as np

class AddBias:
    def addB(self, data):
        ones = np.ones((data.m, 1), dtype=int)
        data.x = np.concatenate((ones, data.x), axis=1)
        return data