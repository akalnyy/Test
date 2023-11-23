from pytube import YouTube
from sys import argv

import os
from moviepy.editor import *

link = argv[1]

yt = YouTube(link)

downloadsFolder = "C:\\Users\\Anton\\Downloads"

print("Title: ", yt.title)
print("Views: ", yt.views)
print("Downloads folder: ", downloadsFolder)

ytd = yt.streams.get_audio_only()

ytd.download(downloadsFolder)

# Convert from mp4 to mp3

for file in os.listdir(downloadsFolder):
    if file.endswith(".mp4"):
        file_path = os.path.join(downloadsFolder, file)

def MP4ToMP3(mp4, mp3):
    fileToConvert = AudioFileClip(mp4)
    fileToConvert.write_audiofile(mp3)
    fileToConvert.close()

video_file_path = file_path
audio_file_path = video_file_path.replace("mp4", "mp3")

print(video_file_path)
print(audio_file_path)

MP4ToMP3(video_file_path, audio_file_path)

if os.path.exists(audio_file_path):
  os.remove(video_file_path)
  print("Video file deleted successfully")
else:
  print("The audio file does not exist")