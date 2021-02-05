from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit, QPushButton
import boto3, sys, os

s3 = boto3.session.Session(profile_name='s3').resource('s3')

def upload_file(path, aws_path=None):
	data = open(path, 'rb')
	if aws_path: path = aws_path
	s3.Bucket('s3-bucket-cs493').put_object(Key=path, Body=data)

def upload_directory(dir_path, aws_path=None):
	for path, dirs, files in os.walk(dir_path):
		for file in files:
			if aws_path:
				upload_file(path+"/"+file, aws_path)
			else:
				upload_file(path+"/"+file)

def song_listener():
	if aws_path.text():
		upload_file(song_file_name.text(), aws_path.text())
	else:
		upload_file(song_file_name.text())

def album_listener():
	print("Uploading album")
	if aws_path.text():
		upload_directory(album_dir_name.text(), aws_path.text())
	else:
		upload_directory(album_dir_name.text())

def artist_listener():
	print("Uploading artist")
	if aws_path.text():
		upload_directory(artist_dir_name.text(), aws_path.text())
	else:
		print("Calling upload_dir")
		upload_directory(artist_dir_name.text())

app = QApplication([])

window = QWidget()
window.setWindowTitle("AWS_SDK_DESKTOP_APP")
layout = QFormLayout()
song_file_name = QLineEdit()
artist_dir_name = QLineEdit()
album_dir_name = QLineEdit()
aws_path = QLineEdit()

song_btn = QPushButton("Upload")
song_btn.clicked.connect(song_listener)

album_btn = QPushButton("Upload")
album_btn.clicked.connect(album_listener)

artist_btn = QPushButton("Upload")
artist_btn.clicked.connect(artist_listener)

layout.addRow("Path to mp3:", song_file_name)
layout.addRow(song_btn)
layout.addRow("Path to Album", album_dir_name)
layout.addRow(album_btn)
layout.addRow("Path to Artist", artist_dir_name)
layout.addRow(artist_btn)
layout.addRow("AWS path(optional):", aws_path)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())

