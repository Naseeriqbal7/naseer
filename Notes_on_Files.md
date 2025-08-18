# WORKING WITH FILES

##### Two types of files
1. Text
    - Contains one or more lines that contain text characters.
    - In a text file, each line end with a newline character `\n`.
    - On Windows, the newline character is sometimes preceded by a carriage return `\r`: `\r\n`.
    - Common Types:
        - .txt files
        - .csv files
        - .json files
        - .xml files
        - .html files
        - .md files
2. Binary
    - Any file that isn't a text file.
    - Many binary file formats contain parts that can be interperted as text.
    - However, binary files typically contain a sequence of bytes that are intended to be interpreted as something other than text characters.
    - Common types:
        - Compiles program files
        - Image files
        - audio files
        - video files
        - database files
        - compressed files

##### Sequence of file operations
1. Open the file: open()
2. Write data to a file or read data from a file: write(), read(), readlines(), or readline()
3. Close the file: close()


##### Opening a file
- When we open a file we create a file object.
- Then, we can use the methods of the file object to work with the file.

##### The built-in open() function
```
open(file_name, mode)
```
- Returns a file object for the specified file with the specified mode.

###### Modes of the open() function
1. r - Read
    - If the file doesn't exist, this mode causes a file not found error.
2. w - Write
    - If the file doesn't exist, this mode creates a new file.
    - If the file exists, this mode overwrites the existing file.
3. a - Append
    - If the file doesn't exist, this mode creates a new file.
    - If the file exists, this mode appends to the existing file.
4. b - Binary
    - Use for binary files along with "r" or "w" mode.
