import cv2;
import numpy as np;


def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE);
    objectType = ""
    for cnt in  contours:
        area = cv2.contourArea(cnt)
        print(area);
        if area > 100:
            cv2.drawContours(imgContour,cnt, -1, (0,0,0), 3);
            peri = cv2.arcLength(cnt,True);
            approx = cv2.approxPolyDP(cnt, 0.02*peri,True);
            # print(len(approx));
            objCor = len(approx);
            x,y,w,h = cv2.boundingRect(approx);

            if objCor == 3 : objectType = "Triangle";
            
            elif objCor == 4 : 
                aspRatio = w/float(h);
                if aspRatio > 0.95 and aspRatio < 1.05 : objectType = "Carre";
                else: objectType = "Rectangle"
            elif objCor > 12 : objectType = "Cercle"
            else: objectType = "None"

            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2);
            cv2.putText(imgContour,objectType,(x+(w//2) - 40, y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,0,0),2);
            

img = cv2.imread("assets/forme1.png");
imgContour = img.copy();
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1);
imgCanny = cv2.Canny(imgBlur,50,50);
getContours(imgCanny);
allImg = np.hstack((imgGray, imgCanny));
allImgColor = np.hstack((img,imgContour));

# cv2.imshow("Image", img);
# cv2.imshow("Image Gray", imgGray);
# cv2.imshow("Image Canny", imgCanny);
cv2.imshow("All Image gray", allImg);
cv2.imshow("All Image color", allImgColor);

cv2.waitKey(0);

cv2.destroyAllWindows();