import cv2;
import numpy as np

img = cv2.imread("assets/carte1.jpg");
img2 = cv2.imread("assets/carte.jpeg")
print(img2.shape);

imgResize = cv2.resize(img2, (800,800))

W, H = 250,350
pts1 = np.float32([[110,48],[292,24],[145,310],[345,275]]);
pts2 = np.float32([[0,0],[W,0],[0,H],[W,H]]);

pts3 = np.float32([[488,147],[777,335],[162,500],[445,714]]);

matrix = cv2.getPerspectiveTransform(pts1,pts2);
imgOut = cv2.warpPerspective(img,matrix,(W,H))

matrix2 = cv2.getPerspectiveTransform(pts3,pts2);
imgOut2 = cv2.warpPerspective(imgResize,matrix2,(W,H))



# cv2.imshow("Image des cartes",img);
# cv2.imshow("Image",imgOut);
cv2.imshow("Image",imgOut2);

cv2.waitKey(0);