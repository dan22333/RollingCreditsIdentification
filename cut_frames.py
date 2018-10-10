import cv2 as cv
import os
import threading
import time


def main():
  video_count = 1
  frame_rate = 200
  frames_start=8000
  number_of_frames_per_movie = 80
  videos_folder = "C:/Users/t-danur/Desktop/geners"
  videos_genres = os.listdir(videos_folder)
  frames_output_folder = videos_folder + "/MovieFrames"
  if not os.path.exists(frames_output_folder):
    os.mkdir(frames_output_folder)
  for genre in videos_genres:
    genre_path = videos_folder+"/"+genre
    genre_videos = os.listdir(genre_path)
    for video in genre_videos:
      threading.Thread(target=extract_video, args=(genre_path,video,frames_start,frame_rate,frames_output_folder, number_of_frames_per_movie,)).start()





def extract_video(genre_path, video,frames_start,frame_rate,frames_output_folder, number_of_frames_per_movie):
  video_file_name = genre_path + "/" + video
  cap = cv.VideoCapture(video_file_name)
  success, frame = cap.read()
  count = 1
  frame_written = 1
  while success:
    if count > frames_start:
      break
    success, frame = cap.read()
    count += 1

  while success:
    if count % frame_rate == 0:
      cv.imwrite(frames_output_folder + "/" + video + "_%d.jpg" % (frame_written), frame)
      frame_written += 1
      # Display the resulting frame
      # cv.imshow('Frame', frame)
    if cv.waitKey(25) & 0xFF == ord('q'):
      break
    count += 1
    if frame_written == (number_of_frames_per_movie + 1):
      break
    success, frame = cap.read()

  # When everything done, release the video capture object
  cap.release()


if __name__ == "__main__":
  main()