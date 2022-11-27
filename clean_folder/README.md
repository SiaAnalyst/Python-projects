### Script to sort files in a folder

The script goes through the folder specified during the call and sorts all files into groups:

- images ('JPEG', 'PNG', 'JPG', 'SVG');
- video files ('AVI', 'MP4', 'MOV', 'MKV');
- documents ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX');
- music ('MP3', 'OGG', 'WAV', 'AMR');
- archives ('ZIP', 'GZ', 'TAR');
- other: unknown extensions.

### Setup

- The package is installed into the system by the command `pip install -e`. (or `python setup.py install`, requires administrator rights).
- After installation, the clean_folder package appears in the system.
- When the package is installed in the system, the script can be called anywhere from the console with the command clean-folder