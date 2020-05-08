# Name: Rohit Singh Adhikari
# Date: 08-May-2020

# import library of Open computer vision
import cv2
# load haarcascade files for front face and eyes.
face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(r'haarcascade_eye.xml')
# Start video device in a system
video = cv2.VideoCapture(0)
# define the variable to count the number of frames
counter = 1
while True:
    counter = counter + 1
    # read the video frames
    check, frame = video.read()
    # convert the frame to gray scale image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # call the face haarcascade
    faces = face_cascade.detectMultiScale(frame, 1.5, 5)
    # detect the face coordinates in the number of incoming frame using loop
    for x, y, w, h in faces:
        # create a rectangle around the face coordinates with color defined in RGB and thickness of box
        img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # launch the open cv window to show the video and mark the face with box
    cv2.imshow("OpenCVWindow", img)
    # wait
    key = cv2.waitKey(1)
    # press q key to quit
    if key == ord('q'):
        break
print("Total number of frames processed :", counter)
# release the video port and destroy all window
# clear all windows
video.release()
cv2.destroyAllWindows()
