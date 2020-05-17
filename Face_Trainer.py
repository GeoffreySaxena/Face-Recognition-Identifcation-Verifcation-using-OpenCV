import cv2
import os
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
dataSetpath = "Z:\\PyCharm\\Face_Recognition_using_haar\\dataSet"


def getImagesWithID(dataSetpath):
    image_paths = [os.path.join(dataSetpath, f) for f in os.listdir(dataSetpath)]
    print(image_paths)
    faces = []
    ids = []
    for image_paths in image_paths:
        face_img = Image.open(image_paths).convert('L')

        face_np = np.array(face_img, np.uint8)
        identity = int(os.path.split(image_paths)[-1].split('.')[0].replace("User", ""))
        faces.append(face_np)
        print(identity)
        ids.append(identity)
        cv2.imshow("Images being Trained are", face_np)
        cv2.waitKey(10)

    return ids, faces


ids, faces = getImagesWithID(dataSetpath)
recognizer.train(faces, np.array(ids))
recognizer.save("TrainingData.yml")
cv2.destroyAllWindows()
