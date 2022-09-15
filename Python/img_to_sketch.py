# convert imge to pencil sketch

import cv2

#specify the patch to image (loading image image)
image1 = cv2.imread("img_arbre.png")
window_name = "original image"

#displaying the original image
cv2.imshow(window_name,image1)

#convert the image from one color space to another
grey_img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img)

#image smoothing
blur = cv2.GaussianBlur(invert, (21, 21), 0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img, invertedblur, scale=256.0)

#save the converted image to specified patch
cv2.imwrite("sketch.png", sketch)

image = cv2.imread("sketch.png")

#window name in which image is displayed
window_name = "Sketch image"

#displaying the sketch image
cv2.imshow(window_name, image)
#waits for users to press any key
#(this is necessary to avoid python kernel from crashing)
cv2.waitKey(0)

#close
cv2.destroyAllWindows()