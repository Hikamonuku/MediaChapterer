def main_menu():
    chapters = []
    while True:
        time = input("Chapter Start (HH:MM:SS): ")
        title = input("Chapter Title: ")
        chapter = {
            "time": time,
            "title": title
        }
        chapters.append(chapter)
        another = input("Add another chapter? [Y/N]: ").lower()
        if another != "y":
            break
    print("\n=== CHAPTERS ===")
    for chapter in chapters:
        print(f"{chapter['time']} - {chapter['title']}")

if __name__ == "__main__":
    main_menu()