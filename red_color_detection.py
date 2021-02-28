import cv2  
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('T2.bmp')

grid_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

grid_HSV = cv2.cvtColor(grid_RGB, cv2.COLOR_RGB2HSV)

lower = np.array([0,150,50])
upper = np.array([10,255,255])

mask = cv2.inRange(grid_HSV, lower, upper)

res = cv2.bitwise_and(grid_RGB,grid_RGB, mask=mask)

plt.figure(figsize=(20,8))
plt.imshow(res)


cv2.imshow("T2",img)
cv2.imshow("Mask",mask)

cv2.waitKey(0)
cv2.destroyAllWindows()