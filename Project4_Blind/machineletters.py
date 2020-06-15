#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 09:07:16 2020

@author: priyamisner
"""


import cv2
import numpy as np
import pytesseract
from PIL import Image


def work(image):
    lastresult = ''
    image = cv2.imread(image)

    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    tessdata_dir_config = '--tessdata-dir "/home/rvq/github/tesseract/tessdata/" --psm 10  --oem 2 '
    arr = Image.fromarray(img)
    result = pytesseract.image_to_string(arr, config = tessdata_dir_config)
    print(result)

work('./letter.png')