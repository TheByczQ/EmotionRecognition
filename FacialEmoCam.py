from facial_emotion_recognition import EmotionRecognition
import face_recognition
import cv2

er = EmotionRecognition(device='gpu', gpu_id=0)
cam = cv2.VideoCapture(0)

#putText settings
font = cv2.FONT_HERSHEY_SIMPLEX
a=20
b=25
org = (a, b)
fontScale = 0.7
color = (0, 0, 255)
thickness = 1

while True:
    _, img = cam.read()
    face_locations = face_recognition.face_locations(img)
    img = er.recognise_emotion(img, face_locations, return_type='BGR')
    if (len(face_locations) == 0):
        img = cv2.putText(img, "No emotion detected", (a, b), font,
                          1, (0, 0, 0), 6, cv2.LINE_AA)
        img = cv2.putText(img, "No emotion detected", (a, b), font,
                          1, color, 2, cv2.LINE_AA)
        cv2.imshow("window", img)
        if cv2.waitKey(1) == 27:
            #break  # esc to quit
            cv2.destroyAllWindows();

    cv2.imshow("window", img)
    if cv2.waitKey(1) == 27:
        break  # esc to quit
cv2.destroyAllWindows();