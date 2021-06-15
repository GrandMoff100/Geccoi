import cv2
from ..detector import Detector


class HandDetector(Detector):
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
