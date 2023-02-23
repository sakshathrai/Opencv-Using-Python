import cv2

# Read an image
img = cv2.imread('image.jpg')

# Display the image
cv2.imshow('image', img)
cv2.waitKey(0)

# Write the image to file
cv2.imwrite('output.jpg', img)
