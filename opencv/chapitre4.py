import cv2;
import numpy as np;


img = np.zeros((600,800,3), np.uint8)

img[:] = (250,0,0);

cv2.line(img, (0,0), (img.shape[1], img.shape[0]),(255,255,255),2);
cv2.line(img, (img.shape[1],0), (0, img.shape[0]),(255,255,255),2);
cv2.rectangle(img,(260,20), (520,150), (255,0,255),2);
cv2.circle(img, (130,280), 100, (0,255,255), 2);
cv2.circle(img, (630,300), 100, (0,255,255), 2);
cv2.putText(img, "CHAPITRE 4", (300,500), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0),1)

cv2.imshow("Image",img)

cv2.waitKey(0)