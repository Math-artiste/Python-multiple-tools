import pywhatkit as kit 
import cv2
Handwritten = input("Enter the text to convert in handwritting : ")
kit.text_to_handwriting(Handwritten, save_to = "signature.png")
img = cv2.imread("signature.png")
cv2.imshow("Signature", img)
cv2.waitKey(0)
cv2.destroyAllWindows
