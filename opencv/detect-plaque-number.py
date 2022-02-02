import cv2
from cv2 import waitKey;

platesCascade = cv2.CascadeClassifier("./haarcascade_russian_plate_number.xml");

video = cv2.VideoCapture(0);
video.set(3,680);
video.set(4,740);
video.set(10,140);
count = 1;

while True:
    success, frame = video.read();
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
    numberPlates = platesCascade.detectMultiScale(frameGray, 1.1, 4);
    print(frame.shape)
    if success:

        for (x,y,w,h) in numberPlates:
            area = w*h;

            if area > 100:
                cv2.putText(frame, "Numero de plaque", (x, y -5), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,225,0),2)
                cv2.rectangle(frame,(x,y),(x+w,y+h), (0,225,0),4);

                frameRoi = frame[y:y+h,x:x+w]
                cv2.imshow("Frame Roi", frameRoi)


        if cv2.waitKey(1) == ord("s"):
            cv2.imwrite("images-plaque/"+str(count)+".jpg",frameRoi);
            cv2.rectangle(frame, (0,200),(640,300), (0,255,0), cv2.FILLED);
            cv2.putText(frame, "Enregistrement avec succes !", (150, 260), cv2.FONT_HERSHEY_DUPLEX,2,(0,225,0),2)
            waitKey(1000);
            count +=1;

        if cv2.waitKey(1) == ord("q"):
            break;

        cv2.imshow("Video streaming",frame);


cv2.destroyAllWindows();