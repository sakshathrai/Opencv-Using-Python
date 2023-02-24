import cv2
from PIL import Image

# Read an image
img = cv2.imread('image.jpg')

# Convert BGR to RGB using OpenCV
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert BGR to RGB using Pillow
img_pil = Image.open('image.jpg').convert('RGB')

# Display the original image and converted images side by side
cv2.imshow('BGR', img)
cv2.imshow('RGB (OpenCV)', img_rgb)
img_pil.show()

# Write the converted images to files
cv2.imwrite('output_opencv.jpg', img_rgb)
img_pil.save('output_pillow.jpg')
