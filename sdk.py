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
				upload_file(path+"/"+file, aws_path+"/"+path+"/"+file)
			else:
				upload_file(path+"/"+file)

if __name__ == "__main__":
	if len(sys.argv) > 2:
		if not os.path.isdir(sys.argv[1]):
			upload_file(sys.argv[1], sys.argv[2])
		else:
			upload_directory(sys.argv[1], sys.argv[2])
	else:
		if not os.path.isdir(sys.argv[1]):
			upload_file(sys.argv[1])
		else:
			upload_directory(sys.argv[1])
