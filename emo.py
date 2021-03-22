from fer import FER
import cv2
import sys
import numpy as np
import operator
import face_recognition
from tkinter import filedialog
from tkinter import *

img = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("All photo files", "*.jpg .jpeg .jpe .bmp .tif, .tiff .png .gif"), ("JPEG files", "*.jpg .jpeg .jpe"), ("PNG files", "*.png"), ("GIF files", "*.gif"), ("TIFF files", "*.tif .tiff"), ("BMP files", "*.bmp")))
img = cv2.imread(img)
#img = cv2.imread("wow.jpg")
face_locations = face_recognition.face_locations(img)
face_locations = [list(x) for x in face_locations]
for face in face_locations:
    w = face[2] - face[0]
    h = face[1] - face[3]
    face[1] = face[0]
    face[0] = face[3]
    face[2] = w
    face[3] = h
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print('Faces found: ', len(face_locations))
for i in range(len(face_locations)):
    img = cv2.rectangle(img, (face_locations[i][0], face_locations[i][1]), (face_locations[i][0]+face_locations[i][2], face_locations[i][1]+face_locations[i][3]), (255, 0, 255), 2)
    #numeracja twarzy
    # n += 1
    # img = cv2.putText(img, 'face'+str(n), (face_locations[i][0]-10, face_locations[i][1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
print(face_locations)
detector = FER(mtcnn=True)
emotion = detector.detect_emotions(img, face_locations)
#print(emotion)

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
    if cv2.waitKey(0) == 27:
        cv2.destroyAllWindows()

if (len(face_locations) >= 2):
    index = 0
    dict = emotion[index]
    emoList = dict["emotions"]
    for faces in range(len(emotion)):
        emoList = emotion[index]["emotions"]
        emoList = {k: v for k, v in sorted(emoList.items(), key=operator.itemgetter(1), reverse=True)}
        #dokładniejszy wynik
        for emo, value in emoList.items():
            print(str(emo) + ": " + str(value))
            value_rounded = round(value * 100, 1)
            value_rounded = int(value_rounded)
            emo_print = "face " + str(index + 1) + ": " + str(emo) + ": " + str(value_rounded) + "%"
        #     img = cv2.putText(img, emo_print, (a, b), font,
        #                       fontScale, color, thickness, cv2.LINE_AA)
        #     b = b + 25
        # print(emo_print)
        index += 1
        for keys in emoList.keys():
            emo_print = keys
            img = cv2.putText(img, emo_print, (face_locations[faces][0] + 5, face_locations[faces][1] - 10), font,
                              fontScale, (0, 0, 0), 6, cv2.LINE_AA)
            img = cv2.putText(img, emo_print, (face_locations[faces][0]+5, face_locations[faces][1]-10), font,
                              fontScale, color, 2, cv2.LINE_AA)
            break
    cv2.imshow('emotion', img)
    if cv2.waitKey(0) == 27:
        cv2.destroyAllWindows()

elif(len(face_locations) == 1):
    index = 0
    dict = emotion[index]
    emoList = dict["emotions"]
    emoList = {k: v for k, v in sorted(emoList.items(), key=operator.itemgetter(1), reverse=True)}
    for emo, value in emoList.items():
        #print(str(emo) + ": " + str(value))
        value_rounded = round(value*100, 1)
        value_rounded = int(value_rounded)
        emo_print = str(emo) + ": " + str(value_rounded) + "%"
        img = cv2.putText(img, emo_print, (a, b), font,
                          0.7, (0, 0, 0), 2, cv2.LINE_AA)
        img = cv2.putText(img, emo_print, (a, b), font,
                          0.7, color, 1, cv2.LINE_AA)
        b = b + 25
    cv2.imshow('emotion', img)
    if cv2.waitKey(0) == 27:
        cv2.destroyAllWindows()
