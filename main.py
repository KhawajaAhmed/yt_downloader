from pytube import YouTube
import os
import subprocess

def get_file_path():
    print("\nEnter filepath where you want video to be downloaded:")
    file_path = input().strip()

    if not os.path.exists(file_path):
        os.makedirs(file_path)
        print("Directory provided not found. New directory made in the current directory!")

    return file_path

def download_video(yt, file_path):
    video_stream = yt.streams.filter(only_video=True).order_by('resolution').desc().first()
    return video_stream.download(file_path, filename=f'{yt.title}_video')

def download_audio(yt, file_path):
    audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
    return audio_stream.download(file_path, filename=f'{yt.title}_audio')

def combine_audio_video(video_path, audio_path, final_video_path):
    subprocess.run(['ffmpeg', '-i', video_path, '-i', audio_path, '-c:v', 'copy', '-c:a', 'aac', final_video_path])

def main():
    video_link = input("Enter the YouTube video link: ")
    yt = YouTube(video_link)

    print(f"Title of the video: {yt.title}\nThe total views for this video are: {yt.views}")

    file_path = get_file_path()

    video_path = download_video(yt, file_path)
    audio_path = download_audio(yt, file_path)

    final_video_path = os.path.join(file_path, f'{yt.title}.mp4')

    combine_audio_video(video_path, audio_path, final_video_path)

    os.remove(video_path)
    os.remove(audio_path)

    print("Video downloaded successfully!")

if __name__ == "__main__":
    main()
