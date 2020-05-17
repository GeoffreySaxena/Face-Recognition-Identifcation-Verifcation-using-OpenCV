import cv2
import sqlite3
import os
import dlib
import numpy as np

xmlpath = "Z:\\Haar Cascade\\face.xml"

faceCascade = cv2.CascadeClassifier(xmlpath)
eyeCascade = cv2.CascadeClassifier(xmlpath1)
smileCascade = cv2.CascadeClassifier(xmlpath2)

video_capture = cv2.VideoCapture(1, cv2.CAP_DSHOW)


def InsertOrUpdate(Identity, Name):
    conn = sqlite3.connect("FaceDB.db")
    cmd = " SELECT * FROM Details WHERE ID=" + str(Identity)
    cursor = conn.execute(cmd)
    record_exists = 0
    for row in cursor:
        record_exists = 1
    if record_exists == 1:
        cmd = "UPDATE Details SET Name=" + str(Name) + "WHERE ID =" + str(Identity)
    else:
        cmd = "INSERT INTO Details(ID, Name) VALUES (" + str(Identity) + " , " + str(Name) + " ) "
    conn.execute(cmd)
    conn.commit()
    conn.close()


identity = input("Enter your Identification Number:")
name = input("Enter your Name:")
InsertOrUpdate(identity, name)

sampleNumber = 0

while True:
    ret, frame = video_capture.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.4, minNeighbors=6, minSize=(30, 30),
                                         flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        sampleNumber = sampleNumber + 1
        path = "Z:\\PyCharm\\Face_Recognition_using_haar\\dataSet\\User"
        cv2.imwrite(path + str(identity) + "." + str(sampleNumber) + ".jpg", gray[y:y + h, x:x + w])
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.waitKey(100)
    cv2.imshow("Face", frame)
    cv2.waitKey(1)
    if sampleNumber >= 50:
        break

video_capture.release()
cv2.destroyAllWindows()
