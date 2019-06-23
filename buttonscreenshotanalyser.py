from PIL import Image
import pytesseract
import cv2
import os
def imagereader(name, invert=True, blur=False):
	image = cv2.imread(name)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	filename = "grey"+name
	if invert:
		gray = cv2.bitwise_not(gray)
	if blur:
		gray = cv2.GaussianBlur(gray, (0,0), 4)
		gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
		gray = cv2.GaussianBlur(gray, (0,0), 4)
		gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
		gray = cv2.GaussianBlur(gray, (0,0), 4)
		gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
		gray = cv2.GaussianBlur(gray, (0,0), 4)
		gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
		gray = cv2.GaussianBlur(gray, (0,0), 4)
		gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
		gray = cv2.GaussianBlur(gray, (0,0), 4)
		gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	cv2.imwrite(filename, gray)
	text = pytesseract.image_to_string(Image.open(filename), config='--psm 6')
	return text


buttonimgs = [Image.open("button1img.png"),
				Image.open("button2img.png"),
				Image.open("button3img.png"),
				Image.open("button4img.png"),
				Image.open("button5img.png")]


buttonvalues = []
for i in range(0,len(buttonimgs)):
	# TODO not very rigourous
	avcolor=buttonimgs[i].resize((1,1)).getcolors()[0][1]
	if avcolor[0]>178 and avcolor[0]<182 and avcolor[1]>172 and avcolor[1]<176 and avcolor[2]<166 and avcolor[2]>162:
		buttonvalues.append("b")
	else:
		text=imagereader("button"+str(i+1)+"img.png")
		buttonvalues.append(text)

moves = int(imagereader("movesimg.png"))
goal = int(imagereader("goalimg.png")[5:])
start = (imagereader("startimg.png", invert=False, blur=True)).lower()
print(start)
s = ""
for i in range(0,len(start)):
	if start[i]=="s":
		s += "5"
	elif start[i]=="o":
		s += "0"
	elif start[i]=="g" or start[i]=="j":
		s += "9"
	elif start[i]=="i" or start[i]=="|" or start[i]=="/":
		s += "1"
	else:
		s += start[i]
data = {
	"start": int(s),
	"moves": moves,
	"goal": goal,
	"buttons": buttonvalues,
	"buttonfuncs": None
}