# в папку samples кидаешь фотки jpg , прога сравнивает их с той что лежит там же где файл


import dlib
from skimage import io
from scipy.spatial import distance
import time
import os, sys
import win_unicode_console

folder = []
for i in os.walk('samples'):
    folder.append(i)

sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
detector = dlib.get_frontal_face_detector()

img = io.imread('1.jpg')


dets = detector(img, 1)



for k, d in enumerate(dets):
    shape = sp(img, d)
    face_descriptor1 = facerec.compute_face_descriptor(img, shape)


for f in folder[0][2]:
    if (f.endswith(".jpg")):
        img = io.imread("samples/" + f)
        dets_webcam = detector(img, 1)
        for k, d in enumerate(dets_webcam):
            shape = sp(img, d)
            face_descriptor2 = facerec.compute_face_descriptor(img, shape)
            a = distance.euclidean(face_descriptor1, face_descriptor2)
            if a < 0.6:
                print('совпало с изображением ' + f)
