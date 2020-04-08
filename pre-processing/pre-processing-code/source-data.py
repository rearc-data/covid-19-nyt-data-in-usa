
import os
import pandas as pd
import boto3

source_dataset_url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/"

def source_dataset(s3_bucket, new_s3_key):
	us_states = pd.read_csv(
		source_dataset_url + "us-states.csv", header=0, index_col=None)
	us_states.to_csv("/tmp/us-states.csv", index=False)

	us_counties = pd.read_csv(
		source_dataset_url + "us-counties.csv", header=0, index_col=None)
	us_counties.to_csv("/tmp/us-counties.csv", index=False)

	#uploading new s3 dataset
	s3 = boto3.client("s3")
	folder = "/tmp"

	for filename in os.listdir(folder):
        print(filename)
        s3.upload_file("/tmp/" + filename, s3_bucket, new_s3_key + filename)