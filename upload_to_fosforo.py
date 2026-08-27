
"""
2011-2016 @author Simone Stucchi <simone.stucchi@gmail.com>
2020-2022 @author Stefano Carlesso <s.carlesso@fondazioneomd.it>
Code was translated from Ruby to Python
----
requirements 
* Windows 10
* Python 3.9
* curl 
* Manually make directories: first_dir, second_dir, third_dir, fourth_dir

"""

import logging
import subprocess
import fnmatch
import re
import os
from pathlib import Path, PurePosixPath
from datetime import date
import shutil


first_dir = Path("D:/") / "Climate_Network"
second_dir = Path("D:/") / "Climate_Network_bis"
third_dir = Path("D:/") / "Climate_Network_ter"
fourth_dir = Path("D:/") / "Climate_Network_x"
log_dir = Path("D:/logs")

logging.basicConfig(
    filename= log_dir / ( str(date.today().isoformat()) + "_to_p.log" ),
    format='[%(asctime)s] %(levelname)-8s %(message)s',
    level=logging.DEBUG,
)


curl_path = Path("C:/Windows/System32/curl.exe")
scp_path = Path("C:/Windows/System32/OpenSSH/scp.exe")
sftp_path = Path("C:/Windows/System32/OpenSSH/sftp.exe")
ssh_path = Path("C:/Windows/System32/OpenSSH/ssh.exe")


month_name_dict = {
    "01": "gennaio", "02": "febbraio", "03": "marzo", "04": "aprile",
    "05": "maggio", "06": "giugno", "07": "luglio", "08": "agosto",
    "09": "settembre", "10": "ottobre", "11": "novembre", "12": "dicembre"
}

fosforo = {
    #"address": "15.161.209.22", # on the internet
    "address": "10.8.0.1", # on openVPN lan 
    "user": "fondazione",
    # "private_key" : Path("C:/msys/home/Fondazione/.ssh/id_rsa"),
    "private_key": Path("C:/Users/home/Fondazione/.ssh/id_rsa"),
    "dest_stazioni": PurePosixPath("/srv/samba/stazioni_gestite2"),
}


    

def to_fosforo():
    '''Take any Dat (Main abd Dia) from 2nd dir, upload to FOSFORO, 
    if successful move to 4th dir
    Requires keys setup and ssh config in C:/Users/$USER/.ssh/config
    '''
    for src_path in third_dir.glob("*.dat"):
        file_name = str(src_path.name)
        if fnmatch.fnmatch(file_name, "*MainDataSet*"):
            type_str = "_MainDataSet_"
        elif fnmatch.fnmatch(file_name, "*Dia*"):
            type_str = "_Dia_"
        first_split = re.split(type_str, file_name)
        pass
        second_split = re.split("[_.]", first_split[1])
        
        station_name = first_split[0]
        year = second_split[0]
        month_name = month_name_dict[second_split[1]]
        user = fosforo["user"]
        host = fosforo["address"]
        destination_dir = fosforo["dest_stazioni"].joinpath(
            station_name, year, month_name)

        # create dirs if needed with ssh 
        # -p create parents if needed, no error if existing
        cmd = F"{ssh_path} {user}@{host} mkdir -p {destination_dir}"
        my_process = subprocess.run(cmd, capture_output=True)
        returncode = my_process.returncode
        stderr = my_process.stderr
        if returncode != 0:
            logging.warning(F"{returncode} {stderr}")
        else:
            logging.info(F"{returncode} {stderr}")        

        # upload single file with scp. Option `-p` to preserves modification 
        # times, access times, and modes from the original file.
        cmd = F"{scp_path} -p {src_path} {user}@{host}:{destination_dir}"
        my_process = subprocess.run(cmd, capture_output=True)
        returncode = my_process.returncode
        stderr = my_process.stderr
        if returncode != 0:
            logging.warning(F"{returncode} {stderr}")
        else:
            logging.info(F"{returncode} {stderr}")
            try:
                destination = fourth_dir / file_name
                # copy the file preserving some metadata
                shutil.copy2(src=src_path, dst=destination)
            except:
                logging.warning(F"exception while trying to copy {file_name}")
            else:
                logging.info(
                    F"Either file was copied or was present in destination")
                try:
                    # delete original file
                    os.remove(src_path)
                except FileNotFoundError:
                    logging.info("Non fatal FileNotFoundError")
                    pass
                except:
                    pass
                else:
                    logging.info(F"remove original")
            finally:
                # executed in any case
                pass



# All magic here
to_fosforo()
