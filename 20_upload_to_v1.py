# take DAT (TOA5) files MainDataSet*.dat  from second directory 
# upload them to DatametV1 and, if successful, move them to third directory
# take Dia*.dat from second dir and simply move then to third dir


## curl -v -F file=@ANCONA_MainDataSet_2020_09_01_0340.dat http://192.168.1.90:9000/load-jobs

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
third_dir = base_dir / "Climate_Network_ter"

endpoint3 = 'http://46.137.162.248/load-jobs'


for dat_file in second_dir.glob("*MainDataSet*.dat"):
    files = {'file': open(dat_file, 'rb'),}
    response = requests.post(endpoint3, files=files)
    print(response.text)
    ## grammatical error but correct string
    # if response.text == '{ succcess: true }':
        # dat_file.move_into(third_dir)

# for dat_file in second_dir.glob("*Dia*.dat"):
    # dat_file.move_into(third_dir)
    
