from facial_emotion_recognition import EmotionRecognition
import cv2
import face_recognition
from tkinter import filedialog
from tkinter import *

er = EmotionRecognition(device='gpu', gpu_id=0)

img = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("All photo files", "*.jpg .jpeg .jpe .bmp .tif, .tiff .png .gif"), ("JPEG files", "*.jpg .jpeg .jpe"), ("PNG files", "*.png"), ("GIF files", "*.gif"), ("TIFF files", "*.tif .tiff"), ("BMP files", "*.bmp")))
img = cv2.imread(img)
#img = cv2.imread("team.jpg")
face_locations = face_recognition.face_locations(img)
#putText settings
font = cv2.FONT_HERSHEY_SIMPLEX
a=20
b=25
org = (a, b)
fontScale = 1
color = (0, 0, 255)
thickness = 1
if (len(face_locations) == 0):
    print('The dictionary is empty.')
    img = cv2.putText(img, "No emotion detected", (a, b), font,
                      1, (0, 0, 0), 6, cv2.LINE_AA)
    img = cv2.putText(img, "No emotion detected", (a, b), font,
                      1, color, 2, cv2.LINE_AA)
    b = b + 25
    cv2.imshow('emotion', img)

img = er.recognise_emotion(img, face_locations, return_type='BGR')

cv2.imshow('emotion', img)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()