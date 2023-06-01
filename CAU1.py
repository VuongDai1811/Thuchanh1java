# -*- coding: utf-8 -*-

import cv2
import os #dung lưu ảnh
#đuongan
path = r'D:\baitapanhanh1.jpg'
path1 = r'D:\baitapanh'

#docanh
img = cv2.imread(path)
#hienthianh
cv2.imshow('Cua so', img)

#luuanh
os.chdir(path1)
fileName = 'anhmoi.png'
cv2.imwrite(fileName, img)
print('thanh cong')
cv2.waitKey()


