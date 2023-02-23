import cv2

# Read an image in BGR
img = cv2.imread('image.jpg')

# Convert BGR to HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Display the original image and the converted image side by side
cv2.imshow('BGR', img)
cv2.imshow('HSV', img_hsv)

# Write the converted image to file
cv2.imwrite('output_hsv.jpg', img_hsv)
