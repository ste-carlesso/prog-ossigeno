# take DAT (TOA5) files (MainDataSet and Dia) from first directory 
# upload them to DatametV2 DEV using Rest API 
# and, if successful, move them to second directory

##curl -X 'POST' \
##  'https://fomdatamet.it/api/v1/load-jobs' \
##  -H 'accept: application/json' \
##  -H 'Authorization: Bearer sk_4cca1c468e392d7603dc9adb8177abb58e443e21dd47b422' \
##  -H 'Content-Type: multipart/form-data' \
##  -F 'file=@FAENZA_MainDataSet_2026_09_06_0450.dat'
##
from pathlib import Path
import configparser
import requests
from requests_toolbelt import MultipartEncoder

base_dir = Path('D:/')
first_dir = base_dir / "Climate_Network"
second_dir = base_dir / "Climate_Network_bis"

config = configparser.ConfigParser()
config.read('the_secret.ini')
token = config.get("api", "token")

# v2-PROD URL
base_url = "https://fomdatamet.it"
endpoint1 = base_url + "/api/v1/load-jobs"
endpoint2 = base_url + "/api/v1/battery-samples"

my_headers = {
    'accept': 'application/json',
    'Authorization': f"Bearer {token}",
    'Content-Type': 'multipart/form-data'
    }

for element in first_dir.glob("*MainDataSet*.dat"):
    my_data = MultipartEncoder(
        fields={'field0': ('filename', open(element, 'rb'), 'text/plain' )})

    response = requests.post(
        url=endpoint1,
        headers=my_headers,
        data=my_data
    )

    print(response.json())
  
        
