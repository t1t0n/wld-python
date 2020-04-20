import numpy as np
from scipy.signal import convolve2d


def weber(grayscale_image):
    grayscale_image = grayscale_image.astype(np.float64)
    grayscale_image[grayscale_image==0] = np.finfo(float).eps
    neighbours_filter = np.array([
        [1,1,1],
        [1,0,1],
        [1,1,1]
    ])
    convolved = convolve2d(grayscale_image,neighbours_filter, mode='same')
    weber_descriptor = convolved-8*grayscale_image
    weber_descriptor = weber_descriptor/grayscale_image
    weber_descriptor = np.arctan(weber_descriptor)
    return weber_descriptor
