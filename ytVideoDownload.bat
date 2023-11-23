@echo off

cd "C:\Users\Anton\source\repos\Test"
set "curDir=%cd%"
echo %curDir%

python youtubeVideoDownload.py "%*"