import cv2

xmlpath = "Z:\\Haar Cascade\\face.xml"

faceCascade = cv2.CascadeClassifier(xmlpath)

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        image = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("video", frame)
    if cv2.waitKey(1) == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
