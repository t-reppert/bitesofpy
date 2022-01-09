from typing import Optional
from pprint import pprint
import numpy as np
np.set_printoptions(suppress=True, precision=2)

def convolution2D(
    image: np.array, 
    kernel: np.array, 
    padding: Optional[int] = None, 
    stride: int = 1
) -> np.array:
    """Calculate the convolution between the input image and a filter, returning the feature map.

    Args:
        image (np.array): Input image as 2d array with height x width. Supposed to have equal dimensions.
        kernel (np.array): Filter or kernel as 2d array with height x width. Supposed to have equal and odd dimensions.
        padding (Optional[int]): Border around the image with pixels of value 0. If None, defaults to p = (f - 1) / 2.
        stride (int): Step length to move the filter over the image. Defaults to 1.

    Returns:
        np.array: the feature map constructed from the image and the kernel.
    """
    # Validation
    if not (isinstance(stride, int)):
        raise TypeError("stride must be a integer!")
    if stride < 1:
        raise ValueError("stride must be greater than or equal to 1")
    if not (isinstance(image, np.ndarray) and isinstance(kernel, np.ndarray)):
        raise TypeError("image and kernel need to be numpy arrays")
    if not (image.dtype.kind in 'cfiu' and kernel.dtype.kind in 'cfiu'):
        raise TypeError("image and kernel must both contain only numeric values")
    if not (len(kernel.shape) == 2 and len(image.shape) == 2):
        raise ValueError("image and kernel need to be 2D arrays")
    if not (kernel.shape[0] == kernel.shape[1] and image.shape[0] == image.shape[1]):
        raise ValueError("image and kernel need to be quadratic")
    if kernel.shape[0] > image.shape[0]:
        raise ValueError("kernel cannot be larger than image")
    if kernel.shape[0] % 2 == 0:
        raise ValueError("kernel needs to be odd in size")
    if padding or padding == 0:
        if not (isinstance(padding, int)):
            raise TypeError("padding must be an integer")
        if padding < 0:
            raise ValueError("padding must be greater than or equal to 0")
    else:
        padding = (kernel.shape[0]-1) // 2

    # Processing
    image_size = image.shape[0]
    kernel_size = kernel.shape[0]
    feature_size = int(np.floor((image_size - kernel_size + 2 * padding) / stride) + 1)
    feature_map = np.zeros((feature_size, feature_size))
    temp_size = image_size + 2 * padding
    if padding > 0:
        temp_image = np.zeros((temp_size, temp_size))
        temp_image[padding:-padding, padding:-padding] = image
    else:
        temp_image = image.copy()
    for row in range(feature_size):
        row_start = row * stride
        for column in range(feature_size):
            col_start = column * stride
            sub_image = temp_image[row_start:row_start+kernel_size, col_start:col_start+kernel_size]
            feature_map[row, column] = np.sum(kernel * sub_image)
    return feature_map
