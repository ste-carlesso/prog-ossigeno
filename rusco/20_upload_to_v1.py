# take DAT (TOA5) files MainDataSet*.dat  from second directory 
# upload them to DatametV1 and, if successful, move them to third directory
# take Dia*.dat from second dir and simply move then to third dir


## curl -v -F file=@ANCONA_MainDataSet_2020_09_01_0340.dat http://192.168.1.90:9000/load-jobs

## contains code from https://curlconverter.com/python/

from pathlib import Path
import requests
import tomllib

base_dir = Path('D:/')

# first_dir = base_dir / "Climate_Network"
second_dir = base_dir / "Climate_Network_bis"
third_dir = base_dir / "Climate_Network_ter"

endpoint = 'http://46.137.162.248/load-jobs'

for dat_file in second_dir.glob("*MainDataSet*.dat"):
    with open(dat_file, 'rb') as file_object:
        files = {'file': file_object,}
        response = requests.post(endpoint, files=files)
        print(response.text)
    ## grammatical error but correct string
    if response.text == '{ succcess: true }':
        try:
            dat_file.move_into(third_dir)
        except:
            print("can't move file to dest")


for dat_file in second_dir.glob("*Dia*.dat"):
    try:
        dat_file.move_into(third_dir)
    except:
        print("can't move file to dest")