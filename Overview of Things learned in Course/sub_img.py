import cv2
import numpy as np

# Read two images
img1 = cv2.imread('image1.jpg')
img2 = cv2.imread('image2.jpg')

# Resize the images to same dimensions
img1 = cv2.resize(img1, (640, 480))
img2 = cv2.resize(img2, (640, 480))

# Subtract the images
subtracted_img = cv2.subtract(img1, img2)

# Display the original images and the combined image side by side
cv2.imshow('subtracted_img')
