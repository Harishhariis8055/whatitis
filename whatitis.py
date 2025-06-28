#!/usr/bin/env python3
from pathlib import Path

def list_items(target: Path):
    print(f"\nListing items in: {target}\n")
    for item in target.iterdir():
        if item.is_file():
            print(f"{item.name}  →  FILE")
        elif item.is_dir():
            print(f"{item.name}/ →  DIRECTORY")
        else:
            print(f"{item.name}  →  OTHER (link, device, etc.)")

def count_items(target: Path):
    files  = sum(1 for i in target.iterdir() if i.is_file())
    dirs   = sum(1 for i in target.iterdir() if i.is_dir())
    total  = files + dirs
    return files, dirs, total

def menu():
    print("\nWhat would you like to do?")
    print("[1] Count TOTAL files + directories")
    print("[2] Count only FILES")
    print("[3] Count only DIRECTORIES")
    print("[4] List items (file / directory)")

def main():
    # --- Ask user which path to inspect ----------------------------
    path_str = input("Enter the path to inspect (leave blank for current): ").strip()
    target   = Path(path_str) if path_str else Path(".")

    if not target.exists():
        print("❌ Path does not exist.")
        return

    while True:
        menu()
        choice = input("Select an option (1-4, or anything else to quit): ").strip()

        if choice == "1":
            files, dirs, total = count_items(target)
            print(f"\nTotal entries : {total}")
            print(f"  ├─ Files     : {files}")
            print(f"  └─ Directories: {dirs}")
        elif choice == "2":
            files, _, _ = count_items(target)
            print(f"\nFiles only: {files}")
        elif choice == "3":
            _, dirs, _ = count_items(target)
            print(f"\nDirectories only: {dirs}")
        elif choice == "4":
            list_items(target)
        else:
            print("Good-bye!")
            break

if __name__ == "__main__":
    main()
