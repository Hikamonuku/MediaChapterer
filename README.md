# MediaChapterer

MediaChapterer is a simple Python tool for adding chapters to video files using FFmpeg.

The program allows the user to select a video file directly or choose a video from a folder, define chapter timestamps and titles, and generate a new MKV file containing the embedded chapters.

The original video is preserved.

## Features

- Select a video file directly
- Select a folder and choose a video from an enumerated list
- Supports MP4, MKV, AVI, MOV, WebM and M4V
- Flexible timestamp input
- Automatically sorts chapters by timestamp
- Reads the video duration using ffprobe
- Automatically calculates chapter end times
- Generates FFmetadata
- Embeds chapters using FFmpeg
- Uses stream copy (`-c copy`), avoiding re-encoding
- Preserves the original video

## Requirements

- Python 3
- FFmpeg
- ffprobe

FFmpeg and ffprobe must be available in the system PATH.

## Usage

Run:

```bash
python main.py