from transform import four_point_transform
import numpy as numpy
import argparse
import cv2
import imutils

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to the image to be scanned")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
ratio=image.shape[0]/500.0
orig=image.copy()
image=imutils.resize(image,height=500)

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray=cv2.GaussianBlur(gray,(5,5),0)
edged=cv2.Canny(gray,75,200)

print("STEP1:Edge Detection")
cv2.imshow("Image",image)
cv2.imshow("Edged",edged)
cv2.waitKey(0)
cv2.destroyAllWindows()

cnts=cv2.findContours(edged.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(cnts)
cnts=sorted(cnts,key=cv2.contourArea,reverse=True)[:5]

for c in cnts:
	perl=cv2.arcLength(c,True)
	approx=cv2.approxPolyDP(c,0.02*perl,True)

	if len(approx)==4:
		screenCnt=approx
		break
print("STEP2:FIND CONTOURS OF PAPER")
cv2.drawContours(image,[screenCnt],-1,(0,255,0),2)
cv2.imshow("Outline",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

warped=four_point_transform(orig,screenCnt.reshape(4,2)*ratio)

warped=cv2.cvtColor(warped,cv2.COLOR_BGR2GRAY)
warped=cv2.adaptiveThreshold(warped,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,251,11)


print("STEP3:APPLY PERSPECTIVE TRANSFORM")
cv2.imshow("Original",imutils.resize(orig,height=650))
cv2.imshow("scanned",imutils.resize(warped,height=650))
cv2.waitKey(0)