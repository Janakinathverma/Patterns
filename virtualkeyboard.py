from charset_normalizer import detect
import cv2
import cvzone
from cvzone.HandTrackingModule import Handdetector
from time import sleep
import numpy as np
from pynput.keyboard import Controller
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.set(3,1280)
cap.set(4,720)
detector=HandDetector(detectionCon=0.8)
cap.set(5,674)