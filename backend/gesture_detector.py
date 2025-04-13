# backend/gesture_detector.py
import cv2
import mediapipe as mp

class GestureDetector:
    def __init__(self):
        self.hands = mp.solutions.hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
        self.drawer = mp.solutions.drawing_utils

    def get_gesture(self, frame):
        gesture = "none"
        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                lmList = [(int(lm.x * w), int(lm.y * h)) for lm in hand_landmarks.landmark]
                self.drawer.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)

                fingers = [0, 0, 0, 0, 0]
                tipIds = [4, 8, 12, 16, 20]
                for i in range(1, 5):
                    if lmList[tipIds[i]][1] < lmList[tipIds[i]-2][1]:
                        fingers[i] = 1

                if fingers == [0, 1, 0, 0, 0]:
                    gesture = "point"
                elif fingers == [0, 1, 1, 0, 0]:
                    gesture = "peace"
                elif fingers == [0, 1, 1, 1, 1]:
                    gesture = "swipe"
                elif fingers == [1, 0, 0, 0, 0]:
                    gesture = "thumbs_up"
                elif fingers == [0, 0, 0, 0, 0]:
                    gesture = "fist"

        return frame, gesture
