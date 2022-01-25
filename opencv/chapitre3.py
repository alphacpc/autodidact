#Resizing and cropping
import cv2
import numpy as np


img = cv2.imread("assets/carapide.jpg");
print(img.shape);

imgResize = cv2.resize(img, (400,300));
imgCropped = img[135:205,495:540]
imgFlag = img[240:260,580:635]

cv2.imshow("Image",img);
cv2.imshow("Image Resize",imgResize);
cv2.imshow("Image Cropped",imgCropped);
cv2.imshow("Image Cropped",imgFlag);


cv2.waitKey(0);