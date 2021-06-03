import cv2
import mediapipe as mp


class HandDetector:
    def __init__(self, mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.mode = mode
        self.max_num_hands = max_num_hands
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence

        self.hands = self.mp.solutions.hands.Hands(self.mode, self.max_num_hands,
                                                   self.min_detection_confidence, self.min_tracking_confidence)
        self.drawing_utils = mp.solutions.drawing_utils

    def find_hands(self, img, draw=False):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        self.results = self.hands.process(img)

        if self.results.multi_hand_landmarks:
            for hand in self.results.multi_hand_landmarks:
                if draw:
                    self.drawing_utils.draw_landmarks(img, hand, mp.solutions.hands.HAND_CONNECTIONS)

        return img

    def find_position(self, img, list=True, point=None, hand_num=0, draw=False):
        if list:
            landmark_list = []
            if self.results.multi_hand_landmarks:
                landmarks = self.results.multi_hand_landmarks[hand_num]
                h, w, c = img.shape
                for id, lm in enumerate(landmarks.landmark):
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    landmark_list.append([id, cx, cy])
                    if draw:
                        cv2.circle(img, (cx, cy), 15, (255, 255, 255), cv2.FILLED)

                return landmark_list

            elif point:
                return {"x": landmark_list[point][1], "y": landmark_list[point][2]}


if __name__ == "__main__":
    pass
