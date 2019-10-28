import numpy as np


class Normalization:
    def normalize(self, x, mu, std):
        return (x - mu)/std

    def featureNormalize(self,data):
        vfunc = np.vectorize(self.normalize)
        mu = np.mean(data.x, axis=0)
        sigma = np.std(data.x, axis=0)
        x_norm = vfunc(data.x, mu, sigma)

        return[x_norm, mu, sigma]