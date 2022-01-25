import cv2;
import numpy as np

img = cv2.imread("assets/carte1.jpg");
print(img.shape);

W, H = 250,350
pts1 = np.float32([[110,48],[292,24],[345,275], [145,310]]);
pts2 = np.float32([[0,0],[W,0],[0,H],[W,H]]);

matrix = cv2.getPerspectiveTransform(pts1,pts2);
imgOut = cv2.warpPerspective(img,matrix,(W,H))



cv2.imshow("Image des cartes",img);
cv2.imshow("Image",imgOut);

cv2.waitKey(0);