import cv2
import numpy as np

# Read an image in BGR
img = cv2.imread('image.jpg')

# Split the image into its channels
b, g, r = cv2.split(img)

# Create an empty image with same dimensions as the original image
zeros = np.zeros(img.shape[:2], dtype="uint8")

# Merge the channels into a color image
blue = cv2.merge([b, zeros, zeros])
green = cv2.merge([zeros, g, zeros])
red = cv2.merge([zeros, zeros, r])

# Display the original image and the separated channels side by side
cv2.imshow('BGR', img)
cv2.imshow('Blue Channel', blue)
cv2.imshow('Green Channel', green)
cv2.imshow('Red Channel', red)

# Write the separated channels to files
cv2.imwrite('output_blue.jpg', blue)
cv2.imwrite('output_green.jpg', green)
cv2.imwrite('output_red.jpg', red)
