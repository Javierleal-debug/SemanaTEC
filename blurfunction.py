import cv2
import numpy as np


def blur(image):
  image = cv2.imread(image)
  cv2.imshow('image',image)
  blur = cv2.blur(image,(5,5))
  cv2.imshow('blur image',blur)


blur('angles.png')
