import cv2
from fer import FER
from Spotify_Playlist import create_mood_music

video_capture = cv2.VideoCapture(0)  # Initialize webcam
emotion_detector = FER()  # Initialize FER model

def detect_and_create_playlist():
    ret, frame = video_capture.read()

    if not ret:
        print("Error accessing the camera!")
        video_capture.release()
        cv2.destroyAllWindows()
        return  # End the function if no camera feed is found

    # Detect emotions
    result = emotion_detector.detect_emotions(frame)

#if we don't face any issues for accessing the camera then we will go ahead and capture our emotions which was captured by frame

    if result:
        dominant_emotion = max(result[0]['emotions'], key=result[0]['emotions'].get)
        print(f"Detected mood: {dominant_emotion}")

        # Create playlist based on detected emotion
        create_mood_music(dominant_emotion)
        print(f"Playlist created for mood: {dominant_emotion}")

    else:
        print("No emotions detected, try again!")

    # Display the captured frame
    cv2.imshow("Emotions Detected", frame)
    cv2.waitKey(1000)  # Show the frame for 1 second

    # Release resources
    video_capture.release()
    cv2.destroyAllWindows()

# Run the function
detect_and_create_playlist()