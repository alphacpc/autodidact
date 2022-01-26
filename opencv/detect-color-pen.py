import cv2;
import numpy as np;


frameWeight = 640;
frameHeight = 480;

def empty():
    pass

cv2.namedWindow("TrackBars");
cv2.resizeWindow("TrackBars",640,240);
cv2.createTrackbar("Couleur min","TrackBars",0,170,empty);
cv2.createTrackbar("Couleur max","TrackBars",193,255,empty);
cv2.createTrackbar("Sat min","TrackBars",91,255,empty);
cv2.createTrackbar("Sat max","TrackBars",255,255,empty);
cv2.createTrackbar("Val min","TrackBars",43,255,empty);
cv2.createTrackbar("Val max","TrackBars",255,255,empty);


def findColor(img):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV);
    h_min = cv2.getTrackbarPos("Couleur min", "TrackBars");
    h_max = cv2.getTrackbarPos("Couleur max", "TrackBars");
    s_min = cv2.getTrackbarPos("Sat min", "TrackBars");
    s_max = cv2.getTrackbarPos("Sat max", "TrackBars");
    v_min = cv2.getTrackbarPos("Val min", "TrackBars");
    v_max = cv2.getTrackbarPos("Val max", "TrackBars");

    lower = np.array([h_min, s_min, v_min]);
    upper = np.array([h_max, s_max, v_max]);
    mask = cv2.inRange(imgHSV,lower,upper);
    imgResult = cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("Mask", mask);

video = cv2.VideoCapture(0);
video.set(3,frameWeight);
video.set(4,frameHeight);
video.set(10,200);

fps = video.get(cv2.CAP_PROP_FPS)

while True:
    success, frame = video.read();

    if success == True:
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
        cv2.imshow("Live streaming", frame);
        waitKey = cv2.waitKey(int(1000/fps))
        
        if waitKey == ord("q"):
            print("fin du programme !");
            break

cv2.destroyAllWindows();