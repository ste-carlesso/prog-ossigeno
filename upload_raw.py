"""
New task: move RAW data from here to Fosforo
"""

import os, re
import shutil
from pathlib import Path, PurePosixPath, PureWindowsPath

import datetime as dt

## THE IMPORTANT VARIABLES ##


scp_path = Path("C:\Windows\System32\OpenSSH\scp.exe")
ssh_path = Path("C:\Windows\System32\OpenSSH\ssh.exe")
month_name_dict = {
    "01":"gennaio", "02":"febbraio", "03":"marzo", "04":"aprile",
    "05":"maggio", "06":"giugno", "07":"luglio", "08":"agosto",
    "09":"settembre", "10":"ottobre", "11":"novembre", "12":"dicembre" }
fosforo = {
    "host" : "fosforo",
    #"address": "15.161.209.22", # on the internet
    "address": "10.8.0.1", # on openVPN lan 
    "user" : "fondazione",
    "private_key" : Path("C:/msys/home/Fondazione/.ssh/id_rsa"),
    "dest_stazioni" : PurePosixPath("/srv/samba/stazioni_gestite2"),
    "dest_dia" : PurePosixPath("/srv/samba/dia_temp"), 
    }

source_path = Path("D:/RAW")

yed = dt.datetime.today() - dt.timedelta(days = 1)

## THE RAW FILES LOOP ##
#D:\RAW\Citta_Studi\MILANO_CITTA_STUDI_RawData.dat
for item in ["Citta_Studi", "Roma_Termini"]:
    item_path = source_path.joinpath(Path(item))
    pattern = "*RaWData*{:d}_{:02d}_{:02d}*.dat".format(yed.year, yed.month, yed.day)
    raw_list = item_path.glob(pattern)
    #ROMA_TERMINI_RawData_2020_10_28_0413.dat
    for file_path in raw_list:
        file_name = file_path.name
        first_split = re.split(r"_RawData_", str(file_name))
        station_name = first_split[0]
        second_split = re.split(r"[_.]", first_split[1] )
        year = second_split[0]
        month = second_split[1]
        month_name = month_name_dict[month]
        user = fosforo["user"]
        ip = fosforo["address"]
        destination_path = fosforo["dest_stazioni"].joinpath(station_name, "RAW", year, month_name)
        url = F"scp://{ip}{destination_path}/"
        source = file_path
        #send_to_fosforo = F"{curl_path} -u {user}: -T {source} --ftp-create-dirs {url}"
        make_dir = F"{ssh_path} fondazione@fosforo mkdir -p {destination_path}"
        send_to_fosforo = F"{scp_path} {source} {user}@{ip}:{destination_path}"
        try:
            #print(make_dir)
            os.system(make_dir)
            os.system(send_to_fosforo)
        except:
            # maybe the file exist
            print("failed to make dir or to upload file")




