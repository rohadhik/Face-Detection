# Name: Rohit Singh Adhikari
# Date: 08-May-2020

# import open CV
import cv2

'''
This program will help you to detect the human faces on a image
using Haarcascade.
'''

# create a cascade classifier object
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# read the image as a color image
img = cv2.imread(r"test.jpg", 1)
# read the image a gray scale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# search for the co-ordinates of the image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.075, minNeighbors=5)
# draw the face rectangle
for x,y,w,h in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 4)
# show the image
cv2.imshow("OpenCVWindow", img)
# wait for the key press
cv2.waitKey(0)
cv2.destroyAllWindows()