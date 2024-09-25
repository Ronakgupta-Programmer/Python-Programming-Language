import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector

def hand_tracking():
    cap = cv2.VideoCapture(0)
    detector = HandDetector(detectionCon=0.8)
    rectList = [np.random.randint(100, 400, size=2) for _ in range(5)]

    while True:
        success, img = cap.read()
        if not success:
            break

        img = cv2.flip(img, 1)
        hands, img = detector.findHands(img)

        if hands:
            lmList = hands[0]['lmList']
            x1, y1 = lmList[8][0], lmList[8][1]
            cursor = [x1, y1]

            for rect in rectList:
                if (cursor[0] - 50 < rect[0] < cursor[0] + 50) and (cursor[1] - 50 < rect[1] < cursor[1] + 50):
                    rect[0], rect[1] = cursor[0], cursor[1]

        for rect in rectList:
            cv2.rectangle(img, (rect[0]-50, rect[1]-50), (rect[0]+50, rect[1]+50), (255, 0, 255), cv2.FILLED)

        cv2.imshow("Hand Tracking", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    hand_tracking()
