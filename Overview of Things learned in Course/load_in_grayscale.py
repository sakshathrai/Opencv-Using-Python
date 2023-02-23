import cv2

# Read an image in grayscale
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Display the image
cv2.imshow('image', img)
cv2.waitKey(0)

# Write the image to file
cv2.imwrite('output.jpg', img)
