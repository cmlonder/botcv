import io
import os
import subprocess
import time

import cv2
import numpy as np
from appium import webdriver


class AndroidDevice:
    desired_caps = None

    def __init__(self, apk_file) -> None:
        self.desired_caps = {
            "platformName": "Android",
            "automationName": "uiautomator2",
            "deviceName=": "Android Emulator",
            "app": os.path.abspath(apk_file),
        }

    def connect(self, url):
        return webdriver.Remote(url, self.desired_caps)

    def get_device_size(self):
        size = None
        start_time = time.time()
        pipe = subprocess.Popen("adb shell wm size", stdout=subprocess.PIPE, shell=True)
        for line in io.TextIOWrapper(pipe.stdout, encoding="utf-8"):
            device_size = line.replace("Physical size: ", "")
            device_size = device_size.strip()
            device_size = device_size.split("x")
            print("Device size:", device_size)
            # for instance: 1080 x 22
            # TODO: axis may depend on how game is played, rotated?
            y_axis = device_size[0]
            x_axis = device_size[1]
            size = (int(device_size[1]), int(device_size[0]))
        return size

    def take_screen_shot(self):
        start_time = time.time()
        pipe = subprocess.Popen(
            "adb exec-out screencap -p",
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            shell=True,
        )
        img_bytes = pipe.stdout.read()
        read_time = time.time()

        img = cv2.imdecode(np.frombuffer(img_bytes, np.uint8), cv2.IMREAD_COLOR)
        end_time = time.time()

        # print('stream size', len(img_bytes))
        # print('read cost', read_time - start_time)
        # print('decode cost', end_time - read_time)
        print("screenshot time", end_time - start_time)

        cv2.imwrite("games/idle_heroes/images/screenshot.png", img)
        return "games/idle_heroes/images/screenshot.png"
