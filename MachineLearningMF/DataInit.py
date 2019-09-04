import Loadcvs
import numpy as np

class DataInit:
    x = []
    y = []
    m = 0
    theta = 0
    def loader(self, path):
        Loader = Loadcvs.Loadcvs()
        data = Loader.Loadcvs(path)
        colLen = len(data[0])-1

        self.x = np.array(data[:, :colLen])
        self.y = np.array(data[:, colLen])
        self.m = np.size(self.y)

        self.y = self.y.reshape(self.m, 1)








