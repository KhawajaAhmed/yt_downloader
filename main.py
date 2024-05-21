# Youtube Video Downloader- Khawaja Hussain Ahmed

from pytube import YouTube
from sys import argv
import subprocess

video_link = argv[1]

yt = YouTube(video_link)

print(f"Title of the video: {yt.title}\nThe total views for this video are: {yt.views}")

video_stream = yt.streams.filter(res="2160p").first()
print(video_stream)
video_file = video_stream.download(filename=yt.title+'video') 

audio_stream = yt.streams.filter(only_audio="True").order_by('abr').desc().first()
print(audio_stream)
audio_file = audio_stream.download(filename=yt.title+'audio')

subprocess.run(['ffmpeg', '-i', f'{yt.title}video', '-i', f'{yt.title}audio', '-c:v', 'copy', '-c:a', 'aac', 'final_video.mp4'])