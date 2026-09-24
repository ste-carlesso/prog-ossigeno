## take DAT (TOA5) files (MainDataSet and Dia) from first directory, upload them to DatametV2 DEV 
## using Rest API, and move them to second directory

## curl -X 'POST' \
##  'https://fomdatamet.it/api/v1/load-jobs' \
##  -H 'accept: application/json' \
##  -H 'Authorization: Bearer sk_XXXXXXXXXXXXXXXXXXXXXXXXXXX' \
##  -H 'Content-Type: multipart/form-data' \
##  -F 'file=@FAENZA_MainDataSet_2026_09_06_0450.dat'

## contains code from https://curlconverter.com/python/

from pathlib import Path
import requests
import tomllib
from datetime import datetime as dt

def time_string():
    return dt.strftime(dt.now(), '%Y-%m-%d_%H:%M:%S')


with open('secret.toml', 'rb') as secret:
    config = tomllib.load(secret)

base_dir = Path('D:/')
token = config['api']['token']
base_url = "https://fomdatamet.it"
first_dir = base_dir / "Climate_Network"
second_dir = base_dir / "Climate_Network_bis"

# requests won't add a boundary when you pass files
# if this header is set:  'Content-Type': 'multipart/form-data'
headers = {
    'accept': 'application/json',
    'Authorization': f"Bearer {token}",
}

endpoint = base_url + "/api/v1/load-jobs"

for dat_file in first_dir.glob("*MainDataSet*.dat"):
    with open(dat_file, 'rb') as file_object:
        files = {'file': file_object,}
        response = requests.post(endpoint, headers=headers, files=files)
        print([time_string(), response.json()], sep='\t')
    if response.json()['success']:
        try:
            dat_file.move_into(second_dir)
        except:
            print([time_string(), "can't move file to dest"], sep='\t')


endpoint = base_url + "/api/v1/battery-samples"
 
for dat_file in first_dir.glob("*Dia*.dat"):
    with open(dat_file, 'rb') as file_object:
        files = {'file': file_object,}
        response = requests.post(endpoint, headers=headers, files=files)
        print([time_string(), response.json()], sep='\t')

    if response.json()['status'] == 'success':
        try:
            dat_file.move_into(second_dir)
        except:
            print([time_string(), "can't move file to dest"], sep='\t')

