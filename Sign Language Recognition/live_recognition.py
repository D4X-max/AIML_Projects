import tensorflow as tf
import cv2
import mediapipe as mp
import numpy as np

# Load the trained model
model = tf.keras.models.load_model('sign_language_model.h5')

# Initialize MediaPipe and OpenCV
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

labels = ['A', 'B', 'C']  # Replace with your actual label list

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            h, w, _ = frame.shape
            x_min = int(min([lm.x for lm in hand_landmarks.landmark]) * w)
            y_min = int(min([lm.y for lm in hand_landmarks.landmark]) * h)
            x_max = int(max([lm.x for lm in hand_landmarks.landmark]) * w)
            y_max = int(max([lm.y for lm in hand_landmarks.landmark]) * h)

            # Clip coordinates to frame size
            x_min = max(0, x_min)
            y_min = max(0, y_min)
            x_max = min(w, x_max)
            y_max = min(h, y_max)

            # Crop hand region and validate
            hand_img = frame[y_min:y_max, x_min:x_max]
            if hand_img.size == 0:
                continue

            # Resize and normalize
            hand_img = cv2.resize(hand_img, (128, 128))
            hand_img = hand_img.astype('float32') / 255.0
            hand_img = np.expand_dims(hand_img, axis=0)  # Shape: (1, 128, 128, 3)

            # Predict
            pred = model.predict(hand_img)
            pred_label = labels[np.argmax(pred)]

            # Display prediction
            cv2.putText(frame, pred_label, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.imshow('Sign Language Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
