# S3 SDK with Python

A python tool to upload songs, artists, and albums to AWS s3.
## Python CLI

Upload songs, artists, and albums to a bucket from the command line.
Use the package manager pip to install PyQt5, and Boto3. (Must be on python 3 or higher)

```bash
pip install boto3
```

### Usage
The CLI takes 2 arguments. The first is the path to a song, album, or artist. The second, which is optional, is the path on was you wish for it to be stored. (Can also be used to rename) Default is root of bucket.   
From command line, run:
```
python3 sdk.py path/to/song.mp3
python3 sdk.py path/to/album
python3 sdk.py path/to/artist
```
-OR-
```
python3 sdk.py path/to/song.mp3 path/in/aws
python3 sdk.py path/to/album path/in/aws
python3 sdk.py path/to/artist path/in/aws
```

## Python Desktop Application

Upload songs, artists, and albums to a bucket using the more user friendly desktop app. Use the package manager pip to install pyqt5 and boto3. (Must be one python 3 or higher)

```bash
pip install pyqt5
pip install boto3
```

### Usage

The Desktop app is more self explanatory. From command line run:
```
python3 ui.py
```
From here you will see a desktop app pop up. Make sure to enter the path names relative to wherever you ran the app with `python3 ui.py`