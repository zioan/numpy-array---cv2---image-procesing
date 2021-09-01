import cv2

# read image in greyscale
image = cv2.imread("smallgray.png", 0)

# read image in BGR
# image = cv2.imread("smallgray.png", 1)

print(image)
  # 3 dimension array
  # [[187 158 104 121 143] 
  # [198 125 255 255 147] 
  # [209 134 255  97 182]]

# Create an image from an numpy array
img2 = cv2.imwrite("newsmallgrey.png", image)
print(img2)
  # True (that means the image was created)