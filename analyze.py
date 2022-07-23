import cv2
import numpy as np

def analyze(filepath: str):
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('resources/haarcascade_frontalface_default.xml')
    
    # Read the input image
    img = cv2.imread(filepath)
    
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.2, 4)
    
    # # Draw rectangle around the faces
    # faces_map = []
    # for (x, y, w, h) in faces:
    #     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    #     faces_map.append((x, y, x+w, y+h))
    # Display the output
    return {"face_count": len(faces)}

# Testing analyze
path = "resources/family.png"
result = analyze(path)
print(result)