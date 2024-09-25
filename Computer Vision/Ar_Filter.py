import cv2
import mediapipe as mp

def ar_filter():
    cap = cv2.VideoCapture(0)
    mp_face_mesh = mp.solutions.face_mesh

    with mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:
        while True:
            success, img = cap.read()
            if not success:
                print("Failed to capture image.")
                break
            
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = face_mesh.process(img_rgb)

            if results.multi_face_landmarks:
                for face_landmarks in results.multi_face_landmarks:
                    mp.solutions.drawing_utils.draw_landmarks(
                        img, face_landmarks, mp_face_mesh.FACEMESH_TESSELATION)

            cv2.imshow("AR Filter Test", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    ar_filter()