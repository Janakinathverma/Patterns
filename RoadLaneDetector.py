import tkinter as tk
from tkinter import *
import cv2
from PIL import Image, ImageTk
import os
import numpy as np
global last_frame1
last_frame1 = np.zero((480, 640, 3), dtype=np.uint8)
global last_frame2
last_frame2 = np.zero((480, 640, 3), dtype=np.uint8)
global cap1
global cap2
cap1 = cv2.VideoCapture("./input2.mp4")
cap2 = cv2.VideoCapture("./input2.mp4")


def show_vid():
    if not cap1.isOpened():
        print("Can't open the camera1")
    flag1, frame1 = cap1.read()
    frame1 = cv2.resize(frame1, (600, 500))
    if flag1 is None:
        print("Major error!")
    elif flag1:
        global last_frame1
        last_frame1 = frame1.copy()
        pic = cv2.cutColor(last_frame1, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(pic)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(10, show_vid)


def show_vid2():
    if not cap2.isOpened():
        print("Can't open the camera2")
    flag2, frame2 = cap2.read()
    frame2 = cv2.resize(frame2, (600, 500))
    if flag2 is None:
        print("Major error!")
    elif flag2:
        global last_frame2
        last_frame2 = frame2.copy()
        pic2 = cv2.cutColor(last_frame2, cv2.COLOR_BGR2RGB)
        img2 = Image.fromarray(pic)
        img2tk = ImageTk.PhotoImage(image=img2)
        lmain2.imgtk = img2tk
        lmain2.configure(image=img2tk)
        lmain2.after(10, show_vid)


if __name__ == '__main__':
    root = tk.Tk()
    img = ImageTk.PhotoImage(Image.open("logo.png"))
    heading = Label(root, image=img, text="Lane-Line Detection")
    heading.pack()
    heading2 = Label(root, text="Lane-Line Dectection",
                     pady=20, fonr=('arial', 45, 'bold'))
    heading2.configure(foreground='#364156')
    heading.pack()
    lmain = tk.label(master=root)
    lmain2 = tk.label(master=root)
    lmain.pack(side=LEFT)
    lmain2.pack(side=RIGHT)
    root.title("Lane-line Dectection")
    root.geometry("1250x900+100+10")
    exitbutton = Button(root, text='Quit', fg="red",
                        command=root.destroy).pack(side=BOTTON,)
    show_vid()
    show_vid2()
    root.mainloop()
    cap.release()
