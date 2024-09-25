import cv2
import numpy as np
import tkinter as tk
from threading import Thread
from cvzone.HandTrackingModule import HandDetector
from cvzone.FaceDetectionModule import FaceDetector
from deepface import DeepFace
import mediapipe as mp

class CVApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unique CV Program GUI")
        self.root.geometry("400x600")
        self.root.configure(bg="#f0f0f0")
        
        # Initialize variables
        self.cap = None
        self.running = False  # To control the video capture thread
        self.face_thread = None
        self.hand_thread = None
        self.object_thread = None
        self.motion_thread = None
        self.gesture_thread = None
        self.ar_thread = None  # Thread for AR filter
        self.emotion_thread = None  # Thread for emotion detection

        # Create a title label
        tk.Label(root, text="Choose Functionality", font=("Helvetica", 16), bg="#f0f0f0").grid(row=0, columnspan=3, pady=(10, 20))

        # Create buttons for different functionalities
        btn_style = {
            "font": ("Helvetica", 12),
            "bg": "#4CAF50",
            "fg": "white",
            "activebackground": "#45a049",
            "width": 20,
            "height": 2
        }

        tk.Button(root, text="Hand Tracking", command=self.start_hand_tracking, **btn_style).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(root, text="Face Detection", command=self.start_face_detection, **btn_style).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(root, text="Object Detection", command=self.start_object_detection, **btn_style).grid(row=1, column=2, padx=10, pady=10)
        tk.Button(root, text="Motion Detection", command=self.start_motion_detection, **btn_style).grid(row=2, column=0, padx=10, pady=10)
        tk.Button(root, text="Gesture Recognition", command=self.start_gesture_recognition, **btn_style).grid(row=2, column=1, padx=10, pady=10)
        tk.Button(root, text="AR Filter", command=self.start_ar_filter, **btn_style).grid(row=2, column=2, padx=10, pady=10)
        tk.Button(root, text="Emotion Detection", command=self.start_emotion_detection, **btn_style).grid(row=3, column=0, padx=10, pady=10)
        tk.Button(root, text="Real-time Image Filters", command=self.start_image_filters, **btn_style).grid(row=3, column=1, padx=10, pady=10)
        tk.Button(root, text="Exit", command=self.close_app, **btn_style).grid(row=3, column=2, pady=(20, 10))

    def close_app(self):
        self.running = False
        if self.cap is not None:
            self.cap.release()
            cv2.destroyAllWindows()
        self.root.quit()  # Close the tkinter window

        # Wait for the threads to finish
        if self.face_thread is not None:
            self.face_thread.join()
        if self.hand_thread is not None:
            self.hand_thread.join()
        if self.object_thread is not None:
            self.object_thread.join()
        if self.motion_thread is not None:
            self.motion_thread.join()
        if self.gesture_thread is not None:
            self.gesture_thread.join()
        if self.ar_thread is not None:
            self.ar_thread.join()
        if self.emotion_thread is not None:
            self.emotion_thread.join()

    def start_hand_tracking(self):
        if self.cap is None:
            self.cap = cv2.VideoCapture(0)
            self.running = True
            self.hand_thread = Thread(target=self.hand_tracking)
            self.hand_thread.start()

    def hand_tracking(self):
        detector = HandDetector(detectionCon=0.8)
        rectList = [np.random.randint(100, 400, size=2) for _ in range(5)]
        while self.running:
            success, img = self.cap.read()
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

        self.cap.release()
        cv2.destroyAllWindows()

    def start_face_detection(self):
        if self.cap is None:
            self.cap = cv2.VideoCapture(0)
            self.running = True
            self.face_thread = Thread(target=self.face_detection)
            self.face_thread.start()

    def face_detection(self):
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        while self.running:
            success, img = self.cap.read()
            if not success:
                break
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=5)

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            cv2.imshow("Face Detection", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def start_object_detection(self):
        if self.cap is None:
            self.cap = cv2.VideoCapture(0)
            self.running = True
            self.object_thread = Thread(target=self.object_detection)
            self.object_thread.start()

    def object_detection(self):
        while self.running:
            success, img = self.cap.read()
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

        self.cap.release()
        cv2.destroyAllWindows()

    def start_motion_detection(self):
        if self.cap is None:
            self.cap = cv2.VideoCapture(0)
            self.running = True
            self.motion_thread = Thread(target=self.motion_detection)
            self.motion_thread.start()

    def motion_detection(self):
        ret, frame1 = self.cap.read()
        ret, frame2 = self.cap.read()
        while self.running:
            diff = cv2.absdiff(frame1, frame2)
            gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (5, 5), 0)
            _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
            dilated = cv2.dilate(thresh, None, iterations=3)
            contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            for contour in contours:
                if cv2.contourArea(contour) > 500:
                    (x, y, w, h) = cv2.boundingRect(contour)
                    cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.imshow("Motion Detection", frame1)
            frame1 = frame2
            ret, frame2 = self.cap.read()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def start_gesture_recognition(self):
        if self.cap is None:
            self.cap = cv2.VideoCapture(0)
            self.running = True
            self.gesture_thread = Thread(target=self.gesture_recognition)
            self.gesture_thread.start()

    def gesture_recognition(self):
        mp_hands = mp.solutions.hands
        hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.7)
        while self.running:
            success, img = self.cap.read()
            if not success:
                break
            img = cv2.flip(img, 1)
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = hands.process(img_rgb)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    for id, lm in enumerate(hand_landmarks.landmark):
                        h, w, _ = img.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

            cv2.imshow("Gesture Recognition", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def start_ar_filter(self):
        if self.cap is None:
            self.cap = cv2.VideoCapture(0)
            self.running = True
            self.ar_thread = Thread(target=self.ar_filter)
            self.ar_thread.start()

    def ar_filter(self):
        # Initialize webcam
        cap = cv2.VideoCapture(0)
        # Initialize FaceMesh module
        mp_face_mesh = mp.solutions.face_mesh
        # Start FaceMesh
        with mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:
            while True:
                success, img = cap.read()
                if not success:
                    print("Failed to capture image.")
                    break
        
                img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                results = face_mesh.process(img_rgb)

                # Check if any face landmarks are found
                if results.multi_face_landmarks:
                    for face_landmarks in results.multi_face_landmarks:
                        # Use FACEMESH_TESSELATION to draw landmarks
                        mp.solutions.drawing_utils.draw_landmarks(
                            img, face_landmarks, mp_face_mesh.FACEMESH_TESSELATION)

                # Show the image with landmarks
                cv2.imshow("AR Filter Test", img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        # Release the webcam and close windows
        cap.release()
        cv2.destroyAllWindows()






    def start_emotion_detection(self):
        if self.cap is None:
            self.cap = cv2.VideoCapture(0)
            self.running = True
            self.emotion_thread = Thread(target=self.emotion_detection)
            self.emotion_thread.start()

    def emotion_detection(self):
        while self.running:
            success, img = self.cap.read()
            if not success:
                break
            
            try:
                # Analyze emotion
                result = DeepFace.analyze(img, actions=['emotion'], enforce_detection=False)
                emotion = result[0]['dominant_emotion']
                cv2.putText(img, f'Emotion: {emotion}', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            except Exception as e:
                print(f"Error in emotion detection: {e}")

            cv2.imshow("Emotion Detection", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def start_image_filters(self):
        if self.cap is None:
            self.cap = cv2.VideoCapture(0)
            self.running = True
            self.image_filter_thread = Thread(target=self.image_filters)
            self.image_filter_thread.start()

    def image_filters(self):
        while self.running:
            success, img = self.cap.read()
            if not success:
                break
            
            # Applying a grayscale filter as an example
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imshow("Real-time Image Filter (Grayscale)", img_gray)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = tk.Tk()
    app = CVApp(root)
    root.mainloop()
