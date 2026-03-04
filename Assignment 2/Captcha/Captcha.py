#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 21:27:19 2026

@author: jathinmadineni
"""

import random
import string
import sys
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

w = 220
h = 100
captcha_length = 6


def generateCode():
    charsAndDigits = string.ascii_letters + string.digits
    result = ""
    for i in range(captcha_length):
        result += random.choice(charsAndDigits)
    return result


def drawBackgroundNoise(drawObj):
    # random lines
    line_count = random.randint(2, 5)
    for i in range(line_count):
        x1 = random.randint(0, w)
        y1 = random.randint(0, h)
        x2 = random.randint(0, w)
        y2 = random.randint(0, h)
        drawObj.line((x1, y1, x2, y2), fill=(170, 170, 170), width=1)

    # random dots
    dot_count = random.randint(25, 60)
    for i in range(dot_count):
        x = random.randint(0, w)
        y = random.randint(0, h)
        drawObj.point((x, y), fill=(140, 140, 140))


def createCaptchaImage(codeText):

    img = Image.new("RGB", (w, h), (255, 255, 255))
    drawObj = ImageDraw.Draw(img)

    try:
        fontStyle = ImageFont.truetype("arial.ttf", 34)
    except:
        fontStyle = ImageFont.load_default()

    x_pos = 20

    for letter in codeText:
        y_random = random.randint(-6, 6)
        drawObj.text((x_pos, 35 + y_random), letter, font=fontStyle, fill=(0, 0, 0))
        x_pos += random.randint(25, 32)

    drawBackgroundNoise(drawObj)

    img = img.filter(ImageFilter.SMOOTH)

    fileName = "captcha_2" + str(random.randint(1000, 9999)) + ".png"
    img.save(fileName)

    return fileName


def showCaptcha(fileName):

    if sys.platform.startswith("win"):
        os.startfile(fileName)
    elif sys.platform.startswith("darwin"):
        os.system("open " + fileName)
    else:
        os.system("xdg-open " + fileName)


print("creating captcha")

captchaText = generateCode()
imageFile = createCaptchaImage(captchaText)

showCaptcha(imageFile)

userInput = input("enter the text shown in image: ")

if userInput == captchaText:
    print("correct captcha has been entered")
else:
    print("wrong captcha")
    print("actual text was:", captchaText)