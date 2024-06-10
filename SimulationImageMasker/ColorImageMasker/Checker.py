from matplotlib import pyplot as plt
import numpy as np

from SimulationImageMasker.ColorImageMasker.ColorMapGenerator import generate_colormap

if __name__ == '__main__':

    N = 16
    M = 7
    H = np.arange(N * M).reshape([N, M])
    fig = plt.figure(figsize=(10, 10))
    ax = plt.pcolor(H, cmap=generate_colormap(N * M))
    plt.show()
