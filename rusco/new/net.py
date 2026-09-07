import configparser
import os
from pathlib import Path
import requests


my_config = configparser.ConfigParser()
this_dir = Path(__file__).parent
my_config.read(this_dir / "public.ini")
# file secret.ini must be kept private, so I edited gitignore;
my_config.read(this_dir / "secret.ini")

base_dir = this_dir.parent
first_dir = base_dir / "Climate_Network"
second_dir = base_dir / "Climate_Network_bis"
first_dir.mkdir(exist_ok=True)
second_dir.mkdir(exist_ok=True)

if os.name == "posix":
    executable = "curl"
elif os.name == "nt":
    executable = Path("C:/Windows/System32/curl.exe")
else:
    print("operating system not supported")

proto = "https://"
domain = my_config["DEFAULT"]["datamet_domain"]
suff_01 = my_config["DEFAULT"]["suff_01"]
url_01 = f"'{proto}{domain}{suff_01}'"
suff_02 = my_config["DEFAULT"]["suff_02"]
url_02 = f"'{proto}{domain}{suff_02}'"

service_key = my_config["DEFAULT"]["service_key"]

for element in first_dir.glob("**/*MainDataSet*.dat"):
    #element_string = str(element)
    #my_files = f"-F file=@{element_string};type=CRBasicEditor/x-CSI.DAT"
    my_files = {
        # 'file': ('sample009.dat', open(element, 'rb'), 'CRBasicEditor/x-CSI.DAT')
        'file': ('sample009.dat', open(element, 'rb'))
    }

    my_headers = {
        'accept': 'application/json',
        'Authorization': f"Bearer {service_key}",
        'Content-Type': 'multipart/form-data',
        }
    r = requests.request(
        method='POST',
        url=url_01,
        headers=my_headers,
        files=my_files
        )

# for element in first_dir.glob("*Dia*.dat"):
#     element_string = str(element)
#     my_file = f"-F file=@{element_string};type=CRBasicEditor/x-CSI.DAT"
#     cmd = f"{executable} {method} {url_02} {accept} {auth} {content_tp} {my_file}"
#     ret_code = os.system(cmd)
#     print(ret_code)
#     if ret_code:
#         print("error")
#     else:
#         element.move_into(second_dir)
#     print(ret_code)

