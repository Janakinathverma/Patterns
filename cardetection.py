import time
import cv2
# add any video link containing the input
cap = cv2.videocapture('traffic.mp4')
car_cascade = cv2.CascadeClassifier('cars.xml')
coord = [[6367, 352], [904, 352], [631, 512], [952, 512]]
dist = 3
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BAYER_BGR2BGR)
    cars = car_cascasde.detectMultiScale(gray, 1.8, 2)
    for(x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x+w, y+h), (225, 0, 0), 2)
    cv2.line(img, (coord[0][0], coord[1]01], coord[1][1], 0, 0, 255), 2)
    cv2.line(img, (coord[0][0], coord[2][1], coord[1][1], 0, 0, 255), 2)
    cv2.line(img, (coord[2][0], coord[3][1], coord[1][1], 0, 0, 255), 2)
    cv2.line(img, (coord[1][0], coord[3][1], coord[1][1], 0, 0, 255), 2)
