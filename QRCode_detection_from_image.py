import cv2
import numpy as np
from pyzbar.pyzbar import decode


img = cv2.imread('test.jpg')
# w,h,c =img.shape

code = decode(img)

for barcode in decode(img):
    print(barcode.data)
    print(barcode.rect)
    myData = barcode.data.decode('utf-8')
    print(myData)
    
# img = cv2.resize(img,(w//2,h//2))    
    
    
cv2.imshow('sample_image', img) 
cv2.waitKey()   
# print(code)