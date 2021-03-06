import boto3, sys, os, json

s3 = boto3.session.Session(profile_name='s3').resource('s3')
client = boto3.client('dynamodb')

def upload_file(path, aws_path=None):
	data = open(path, 'rb')
	if aws_path: path = aws_path
	s3.Bucket('s3-bucket-cs493').put_object(Key=path, Body=data)

def upload_directory(dir_path, aws_path=None):
	for path, dirs, files in os.walk(dir_path):
		for file in files:
			if aws_path:
				upload_file(path+"/"+file, aws_path+"/"+path+"/"+file)
			else:
				upload_file(path+"/"+file)

def walk(folder):
	if len(folder.split("/")) == 1:
		artist = folder
	else:
		artist = folder.split("/")[-1]

	albums = {}
	for path, dirs, files in os.walk(folder):
		for album in dirs:
			albums[album] = []
		for song in files:
			albums[path.split("/")[-1]].append([song, path+"/"+song])

	return artist, albums

def upload_to_ddb(upload_obj):
	client.batch_write_item(
		RequestItems={'music': upload_obj},
	)

def create_ddb_upload_object(genre, artist, albums):
	upload_obj = [
		{
			'PutRequest': {
				'Item': {
					"pk": {"S": "genre"},
					"sk": {"S": genre},
					"type": {"S": "genre"},
					"name": {"S": genre},
				},
			},
		},
		{
			'PutRequest': {
				'Item': {
					"pk": {"S": "genre#"+genre},
					"sk": {"S": "artist#"+artist},
					"type": {"S": "artist"},
					"name": {"S": artist},
				}
			},
		}
	]
	for album in albums:
		upload_obj.append({
			'PutRequest': {
				'Item': {
					"pk": {"S": "artist#"+artist},
					"sk": {"S": "album#"+album},
					"type": {"S": "album"},
					"name": {"S": album},
				},
			},
		})
		for song, song_path in albums[album]:
			upload_obj.append({
				"PutRequest": {
					"Item": {
						"pk": {"S": "song"},
						"sk": {"S": song},
						"type": {"S": "song"},
						"name": {"S": song},
						"s3_key": {"S": song_path},
					},
				},
			})
			upload_obj.append({
				"PutRequest": {
					"Item": {
						"pk": {"S": "album#"+album},
						"sk": {"S": "song#"+song},
						"type": {"S": "song"},
						"name": {"S": song},
						"s3_key": {"S": song_path},
					},
				},
			})
	return upload_obj

if __name__ == "__main__":
	answer = input("Would you like to upload to DynamoDB also? (Y | N): ") 
	if answer == "Y":
		genre = input("Great, let's start with the genre. Please enter the genre: ")
		artist_folder = input("Thanks, and what is the path to the artist? (Please make sure songs are contained within the proper album folder, and each album folder is contained within the proper artist folder: ")
		artist, albums = walk(artist_folder)
		upload_to_ddb(create_ddb_upload_object(genre, artist, albums))
		print("Uploaded to DynamoDB successfully!")

	aws_path = input("If you have a specific aws_path you'd like to use, enter it now. (If not, press enter): ")
	uploadee_path = input("Cool, and what is the path to what you want to upload?: ")
	if aws_path:
		if os.path.isdir(uploadee_path):
			upload_directory(uploadee_path, aws_path)
			print("Uploaded to s3 successfully!")
		else:
			upload_file(uploadee_path, aws_path)
			print("Uploaded to s3 successfully!")
	else:
		if os.path.isdir(uploadee_path):
			upload_directory(uploadee_path)
			print("Uploaded to s3 successfully!")
		else:
	 		upload_file(uploadee_path)
	 		print("Uploaded to s3 successfully!")
