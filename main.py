import shutil
import subprocess
from pathlib import Path

VIDEO_EXTENSIONS = {
    ".mp4",
    ".mkv",
    ".avi",
    ".mov",
    ".webm",
    ".m4v"
}

def check_ffmpeg():
    ffmpeg = shutil.which("ffmpeg")
    ffprobe = shutil.which("ffprobe")
    if ffmpeg is None:
        print("FFmpeg not found.")
    if ffprobe is None:
        print("ffprobe not found.")
    if ffmpeg is None or ffprobe is None:
        print("Install FFmpeg and make sure it is available in PATH.")
        return False
    return True

def time_to_ms(time):
    parts = time.split(":")
    total_seconds = 0
    multiplier = 1
    for part in reversed(parts):
        total_seconds += int(part) * multiplier
        multiplier *= 60
    return total_seconds * 1000

def select_video():
    while True:
        user_input = input("Video file or folder: ").strip().strip('"')
        path = Path(user_input)
        if path.is_file():
            if path.suffix.lower() in VIDEO_EXTENSIONS:
                return str(path)
            print("Unsupported video format.")
            continue
        if path.is_dir():
            videos = [
                file
                for file in path.iterdir()
                if file.is_file()
                and file.suffix.lower() in VIDEO_EXTENSIONS
            ]
            if not videos:
                print("No compatible video files found in this folder.")
                continue
            videos.sort(key=lambda video: video.name.lower())
            print("\n=== VIDEOS FOUND ===")
            for index, video in enumerate(videos, start=1):
                print(f"{index}. {video.name}")
            while True:
                choice = input("Select video: ").strip()
                if choice.isdigit():
                    choice = int(choice)
                    if 1 <= choice <= len(videos):
                        return str(videos[choice - 1])
                print("Invalid option.")
        else:
            print("File or folder not found. Try again.")

def collect_chapters():
    chapters = []
    while True:
        entry = input("Chapter (HH:MM:SS - Title): ").strip()
        if " - " in entry:
            time, title = entry.split(" - ", 1)
        else:
            time = entry
            title = input("Chapter Title: ").strip()
        chapter = {
            "time": time.strip(),
            "time_ms": time_to_ms(time.strip()),
            "title": title.strip()
        }
        chapters.append(chapter)
        another = input("Add another chapter? [Y/N]: ").lower()
        if another != "y":
            break
    chapters.sort(key=lambda chapter: chapter["time_ms"])
    return chapters

def get_video_duration(video_path):
    result = subprocess.run(
        [
            "ffprobe",
            "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            video_path
        ],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        print("Could not read video duration.")
        print(result.stderr)
        return None
    duration_seconds = float(result.stdout.strip())
    return int(duration_seconds * 1000)

def main_menu():
    if not check_ffmpeg():
        return
    video_path = select_video()
    chapters = collect_chapters()
    duration_ms = get_video_duration(video_path)
    if duration_ms is None:
        return
    print(f"\nVideo: {video_path}")
    print(f"Duration: {duration_ms} ms")

if __name__ == "__main__":
    main_menu()