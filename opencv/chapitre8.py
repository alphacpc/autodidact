import cv2;

facesCascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml");
img = cv2.imread("assets/zulu.jpg");
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);

faces = facesCascade.detectMultiScale(imgGray,1.1,4);

for (x,y,w, h) in faces :
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,255),2)

cv2.imshow("Image Chacka Zulu", img);

cv2.waitKey(0);

cv2.destroyAllWindows();