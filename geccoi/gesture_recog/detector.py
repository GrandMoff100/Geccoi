import mediapipe as mp
import cv2


class Detector:
    WRIST = 0
    THUMB = 4
    INDEX = 8
    MIDDLE = 12
    RING = 16
    PINKY = 20
    UPPER_PALM = 9

    def __init__(self, mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.mode = mode
        self.max_num_hands = max_num_hands
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence

        self.hands = mp.solutions.hands.Hands(self.mode, self.max_num_hands,
                                              self.min_detection_confidence, self.min_tracking_confidence)
        self.drawing_utils = mp.solutions.drawing_utils
        self.results = None

    def find_hands(self, img, draw=False):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        self.results = self.hands.process(img)

        if self.results.multi_hand_landmarks:
            for hand in self.results.multi_hand_landmarks:
                if draw:
                    self.drawing_utils.draw_landmarks(img, hand, mp.solutions.hands.HAND_CONNECTIONS)

        return img

    def get_gesture(self, landmarks):
        ...
