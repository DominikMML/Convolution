# -*- coding: utf-8 -*-
import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt
from skimage.color import rgb2hsv

class Filters(object):
    
    def __init__(self, image):
        hsv_img = rgb2hsv(image)
        self.image = hsv_img[:, :, 2].reshape((hsv_img.shape[0],
                                               hsv_img.shape[1]))

    def Convolve2d(self, kernel):
        self.kernel = kernel 
        kernel = np.flipud(np.fliplr(self.kernel))
        output = np.zeros_like(self.image)
    
        image_padded = np.zeros((self.image.shape[0] + 2, 
                                 self.image.shape[1] + 2))
        image_padded[1:-1, 1:-1] = self.image
    
        for x in range(self.image.shape[1]):
            for y in range(self.image.shape[0]):
                output[y, x]=(kernel * image_padded[y: y+self.filter_size, 
                                                    x: x+self.filter_size]).sum()
        return output
    
    def BoxFilter(self,filter_array, filter_size,overlap=0.0):
        self.filter_size = filter_size
        self.filter_array = filter_array 

        return self.Convolve2d(filter_array)
    
   
im = imread('/home/dlvm/rollei.jpg', as_gray=False)
im = im / 255

plt.imshow(im)
plt.show()

filter_array = np.array([[-3, -2, 0],
                         [-2, 1, 1], 
                         [0, 2, 3]]).reshape((3,3))


im_filtered = Filters(im).BoxFilter(filter_array,
                                    filter_array.shape[0],
                                    0.0)

plt.imshow(im_filtered)
plt.show()


