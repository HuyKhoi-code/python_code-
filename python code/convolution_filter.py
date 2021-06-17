import numpy as np

def Convo (img, kernel):
    img_height = img.shape[0]
    img_weight = img.shape[1]
    kernel_height = kernel.shape[0]
    kernel_weight = kernel.shape[1]
    h = (kernel_height - 1) // 2
    w = (kernel_weight - 1) // 2
    out = np.zeros((img_height - h, img_weight - w))
    for i in range (h, img_height - h):
        for j in range (w, img_weight - w):
            sum = 0
            for u in range (-h, h + 1):
                for v in range (-w, w + 1):
                    H = kernel[i , j]
                    F = img[i+u, j+v] 
                    sum += H*F
            out[i, j]=sum
    return out

img = np.array([[1, 0, 0, 1, 0],
                [0, 1, 1, 0, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 0, 1, 1],
                [0, 1, 1, 0, 1]
                ])

kernel = np.array([[1, 0, 0],
                   [0, 1, 1],
                   [1, 0, 1]])

Convo(img, kernel)
