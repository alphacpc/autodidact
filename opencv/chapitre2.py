#***********Fonctions basiques**********

import cv2;
import numpy as np;

img = cv2.imread("assets/zulu.jpg");

kernel = np.ones((5,5),np.uint8);

#Basic Functions
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
imgCanny = cv2.Canny(img, 200, 200);
imgBlur = cv2.GaussianBlur(imgGray, (7,7),0);
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1);
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

imgHori = np.hstack((imgGray, imgBlur, imgCanny, imgDialation, imgEroded))

# cv2.imshow("Image",img);
# cv2.imshow("Image gris",imgGray);
# cv2.imshow("Image canny",imgCanny);
# cv2.imshow("Image Blur",imgBlur);
# cv2.imshow("Image Dialation", imgDialation);
# cv2.imshow("Image Erode", imgEroded);
cv2.imshow("Images", imgHori);

cv2.waitKey(0);

cv2.destroyAllWindows()