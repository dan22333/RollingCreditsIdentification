import os
import cv2 as cv
videos = os.listdir(r"C:\Users\t-danur\Downloads\videos")
video_count = 1
for video in videos:
  cap = cv.VideoCapture("C:\\Users\\t-danur\Downloads\\videos\\" + video)
  success, frame = cap.read()
  count = 0
  while success:
    # if count%2==0:
    cv.imshow('Frame', frame)
    if cv.waitKey(25) & 0xFF == ord('q'):
      break
    count += 1
    success, frame = cap.read()
  video_count +=1

  # When everything done, release the video capture object
  cap.release()

  # Closes all the frames
  cv.destroyAllWindows()