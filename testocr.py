from PIL import Image
import pytesseract
import cv2
import os

for i in range(0, 3):
	image = cv2.imread("button"+str(i+1)+"img.png")
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	filename = "greybutton"+str(i+1)+".png"
	cv2.imwrite(filename, cv2.bitwise_not(gray))
	text = pytesseract.image_to_string(Image.open(filename),
		config='digits -psm 7')
	print(text)