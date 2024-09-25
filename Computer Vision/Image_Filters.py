import cv2
import tkinter as tk
from threading import Thread

class FilterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Filter Application")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")

        # Button style
        btn_style = {
            "font": ("Helvetica", 14),
            "bg": "#4CAF50",
            "fg": "white",
            "activebackground": "#45a049",
            "width": 20,
            "height": 3,
        }

        # Title Label
        tk.Label(root, text="Choose an Image Filter", font=("Helvetica", 18), bg="#f0f0f0").pack(pady=20)

        # Buttons for different filters
        tk.Button(root, text="Grayscale Filter", command=self.apply_grayscale, **btn_style).pack(pady=10)
        tk.Button(root, text="Blur Filter", command=self.apply_blur, **btn_style).pack(pady=10)
        tk.Button(root, text="Edge Detection", command=self.apply_edges, **btn_style).pack(pady=10)
        tk.Button(root, text="Exit", command=root.quit, **btn_style).pack(pady=10)

    def apply_grayscale(self):
        Thread(target=self.run_grayscale).start()

    def run_grayscale(self):
        cap = cv2.VideoCapture(0)

        while True:
            success, img = cap.read()
            if not success:
                break

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imshow("Grayscale", gray)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def apply_blur(self):
        Thread(target=self.run_blur).start()

    def run_blur(self):
        cap = cv2.VideoCapture(0)

        while True:
            success, img = cap.read()
            if not success:
                break

            blurred = cv2.GaussianBlur(img, (15, 15), 0)
            cv2.imshow("Blurred", blurred)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def apply_edges(self):
        Thread(target=self.run_edges).start()

    def run_edges(self):
        cap = cv2.VideoCapture(0)

        while True:
            success, img = cap.read()
            if not success:
                break

            edges = cv2.Canny(img, 100, 200)
            cv2.imshow("Edges", edges)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = tk.Tk()
    app = FilterApp(root)
    root.mainloop()
