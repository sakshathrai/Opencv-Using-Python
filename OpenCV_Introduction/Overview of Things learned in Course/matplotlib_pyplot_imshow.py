import cv2 as c
from matplotlib import pyplot as plt
img_cat=c.imread('cats.jpg')
#in default i.e bgr
plt.imshow(img_cat)
#convert bgr to rgb
plt.imshow(c.cvtColor(img_cat,c.COLOR_BGR2RGB))
