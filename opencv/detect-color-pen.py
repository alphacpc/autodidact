from turtle import up
import cv2;
import numpy as np;

video = cv2.VideoCapture(0);
video.set(10, 200);

#BLUE,27,144,60,105,59,147
#VERT 48,113,0,129,20,82
#ROUGE 0,6,30,167,0,87
myColors = [[27,144,60,105,59,147],
            [48,113,0,129,20,82],
            [0,6,30,167,0,87]];

myColorValues = [[255,0,0], #BGR
                [0,255,0],
                [0,0,255]]

myPoints = [] ## x,y,colorId  

def findColor(frame,myColors,myColorsValues):
    imgHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV);
    count = 0;
    newPoints= []
    for color in myColors:
        lower = np.array([color[0],color[2],color[4]]);
        upper = np.array([color[1],color[3],color[5]]);
        mask = cv2.inRange(imgHSV,lower,upper);
        x,y = getContours(mask);
        cv2.circle(frameResult,(x,y),5,myColorValues[count],cv2.FILLED);
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count += 1
        # cv2.imshow(str(color[0]),mask);
    return newPoints


def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE);
    x,w,y,h = 0,0,0,0
    for cnt in  contours:
        area = cv2.contourArea(cnt)
        # print(area);
        if area > 100:
            #cv2.drawContours(frameResult,cnt, -1, (0,0,0), 3);
            peri = cv2.arcLength(cnt,True);
            approx = cv2.approxPolyDP(cnt, 0.02*peri,True);
            x,y,w,h = cv2.boundingRect(approx);
    return x+w//2 , y

def DrawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(frameResult,(point[0],point[1]),20,myColorValues[point[2]],cv2.FILLED);

while True:
    success, frame = video.read();
    frameResult = frame.copy();
    newPoints = findColor(frame, myColors, myColorValues);
    if len(newPoints) !=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints) !=0:
        DrawOnCanvas(myPoints, myColorValues);

    cv2.imshow("Resultat",frameResult);
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows();