# take DAT (TOA5) files (MainDataSet and Dia) from first directory 
# upload them to DatametV2 DEV using Rest API 
# and, if successful, move them to second directory
from pathlib import Path
import configparser
import requests

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
    #'accept': 'application/json',
    'Authorization': f"Bearer {token}",
    'Content-Type': 'multipart/form-data',
    }
print(my_headers)
for element in first_dir.glob("*MainDataSet*.dat"):
    my_files = {'file': open(element, 'rb')}
    try:
        response = requests.post(
            url=endpoint1,
            headers=my_headers,
            files=my_files
        )

        element.move(second_dir)
        print(response)
        
    except:
        print("There was an error during HTTP request")    
        
for element in first_dir.glob("*Dia*.dat"):
    my_files = {'file': open(element, 'rb')}
    try:
        response = requests.post(
            url=endpoint2,
            headers=my_headers,
            files=my_files
        )

        element.move(second_dir)
        print(response)
        
    except:
        print("There was an error during HTTP request")    
