import numpy as np


def convolution(image, kernel):

    image_h = image.shape[0]
    image_w = image.shape[1]

    kernel_h = kernel.shape[0]
    kernel_w = kernel.shape[1]

    con_image = np.zeros((image_h + kernel_h//2*2, image_w + kernel_w//2*2))
    con_image[kernel_h//2:kernel_h//2+image_h, kernel_w//2:kernel_w//2+image_w] = image

    result = np.zeros(image.shape)

    for i in range(image_h):
        for j in range(image_w):
            result[i][j] = np.sum(con_image[i:i+kernel_h, j:j + kernel_w] * kernel)

    return result



def main():

    test_image = np.random.randint(0,100,[10,10])
    test_kernel = np.random.randint(0,2, [3,3])
    result = convolution(test_image, test_kernel)


    print(result)

    print(np.sum(np.stack([result, result], 2), 2))




import sys

if __name__ == "__main__":
    #main()
    import numpy as np

    array = np.array([1,2,3])

    print(tuple(array))
    print(len())
    print(type(tuple(array)))