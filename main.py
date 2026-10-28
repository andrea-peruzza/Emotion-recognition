# ===============================================
#  PROGRAM: Facial Expression Recognition
#  DESCRIPTION:
#     - Uses the computer webcam to detect faces.
#     - Analyzes facial expressions (happy, sad, angry, etc.).
#     - Displays an image corresponding to the detected emotion on the screen.
# ===============================================

# Import required libraries
import cv2              # OpenCV: for webcam handling and displaying images
from fer import FER      # FER (Facial Expression Recognition): to detect emotions from faces


# Initialize webcam

# cv2.VideoCapture(0) opens the computer's default webcam
camera = cv2.VideoCapture(0)


# Initialize emotion detector

# mtcnn=True specifies using MTCNN for better face detection
detector = FER(mtcnn=True)


# Map each emotion to its corresponding image path
# Images must be located in the "images" folder (e.g. "images/happy.png")
emotion_images = {
    "happy": "images/happy.png",
    "sad": "images/sad.png",
    "angry": "images/angry.png",
    "surprise": "images/surprised.png",
    "neutral": "images/neutral.png"
}


# Main loop

# Read and analyze frames while the webcam is active
while True:
    # Read a frame from the webcam
    ret, frame = camera.read()

    # If the frame could not be read (e.g. webcam disconnected), exit loop
    if not ret:
        break

    # Emotion detection in current frame
    # detect_emotions() returns a list of dictionaries with emotions and their scores
    result = detector.detect_emotions(frame)

    if result:
        # Extract emotions dictionary from the first detected face
        emotions = result[0]["emotions"]

        # Find the emotion with the highest score
        dominant_emotion = max(emotions, key=emotions.get)

        # Create overlay text to display on screen (e.g. "Emotion: happy")
        text = f"Emotion: {dominant_emotion}"


        # cv2.putText draws text onto the frame (image)
        cv2.putText(
            frame,                   # image to write on
            text,                    # text string to write
            (10, 40),                # position (x, y) of text
            cv2.FONT_HERSHEY_SIMPLEX,# font type
            1,                       # font scale
            (255, 255, 255),         # text color (white)
            2                        # thickness
        )

        # Load corresponding image (fallback to "neutral" if not found)
        img = cv2.imread(emotion_images.get(dominant_emotion, "images/neutral.png"))

        # Resize image to 150x150 pixels to fit the window
        img = cv2.resize(img, (150, 150))

        # Overlay the image onto top-left corner of frame (y:x coordinates)
        frame[10:160, 10:160] = img

    
    # Display the result on screen
    
    cv2.imshow("Emotion Mapper", frame)

    # Press 'q' to exit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Release the webcam and close all OpenCV windows
camera.release()
cv2.destroyAllWindows()
