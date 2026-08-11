def time_to_ms(time):
    parts = time.split(":")
    total_seconds = 0
    multiplier = 1
    for part in reversed(parts):
        total_seconds += int(part) * multiplier
        multiplier *= 60
    return total_seconds * 1000

def main_menu():
    chapters = collect_chapters()
    print("\n=== CHAPTERS ===")
    for chapter in chapters:
        print(
            f"{chapter['time']} - {chapter['title']} "
            f"({chapter['time_ms']} ms)"
        )

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

def select_video():
    video_path = input("Video file: ").strip().strip('"')
    return video_path

if __name__ == "__main__":
    main_menu()