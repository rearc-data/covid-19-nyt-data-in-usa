import os
import boto3
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from multiprocessing.dummy import Pool

def data_to_s3(endpoint):

	# throws error occured if there was a problem accessing data
	# otherwise downloads and uploads to s3

	source_dataset_url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/'

	try:
		response = urlopen(source_dataset_url + endpoint)

	except HTTPError as e:
		raise Exception('HTTPError: ', e.code, endpoint)

	except URLError as e:
		raise Exception('URLError: ', e.reason, endpoint)

	else:
		filename = endpoint.replace('/', '_')
		file_location = '/tmp/' + filename

		with open(file_location, 'wb') as f:
			f.write(response.read())

		# variables/resources used to upload to s3
		s3_bucket = os.environ['S3_BUCKET']
		data_set_name = os.environ['DATA_SET_NAME']
		new_s3_key = data_set_name + '/dataset/'
		s3 = boto3.client('s3')

		s3.upload_file(file_location, s3_bucket, new_s3_key + filename)			
		
		print('Uploaded: ' + filename)

		# deletes to preserve limited space in aws lamdba
		os.remove(file_location)

		# dicts to be used to add assets to the dataset revision
		return {'Bucket': s3_bucket, 'Key': new_s3_key + filename}

def source_dataset():

	# list of enpoints to be used to access data included with product
	endpoints = [
		'us.csv',
		'us-states.csv',
		'us-counties.csv',
		'live/us.csv',
		'live/us-states.csv',
		'live/us-counties.csv'
	]

	# multithreading speed up accessing data, making lambda run quicker
	with (Pool(6)) as p:
		asset_list = p.map(data_to_s3, endpoints)

	# asset_list is returned to be used in lamdba_handler function
	return asset_list
