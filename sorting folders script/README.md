# Sorting folder script

Many people have a folder on their desktop, which is called something like `"Disassemble"`. As a rule, you never get around to disassembling this folder.

This script will help you to disassemble this folder. You can customize this program for yourself and, it will execute an individual script that meets your needs. To do this, the application will check the file extension (the last characters in the file name, usually after a dot) and, depending on the extension, decide which category to assign this file to.

The script takes one argument at startup - the name of the folder in which it will sort. The file with the program is called `main.py`, then to sort the `/user/Desktop/Junk` folder, you need to run the script with the command `python main.py /user/Desktop/Junk`.

The logic for processing the folder is placed in a separate function. 
The script goes to any nesting depth, the folder processing function recursively calls itself when it encounters folder nesting.
The script goes through the folder specified during the call and sorts all files into groups:
- images ('JPEG', 'PNG', 'JPG', 'SVG');
- video files ('AVI', 'MP4', 'MOV', 'MKV');
- documents ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX');
- music ('MP3', 'OGG', 'WAV', 'AMR');
- archives ('ZIP', 'GZ', 'TAR');
- others (unknown extensions).

The normalize function:

- takes a string as input and returns a string, 
- translates Cyrillic characters to Latin,
- replaces all characters except Latin letters and numbers with '_',
- capital letters remain capital and small letters remain small after transliteration.

Processing result:
- images are transferred to the `images` folder,
- documents are transferred to the `documents` folder,
- audio files are moved to `audio`,
- video files are moved to `video`,
- archives are unpacked and their contents are moved to the `archives` folder in a subfolder named the same as the archive, but without the extension at the end,
- all files and folders are renamed using the `normalize.py` file,
- file extensions are not changed after renaming,
- empty folders are deleted,
- the script ignores the archives, video, audio, documents, images folders,
- files with unknown extensions remain unchanged.