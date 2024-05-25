# YouTube Video Downloader

This Python script allows you to download YouTube videos by providing the video link. It uses the pytube library to download the highest quality video and audio streams and then combines them into a single video file using ffmpeg.

## Installation

1. Clone or download the repository to your local machine.
2. Make sure you have Python installed on your system.
3. Install the required dependencies. For dependencies see 'dependencies'section below.

## Usage

1. Run the script.
2. Enter the YouTube video link when prompted.
3. Specify the directory where you want the video to be downloaded.
4. The script will download the video and combine the audio and video streams into a single file.
5. Once the download is complete, the final video will be saved in the specified directory.

## Dependencies

- [pytube](https://github.com/pytube/pytube): A Python library for downloading YouTube videos.
- [ffmpeg](https://ffmpeg.org/): A command-line tool for handling multimedia files.
