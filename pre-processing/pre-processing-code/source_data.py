import urllib.request
import os
import boto3

def source_dataset(s3_bucket, new_s3_key):

	source_dataset_url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/'

	# Download the file from `url` and save it locally under `file_name`:
	urllib.request.urlretrieve(
		source_dataset_url + 'us-states.csv', '/tmp/' + new_filename + 'us-states.csv')

	urllib.request.urlretrieve(
		source_dataset_url + 'us-counties.csv', '/tmp/' + new_filename + 'us-counties.csv')

	#uploading new s3 dataset
	s3 = boto3.client("s3")
	folder = "/tmp"

	asset_list = []

	for filename in os.listdir(folder):
		print(filename)
		s3.upload_file('/tmp/' + filename, s3_bucket, new_s3_key + filename)

		asset_list.append({'Bucket': s3_bucket, 'Key': new_s3_key + filename})

	return asset_list