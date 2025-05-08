# Virtual Mouse Using Hand Gestures

This project allows you to control the mouse on your computer using hand gestures detected through your webcam. Using MediaPipe's Hand Landmark model, the program recognizes hand gestures and translates them into mouse actions such as moving the cursor and clicking. The project leverages Python libraries such as OpenCV, MediaPipe, and PyAutoGUI.

## Features

- **Mouse Movement:** The index finger's position is tracked and mapped to the screen coordinates to move the mouse cursor.
- **Mouse Click:** A "fist" gesture is recognized and used to simulate a mouse click.
- **Gesture Recognition:** The program can recognize hand gestures, including:
  - "Fist" (all fingers are folded)
  - "Thumbs Up" (thumb extended, other fingers folded)

## Requirements

- Python 3.x
- OpenCV
- Mediapipe
- PyAutoGUI

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/vishnuI262/Virtual-Mouse-Controller.git
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure you have a working webcam connected to your system.

## Running the Project

1. Navigate to the project directory:
    ```bash
    cd Virtual-Mouse-Controller
    ```

2. Run the main Python script:
    ```bash
    python virtual_mouse.py
    ```

3. The webcam window will open. Perform hand gestures in front of the camera to control the mouse.

   - **Thumbs Up**: Simulates a mouse click.
   - **Fist**: Another mouse click gesture.
   - **Index Finger Movement**: Moves the cursor based on the index finger's position.

4. To exit the program, press the **Esc** key.

## How It Works

- **Hand Gesture Detection:** The program captures video from the webcam and processes it frame by frame using MediaPipe's Hand Landmark model to detect key points of the hand (21 landmarks).
- **Cursor Movement:** Based on the index finger's position, the program maps the finger's normalized coordinates to screen coordinates and moves the mouse using PyAutoGUI.
- **Gesture Recognition:** Custom logic is used to detect a "fist" or "thumbs up" gesture, and the corresponding action is triggered (clicking the mouse).

## Troubleshooting

- **No hand detected:** Ensure your hand is visible to the camera and positioned within the frame. The detection is more accurate when the hand is within the camera's view.
- **Cursor movement is too fast or slow:** You can adjust the sensitivity of the cursor movement by modifying the code where the position is mapped.

## Acknowledgements

- **MediaPipe:** A cross-platform framework for building pipelines to process video, audio, and other multimedia types. Used for hand gesture recognition.
- **OpenCV:** A computer vision library used to capture webcam frames and process images.
- **PyAutoGUI:** A library used for GUI automation, including controlling the mouse and keyboard.

---

Feel free to modify the repository and enhance it with additional gestures and features!

