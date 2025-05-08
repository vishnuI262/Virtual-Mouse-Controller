import cv2
import mediapipe as mp
import pyautogui
import time

mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
    max_num_hands=1
)

draw = mp.solutions.drawing_utils

screen_width, screen_height = pyautogui.size()

def recognize_gesture(landmarks_list):
    if len(landmarks_list) == 21:
        if landmarks_list[4][1] > landmarks_list[3][1] and landmarks_list[8][1] > landmarks_list[6][1] and landmarks_list[12][1] > landmarks_list[10][1]:
            return "Fist"
        elif landmarks_list[4][1] < landmarks_list[3][1] and landmarks_list[4][1] < landmarks_list[2][1]:
            if landmarks_list[8][1] > landmarks_list[6][1] and landmarks_list[12][1] > landmarks_list[10][1]:
                return "Thumbs Up"
        return "Unknown Gesture"
    return "No Hand Detected"

def move_cursor(landmarks_list):
    if len(landmarks_list) == 21:
        x = int(landmarks_list[8][0] * screen_width)
        y = int(landmarks_list[8][1] * screen_height)
        pyautogui.moveTo(x, y)

def click_mouse(gesture):
    if gesture == "Fist":
        pyautogui.click()

cap = cv2.VideoCapture(0)

time.sleep(2)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    processed = hands.process(frameRGB)
    
    landmarks_list = []

    if processed.multi_hand_landmarks:
        hand_landmarks = processed.multi_hand_landmarks[0]

        draw.draw_landmarks(frame, hand_landmarks, mpHands.HAND_CONNECTIONS)

        for lm in hand_landmarks.landmark:
            landmarks_list.append((lm.x, lm.y))

        gesture = recognize_gesture(landmarks_list)

        move_cursor(landmarks_list)

        click_mouse(gesture)

        cv2.putText(frame, f'Gesture: {gesture}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Virtual Mouse', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
