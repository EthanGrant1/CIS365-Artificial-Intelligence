import numpy as np
import cv2
import matplotlib.pyplot as plt

def get_image(path,size):
    originalImage = cv2.imread(path)
    resizedImage = cv2.resize(originalImage, size)
    grayImage = cv2.cvtColor(resizedImage, cv2.COLOR_BGR2GRAY)
    return np.array(grayImage)

find_penny = get_image('penny_all_alone.jpg',(900,500))
plt.imshow(find_penny, cmap='gray', vmin=0, vmax=255)
plt.show()

template = get_image('penny.png',(100,100))
plt.imshow(template, cmap='gray', vmin=0, vmax=255)
plt.show()

steps_h = find_penny.shape[0] - template.shape[0]
steps_v = find_penny.shape[1] - template.shape[1]

array = np.zeros((steps_h,steps_v))
for i in range(0,steps_h):
    for j in range(0,steps_v):
        array[i,j] = np.linalg.norm(find_penny[i:i+template.shape[0],j:j+template.shape[1]]- template)

plt.hist(array.flatten(), density=False, bins=100)
plt.show()

m_val = min(array.flatten())
n_max = max(array.flatten())-min(array.flatten())

test = np.zeros((steps_h,steps_v))
for i in range(0,array.shape[0]):
    for j in range(0,array.shape[1]):
        test[i,j] = (array[i][j] - m_val)/n_max

plt.imshow(test*255, cmap='gray', vmin=0, vmax=255)
plt.show()