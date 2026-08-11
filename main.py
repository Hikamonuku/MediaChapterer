def time_to_ms(time):
    parts = time.split(":")
    total_seconds = 0
    multiplier = 1
    for part in reversed(parts):
        total_seconds += int(part) * multiplier
        multiplier *= 60
    return total_seconds * 1000

def main_menu():
    chapters = []
    while True:
        time = input("Chapter Start (HH:MM:SS): ")
        title = input("Chapter Title: ")
        chapter = {
            "time": time,
            "time_ms": time_to_ms(time),
            "title": title
        }
        chapters.append(chapter)
        another = input("Add another chapter? [Y/N]: ").lower()
        if another != "y":
            break
    chapters.sort(key=lambda chapter: chapter["time_ms"])
    print("\n=== CHAPTERS ===")
    for chapter in chapters:
        print(
            f"{chapter['time']} - {chapter['title']} "
            f"({chapter['time_ms']} ms)"
        )

if __name__ == "__main__":
    main_menu()