import os
import boto3
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from multiprocessing.dummy import Pool
import time
from s3_md5_compare import md5_compare


def download_data(url):
    response = None
    retries = 5
    for attempt in range(retries):
        try:
            response = urlopen(url)
        except HTTPError as e:
            if attempt == retries:
                raise Exception('HTTPError: ', e.code)
            time.sleep(0.2 * attempt)
        except URLError as e:
            if attempt == retries:
                raise Exception('URLError: ', e.reason)
            time.sleep(0.2 * attempt)
        else:
            break

    if response is None:
        raise Exception('There was an issue downloading the dataset')
    else:
        return response


def data_to_s3(endpoint):

    # throws error occured if there was a problem accessing data
    # otherwise downloads and uploads to s3

    source_dataset = download_data(
        'https://raw.githubusercontent.com/nytimes/covid-19-data/master/' + endpoint)

    filename = endpoint.replace('/', '_')
    file_location = '/tmp/' + filename

    with open(file_location, 'wb') as f:
        f.write(source_dataset.read())

    return True

    # # variables/resources used to upload to s3
    # s3_bucket = os.environ['S3_BUCKET']
    # data_set_name = os.environ['DATA_SET_NAME']
    # new_s3_key = data_set_name + '/dataset/'
    # s3 = boto3.client('s3')

    # s3.upload_file(file_location, s3_bucket, new_s3_key + filename)

    # print('Uploaded: ' + filename)

    # # deletes to preserve limited space in aws lamdba
    # os.remove(file_location)

    # # dicts to be used to add assets to the dataset revision
    # return {'Bucket': s3_bucket, 'Key': new_s3_key + filename}


def source_dataset(s3_bucket, new_s3_key):

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
        p.map(data_to_s3, endpoints)

    # uploading to s3
    s3_uploads = []
    s3 = boto3.client('s3')

    for filename in os.listdir('/tmp'):
        file_location = '/tmp/' + filename
        has_changes = md5_compare(
            s3, s3_bucket, new_s3_key + filename, file_location)
        if has_changes:
            s3.upload_file(file_location, s3_bucket, new_s3_key + filename)
            print('Uploaded: ' + filename)
        else:
            print('No changes in: ' + filename)

        asset_source = {'Bucket': s3_bucket, 'Key': new_s3_key + filename}
        s3_uploads.append({'has_changes': has_changes,
                           'asset_source': asset_source})

    count_updated_data = sum(
        upload['has_changes'] == True for upload in s3_uploads)
    asset_list = []
    if count_updated_data > 0:
        asset_list = list(
            map(lambda upload: upload['asset_source'], s3_uploads))
        if len(asset_list) == 0:
            raise Exception('Something went wrong when uploading files to s3')

    return asset_list
