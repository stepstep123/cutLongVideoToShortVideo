#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2/12/20 9:30 AM
# @Author  : Jianghua Yu
# @File    : main.py
# @Software: PyCharm


import cv2

if __name__ == '__main__':
    #　the root of input
    vidPath = '/home/paul/Videos/PingAn/RePSSComptition/cutLongVideoToShortVideo/longVideo/myself.mp4'
    # the root of out put
    shotsPath = '/home/paul/Videos/PingAn/RePSSComptition/cutLongVideoToShortVideo/shortVideo/%d.avi' # output path (must be avi, otherwise choose other codecs)
    # the range of cutted video
    segRange = [(0,40),(50,100),(200,400)] # a list of starting/ending frame indices pairs
    # read video
    cap = cv2.VideoCapture(vidPath) # read video
    # get frame rate f
    fps = int(cap.get(cv2.CAP_PROP_FPS)) #get frame rate f
    # print(fps)
    #get widt and hight(width, hight)
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print(size)
    # wirte in XVID codecs
    fourcc = int(cv2.VideoWriter_fourcc('X','V','I','D')) # XVID codecs

    for idx,(begFidx,endFidx) in enumerate(segRange):
        writer = cv2.VideoWriter(shotsPath%idx,fourcc,fps,size)
        cap.set(cv2.CAP_PROP_POS_FRAMES,begFidx)
        ret = True # has frame returned
        while(cap.isOpened() and ret and writer.isOpened()):
            ret, frame = cap.read()
            frame_number = cap.get(cv2.CAP_PROP_POS_FRAMES) - 1
            if frame_number < endFidx:
                writer.write(frame)
            else:
                break
        writer.release()