import cv2;

#Read Image
img = cv2.imread("assets/zulu.jpg");

#Read Video
video =  cv2.VideoCapture("assets/cars.mp4");
frameParSeconde = video.get(cv2.CAP_PROP_FPS);

while True:
    success, frame = video.read();

    if success :
        cv2.imshow("Video", frame);
        if cv2.waitKey(int(1000/frameParSeconde)) == ord("q"):
            break;

    else:
        print("La video n'est pas bien chargée !");
        break;

#Read Webcam
cam =  cv2.VideoCapture(0);
frameParSecondeCam = cam.get(cv2.CAP_PROP_FPS);

while True:
    success, frame = cam.read();

    if success :
        cv2.imshow("Video", frame);
        if cv2.waitKey(int(1000/frameParSecondeCam)) == ord("e"):
            break;

    else:
        print("La video n'est pas bien chargée !");
        break;


#Display
cv2.imshow("Image", img);

cv2.waitKey(0);
    
#Destroy All Windows 
cv2.destroyAllWindows();