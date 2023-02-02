import cv2
import HandDetect
import cxrSerial

def Fcnt(cam,port):
    handDetector = HandDetect.HandDetector(min_detection_confidence=0.7)
    cap = cv2.VideoCapture(cam)
    port = port

    while True:
        status, image = cap.read()
        image = cv2.flip(image,1)
        handLandmarks = handDetector.findHandLandMarks(image=image, draw=True)
        count=0        
        if(len(handLandmarks) != 0):        
            if handLandmarks[4][3] == "Right" and handLandmarks[4][1] > handLandmarks[3][1]:       #Right Thumb
                count = count+1
            elif handLandmarks[4][3] == "Left" and handLandmarks[4][1] < handLandmarks[3][1]:       #Left Thumb
                count = count+1
            if handLandmarks[8][2] < handLandmarks[6][2]:       #Index finger
                count = count+1
            if handLandmarks[12][2] < handLandmarks[10][2]:     #Middle finger
                count = count+1
            if handLandmarks[16][2] < handLandmarks[14][2]:     #Ring finger
                count = count+1
            if handLandmarks[20][2] < handLandmarks[18][2]:     #Little finger
                count = count+1

        
                        
        cv2.putText(image, str(count), (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0),1)
        cxrSerial.SerCom(count)
        cv2.imshow("camXard", image)
        cv2.waitKey(1)            
        if cv2.getWindowProperty('camXard', cv2.WND_PROP_VISIBLE) <1:
            break
    cv2.destroyAllWindows()