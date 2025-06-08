import cv2
import os
import numpy as np

def train_classifier(data_dir):
    faces = []
    ids = []

    for root, dirs, files in os.walk(data_dir):
        for file in files:
            if file.endswith("jpg") or file.endswith("png"):
                path = os.path.join(root, file)
                img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
                id = int(os.path.basename(root))  # Folder name as ID
                faces.append(np.array(img, 'uint8'))
                ids.append(id)

    ids = np.array(ids)
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.train(faces, ids)
    clf.save("classifier.xml")
    print("Training complete and classifier.xml saved.")

if __name__ == "__main__":
    train_classifier("data")