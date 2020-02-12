#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2/12/20 4:01 PM
# @Author  : Jianghua Yu
# @File    : cut_video2.py
# @Software: PyCharm

import cv2
import os

# 将视频截取为指定长度大小，本次实验为0.5s

if __name__ == "__main__":
    # 1.读取视频

    # the path of input video
    vidPath = '/home/paul/Videos/PingAn/RePSSComptition/cutLongVideoToShortVideo/longVideo/myself.mp4'
    # the path of output video
    shortPath = '/home/paul/Videos/PingAn/RePSSComptition/cutLongVideoToShortVideo/shortVideo/'
    # read video
    cap = cv2.VideoCapture(vidPath)

    # 2.获取帧率

    # get fps
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    # sum fps
    count = cap.get(7)
    # print("COUNT", video_capture.get(6))
    print("fps:", fps)
    # get size (width, hight)
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print("size：",size)

    #define condition
    # per 0.5s to save a video
    # 当前帧
    num = 0
    # 当前截取的第几段
    flag = 0
    # 每隔0.5s截取一段
    time = 0.5
    # timeSpace = fps*0.5
    # needTime = fps*14
    # 3.videoWriter保存视频

    #　write in XVID codecs
    fourcc = cv2.VideoWriter_fourcc("X", "V", "I", "D")
    # videoWriter = cv2.VideoWriter(shortPath+str(num)+".avi", fourcc, fps, frameSize=size)
    # success, frame = cap.read()
    while(num <= count):
        # read per frame
        success, frame = cap.read()
        # frame_index // (fps * c)

        if (num == int((fps * time) * flag)):
            flag += 1
            videoWriter = cv2.VideoWriter(shortPath + str(flag) + ".avi", fourcc, fps, frameSize=size)
            videoWriter.write(frame)
            # videoWriter = cv2.VideoWriter(shortPath + str(flag) + ".avi", fourcc, fps, frameSize=size)
        num += 1
        if not success:
            print("finished")
            break
    cap.release()
