import math
import time
from ctypes import cast, POINTER

import cv2
import numpy as np
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

import hand_tracking as ht


def volume_control():
    cam_w, cam_h = 640, 480

    cap = cv2.VideoCapture(0)
    cap.set(3, cam_w)
    cap.set(4, cam_h)
    p_time = 0

    detector = ht.HandDetector(min_detection_confidence=0.7)

    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume_range = volume.GetVolumeRange()
    min_vol = volume_range[0]
    max_vol = volume_range[1]
    vol = 0
    volBar = 400
    volPer = 0
    while True:
        success, img = cap.read()
        img = detector.find_hands(img, True)
        hand_positions = detector.find_position(img)
        if len(hand_positions) != 0:

            x1, y1 = hand_positions[4][1], hand_positions[4][2]
            x2, y2 = hand_positions[8][1], hand_positions[8][2]
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

            cv2.circle(img, (x1, y1), 5, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 5, (0, 0, 255), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
            cv2.circle(img, (cx, cy), 10, (0, 0, 255), cv2.FILLED)

            length = math.hypot(x2 - x1, y2 - y1)

            vol = np.interp(length, [0, 200], [min_vol, max_vol])
            volBar = np.interp(vol, [-65.25, 0], [400, 150])
            volPer = np.interp(vol, [-65.25, 0], [0, 100])
            volume.SetMasterVolumeLevel(vol, None)

            if length < 50:
                cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

        cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
        cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
        cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,
                    1, (255, 0, 0), 3)

        c_time = time.time()
        fps = 1 / (c_time - p_time)
        p_time = c_time
        cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX,
                    1, (255, 0, 0), 3)

        cv2.imshow("Img", img)
        cv2.waitKey(1)
