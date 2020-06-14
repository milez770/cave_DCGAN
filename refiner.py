## import
import numpy as np
import argparse
import imutils
import cv2
import os
import random

imgDir = './caves_bing'
counter = 0
imnum = 800

## crop, reorient
for img_name in os.listdir(imgDir):
    # print(img_name)

    img = cv2.imread(os.path.join(imgDir, img_name))
    if img is not None:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.threshold(blurred, 100, 200, cv2.THRESH_BINARY)[1]

        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        cntscount = 0
        ccX = 0
        ccY = 0
        for c in cnts:
            try:
                # print(c)
                M = cv2.moments(c)
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])

                ccX += cX
                ccY += cY

                cntscount += 1

                #

            except ZeroDivisionError:
                print('')
        # if(counter < 1):
        try:
            ccX /= cntscount
            ccY /= cntscount
        except:
            continue

        # cv2.circle(img, (int(ccX), int(ccY) ), 7, (255, 255, 255), -1)
        # cv2.putText(img, "center", (ccX - 20, ccY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2

        height, width, channels = img.shape
        sx =0
        sy=0
        tx=0
        ty=0
        for ii in range(1, 5):
            rnum = round(10 - random.randint(1, 20))
            tccX = ccX + rnum
            tccY = ccY + rnum
            if(height > width):
                sx = 0
                tx = width
                if(tccY < width/2):
                    sy = 0
                    ty = width + rnum
                    continue
                elif(tccY +width/2 > height):
                    sy = height - width - rnum
                    ty = height - rnum
                    continue
                else:
                    sy = int(tccY - width / 2)
                    ty = int(tccY + width / 2)

            else:
                sy = 0
                ty = height
                if(tccX < height/2):
                    sx = 0
                    tx = height + rnum
                    continue
                elif(tccX +height/2 > width):
                    sx = width - height - rnum
                    tx = width - rnum
                    continue
                else:
                    sx = int(tccX - height / 2)
                    tx = int(tccX + height / 2)

            try:
                # if(imnum > 3361):
                    crop_img = img[sy:ty, sx:tx]
                    ratio = 200/ (ty-sy)
                    print(ratio)

                    dst2 = cv2.resize(crop_img, dsize=(0, 0), fx=ratio, fy=ratio, interpolation=cv2.INTER_AREA)
                    # print(sy, ty, sx, tx)
                    print(str(imnum).zfill(5))

                    cv2.imwrite("./cropped/"+str(imnum).zfill(5)+".jpg", dst2)
                    # cv2.waitKey(0)

                    imnum += 1
            except:
                print('err')


print('finished')

## reflect then save
imnum = 4120
for img_name in os.listdir(imgDir):
    img = cv2.imread(os.path.join(imgDir, img_name))
    horizontal_img = cv2.flip( img, 0 )

    #saving now
    cv2.imwrite('./caves_bing' + str(imnum).zfill(5) + '.jpg', horizontal_img)
    imnum += 1