# main.py
import cv2
from backend.gesture_detector import GestureDetector
from frontend.matrix_animation import MatrixAnimation

def main():
    cap = cv2.VideoCapture(0)
    gesture_detector = GestureDetector()
    matrix = MatrixAnimation()

    while cap.isOpened() and matrix.running:
        success, frame = cap.read()
        if not success:
            break

        frame, gesture = gesture_detector.get_gesture(frame)
        matrix.update_effect(gesture)

        matrix.run(gesture)
        cv2.imshow('Webcam - Gesture Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            matrix.running = False
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
