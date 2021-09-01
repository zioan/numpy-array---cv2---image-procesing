import numpy
import cv2

#Slice
image = cv2.imread("smallgray.png", 0)
  # [[187 158 104 121 143] 
  # [198 125 255 255 147] 
  # [209 134 255  97 182]]

print(image[0:2])
  # [[187 158 104 121 143] 
  # [198 125 255 255 147]

print(image[0:2, 2:4])
  # [[104 121] 
  # [255 255]]

print(image.shape)
  #(3, 5)


# Iterating
for i in image:
  print(i)
  # [187 158 104 121 143] 
  # [198 125 255 255 147] 
  # [209 134 255  97 182]

for i in image.flat:
  print(i)
  # 187
  # 158
  # 104
  # 121
  # 143
  # 198
  # 125
  # 255
  # 255
  # 147
  # 209
  # 134
  # 255
  # 97
  # 182

# Stacking and Splitting

  #STACKING
  #horizontal stack (of 2 or more arrays)
ims = numpy.hstack((image, image))
print(ims)
  # [[187 158 104 121 143 187 158 104 121 143]
  # [198 125 255 255 147 198 125 255 255 147]
  # [209 134 255  97 182 209 134 255  97 182]]


  #vertical stack (of 2 or more arrays)
imsv = numpy.vstack((image, image))
print(imsv)
  # [[187 158 104 121 143]
  # [198 125 255 255 147]
  # [209 134 255  97 182]
  # [187 158 104 121 143]
  # [198 125 255 255 147]
  # [209 134 255  97 182]]


  #SPLITTING
lst = numpy.hsplit(image, 5)
print(lst)
# [array([[187],
#       [198],
#       [209]], dtype=uint8), array([[158],
#       [125],
#       [134]], dtype=uint8), array([[104],
#       [255],
#       [255]], dtype=uint8), array([[121],
#       [255],
#       [ 97]], dtype=uint8), array([[143],
#       [147],
#       [182]], dtype=uint8)]