import cv2 
from fer import FER

video_capture = cv2.VideoCapture(0) #to open the webcam
emotion_detector = FER() #using fer model for capturing emotions
#first we open the camera by cv2.VideoCapture(0) and then we capture the emotion by FER() model

ret, frame = video_capture.read() # ret = success or failure and frame = captured image 
#the read() function returns 2 values

if ret:
  result = emotion_detector.detect_emotions(frame)
  #the above line conatins dictonary , 

  if result:
    dominent_emotion = result[0]['emotions']
    print(dominent_emotion)

  cv2.imshow("Emotions are",frame)
  cv2.waitKey(0)

video_capture.release()
cv2.destroyAllWindows()



