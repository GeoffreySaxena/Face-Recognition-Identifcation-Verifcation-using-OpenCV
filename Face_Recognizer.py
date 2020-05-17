import cv2
import sqlite3

xmlpath = "Z:\\Haar Cascade\\face.xml"

faceCascade = cv2.CascadeClassifier(xmlpath)

video_capture = cv2.VideoCapture(1)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("Z:\\PyCharm\\Face_Recognition_using_haar\\TrainingData.yml")


def getProfile(identity):
    conn = sqlite3.connect("FaceDB.db")
    cmd = " SELECT * FROM Details WHERE ID=" + str(identity)
    cursor = conn.execute(cmd)
    profile = None
    for row in cursor:
        profile = row
    conn.close()
    return profile


while True:
    ret, frame = video_capture.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        image = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        identity, conf = recognizer.predict(gray[y:y+h, x:x+w])
        profile = getProfile(identity)
        if profile is not None:
            cv2.putText(frame, str(profile[0]), (x, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
            cv2.putText(frame, str(profile[1]), (x, y + h + 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)

    cv2.imshow("video", frame)

    if cv2.waitKey(1) == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
