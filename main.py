# Youtube Video Downloader- Khawaja Hussain Ahmed

from pytube import YouTube
from sys import argv
import subprocess
import os

file_path = ""
video_link = argv[1]
yt = YouTube(video_link)

def get_filePath():
    print("\nEnter filepath where you want video to be downloaded:")
    file_path = input().strip()

    if not os.path.exists(file_path):
        os.makedirs(file_path)
        print("Directory provided not found. New directory made in the current directory!")

    return file_path

def download_video(yt,file_path):
    video_stream = yt.streams.filter(only_video=True).order_by('resolution').desc().first()

    return ( video_stream.download(file_path,filename=f'{yt.title}video') ) 

def download_audio(yt,file_path):
    audio_stream = yt.streams.filter(only_audio="True").order_by('abr').desc().first()
    
    return ( audio_stream.download(file_path,filename=f'{yt.title}+audio') )

print(f"Title of the video: {yt.title}\nThe total views for this video are: {yt.views}")

file_path = get_filePath()

video_path = download_video(yt,file_path)
audio_path = download_audio(yt,file_path)

final_video_path = os.path.join(file_path, 'final_video.mp4')

subprocess.run(['ffmpeg', '-i', video_path, '-i', audio_path , '-c:v', 'copy', '-c:a', 'aac', final_video_path])

os.remove(video_path)
os.remove(audio_path)

print("Video downloaded successfully!")