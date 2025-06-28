# whatitis

A simple and intuitive Python command-line tool for exploring file system directories. Count files, directories, and list items with an easy-to-use interactive menu.

## Features

- **Count total items**: Get the total number of files and directories
- **Count files only**: See how many files are in a directory
- **Count directories only**: See how many subdirectories exist
- **List items**: View all items with their types (file, directory, or other)
- **Interactive menu**: Easy-to-use command-line interface
- **Path validation**: Handles invalid paths gracefully
- **Current directory support**: Works with the current directory by default

## Installation

### Prerequisites
- Python 3.6 or higher

### Download
```bash
git clone https://github.com/Harishhariis8055/whatitis.git
cd whatitis
```

### Make executable (optional)
```bash
chmod +x whatitis.py
```

## Usage

### Basic Usage
```bash
python3 whatitis.py
```

### Direct execution (if made executable)
```bash
./whatitis.py
```

### Example Session
```
Enter the path to inspect (leave blank for current): /home/user/Documents

What would you like to do?
[1] Count TOTAL files + directories
[2] Count only FILES
[3] Count only DIRECTORIES
[4] List items (file / directory)
Select an option (1-4, or anything else to quit): 1

Total entries : 25
  ├─ Files     : 18
  └─ Directories: 7
```

## Menu Options

1. **Count TOTAL files + directories**: Shows a breakdown of all items in the directory
2. **Count only FILES**: Displays just the file count
3. **Count only DIRECTORIES**: Displays just the directory count
4. **List items**: Shows each item with its type (FILE, DIRECTORY, or OTHER)

## Features in Detail

### Path Input
- Leave blank to inspect the current directory
- Enter any valid path (relative or absolute)
- Invalid paths are handled with error messages

### Item Classification
- **FILE**: Regular files
- **DIRECTORY**: Subdirectories
- **OTHER**: Special items like symbolic links, device files, etc.

### Interactive Loop
The tool runs in a loop, allowing you to perform multiple operations without restarting the program. Enter any option other than 1-4 to exit.

## Examples

### Inspecting the current directory
```bash
python3 whatitis.py
# Press Enter when prompted for path
```

### Inspecting a specific directory
```bash
python3 whatitis.py
# Enter: /path/to/directory
```

### Sample output for listing items
```
Listing items in: /home/user/projects

README.md  →  FILE
src/  →  DIRECTORY
tests/  →  DIRECTORY
.gitignore  →  FILE
requirements.txt  →  FILE
docs/  →  DIRECTORY
```

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Author

Harish Created with ❤️ for simple file system exploration.

## Changelog

### v1.0.0
- Initial release
- Basic file and directory counting
- Interactive menu system
- Path validation
- Item listing with type classification
