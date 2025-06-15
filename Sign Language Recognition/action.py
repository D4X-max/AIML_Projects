import cv2
import os
import mediapipe as mp

DATA_DIR = 'data'
labels = ['A', 'B', 'C']  # Replace with your chosen signs
num_images = 200

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

for label in labels:
    os.makedirs(os.path.join(DATA_DIR, label), exist_ok=True)
    cap = cv2.VideoCapture(0)
    print(f'Collecting images for {label}. Press "q" to quit.')

    count = 0
    while count < num_images:
        ret, frame = cap.read()
        if not ret:
            continue
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(frame_rgb)

        if result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, result.multi_hand_landmarks[0], mp_hands.HAND_CONNECTIONS)
            img_path = os.path.join(DATA_DIR, label, f'{count}.jpg')
            cv2.imwrite(img_path, frame)
            count += 1

        cv2.imshow('Collecting Data', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
