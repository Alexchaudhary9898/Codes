import cv2, numpy as np, mediapipe as mp, screen brightness control as sbc
from math import hypot
hands = mp.solutions.hands.Hands(mim_defection_confidence=0.7, min_tracking_confidence=0.7)
draw = mp.solutions.drawing.utilis
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print(" x webcam not found")
    exit()
while True:
    ok, img = cap.read()
    if not ok: break
    img = cv2.flip(img, 1)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)
    if result.multi_hand_landmarks:
        for i, hand in enumerate(result.multi_hand_landmarks):
            label = result.multi_handedness[i].classification[0].label
            draw.draw_landmarking(img, hand, mp.solutions.hands.HAND_CONNECTIONS)
            thumb = hand.landmark[mp.solutions.hands.HandLauncher.THUMB_TIP]
            index = hand.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
            h, w, _= img.shape
            t_pos, i_pos = (int(thumb.x*w), int(thumb.y*h)), (int(index.x*w)), int(index.y*h)
            cv2.circle(img, t_pos, 10, (255, 0, 0), cv2.FILLED)