# Emotion Recognition

A simple Python program that uses your computer webcam to recognize facial expressions in real time.

## What it does
- Turns on the webcam and detects a face.
- Analyzes facial expressions (happy, sad, angry, surprised, or neutral).
- Displays the detected emotion name on the screen.
- Overlays a corresponding image from the Images folder in the top-left corner of the video.

## Installation
Requires Python installed on your machine. Open a terminal in the project folder and install the required libraries:

```bash
pip install opencv-python fer tensorflow
```

If you have a requirements.txt file, install everything with:

```bash
pip install -r requirements.txt
```

## How to run
1. Run the script:
```bash
python main.py
```
2. A window will open showing the live webcam feed.
3. To exit the program, press the "q" key on your keyboard.

## License
This project is licensed under the PolyForm Noncommercial License 1.0.0. See the LICENSE file for details.