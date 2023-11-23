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

VIDEO_FILE_PATH = file_path
AUDIO_FILE_PATH = VIDEO_FILE_PATH.replace("mp4", "mp3")

print(VIDEO_FILE_PATH)
print(AUDIO_FILE_PATH)

MP4ToMP3(VIDEO_FILE_PATH, AUDIO_FILE_PATH)

if os.path.exists(AUDIO_FILE_PATH):
  os.remove(VIDEO_FILE_PATH)
  print("Video file deleted successfully")
else:
  print("The audio file does not exist")