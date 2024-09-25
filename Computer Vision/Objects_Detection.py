import cv2
import numpy as np

def object_detection():
    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        if not success:
            break

        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower_color = np.array([100, 150, 0])
        upper_color = np.array([140, 255, 255])
        mask = cv2.inRange(img_hsv, lower_color, upper_color)

        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) > 500:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("Object Detection", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    object_detection()