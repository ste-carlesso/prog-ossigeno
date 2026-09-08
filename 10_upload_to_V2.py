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

with open('secret.toml', 'rb') as secret:
    config = tomllib.load(secret)

base_dir = Path(config['main']['base_dir'])
token = config['api']['token']
base_url = "https://fomdatamet.it"

first_dir = base_dir / "Climate_Network"
second_dir = base_dir / "Climate_Network_bis"
endpoint1 = base_url + "/api/v1/load-jobs"
endpoint2 = base_url + "/api/v1/battery-samples"

headers = {
    'accept': 'application/json',
    'Authorization': f"Bearer {token}",
    # requests won't add a boundary if this header is set when you pass files=
    # 'Content-Type': 'multipart/form-data',
}

for dat_file in first_dir.glob("*MainDataSet*.dat"):
    files = {'file': open(dat_file, 'rb'),}
    response = requests.post(endpoint1, headers=headers, files=files)
    print(response.json())
    if response.json()['success']:
        dat_file.move_into(second_dir)

for dat_file in first_dir.glob("*Dia*.dat"):
    files = {'file': open(dat_file, 'rb'),}
    response = requests.post(endpoint2, headers=headers, files=files)
    print(response.json())
    if response.json()['status'] == 'success':
        dat_file.move_into(second_dir)
