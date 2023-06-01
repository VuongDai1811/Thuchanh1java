# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 20:36:26 2023

@author: Admin
"""

import cv2

part = r'D:\baitapanh\Hoc\anh\Anh-Avatar-Doremon-dep-ngau-cute.jpg'

img = cv2.imread(part)
cv2.imshow('anh goc: ', img)




cv2.waitKey()