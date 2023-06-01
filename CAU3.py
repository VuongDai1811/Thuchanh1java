# -*- coding: utf-8 -*-


import cv2
import os
path = r'D:\baitapanh\anh1.jpg'

#docanh luc dau

img = cv2.imread(path) #anhdau

img1 = cv2.imread(path, cv2.IMREAD_GRAYSCALE) #anhcapsam

#hienthianh
cv2.imshow("anh goc: ", img)
cv2.imshow("anh cap xam vua chuyen: ", img1)

#chuyenanhnhiphan
img_binary = cv2.adaptiveThreshold(img1, maxValue = 255, adaptiveMethod = cv2.ADAPTIVE_THRESH_MEAN_C,
                                   thresholdType = cv2.THRESH_BINARY, blockSize=15, C = 8)

cv2.imshow("anh nhi phan: ", img_binary)
# Luuanhcapsam

# fileName = "anhchuyenxam.png"
# cv2.imwrite (fileName, img1)
# print (' Luu thanh cong anh xam')

# #luuanhnhiphan
# fileName1 = "anhnhiphan.jpg"
# cv2.imwrite (fileName1, img_binary)

cv2.waitKey()
