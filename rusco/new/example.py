from pathlib import Path
import configparser

# import csv
from datetime import datetime as dt
from datetime import timedelta as td
from math import floor
import pyexcel as px
import requests

# variable project_root is no longer used to be compatible with cx_Freeze

output_dir = Path("output")

output_dir.mkdir(exist_ok=True, parents=True)

newline = "\n"
space = " "
underscore = "_"
dash = "-"
output_extension = ".txt"

config = configparser.ConfigParser()
# Public config, user editable
config.read("utente.ini")

## model = config.get("utente", "modello")
model = 'giornaliero' 

station_register = "Siram_giornaliero.xlsx"

# numero di osservazioni (giorni) mostrati
observations = config.get("utente", "osservazioni")
dt_to = dt.today()
dt_from = dt_to - td(days=int(observations))
# timestamp is a string; in Italian 'marca temporale'
timestamp_from = (dt_from.strftime("%Y-%m-%dT00:00:10"),)
timestamp_to = dt_to.strftime("%Y-%m-%dT00:00:00")

# Private config
config.read("secret.ini")
token = config.get("api", "token")
base_url = "https://fomdatamet.it"
endpoint = base_url + "/api/v1/samples"
my_headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}


def round_half_up(n, decimals=0):
    """Address the rounding problem of decimal numbers that can't be represented
    exactly with  floats"""
    multiplier = 10**decimals
    return floor(n * multiplier + 0.5) / multiplier


def get_data(station_meta):
    """For a single station, returns a tuple (timestamp_list, tmax_list, tmin_list, pp_list)"""
    my_params = {
        "from": timestamp_from,
        "to": timestamp_to,
        "resolution": "R1d",
        "station": station_meta[1],
        "param": ["Tmed_V"],
    }
    try:
        response = requests.get(endpoint, headers=my_headers, params=my_params)
        station_data = response.json()
        return station_data
    except:
        print("There was an error during HTTP request")


def loop_over_stations(target):
    goo = ""

    sheet = px.get_sheet(file_name=station_register, start_row=1)
    for station_meta in sheet:
        codice_siram = str(station_meta[3])
        print(station_meta)
        name = station_meta[0]
        station_data = get_data(station_meta)
        for record in station_data["data"]:
            instant = dt.strptime(record["timestamp"], "%Y-%m-%d %H:%M") - td(days=1)
            timestamp = instant.strftime("%Y%m%d")
            label = "Tmed_V_" + name
            val_str = record[label]
            if val_str == "NoneType":
                break
            val_float = float(val_str)
            val_decimal = round_half_up(val_float, 1)
            val_nice = str(val_decimal).replace(".", ",")
            new_row = codice_siram + ";" + timestamp + ";;;" + val_nice
            goo = goo + new_row + newline
        goo = goo + space + newline

    return goo


if __name__ == "__main__":
    final_string = loop_over_stations(station_register)
    if observations == 1:
        leaf = (
            dt_to.strftime("%B%Y")
            + underscore
            + dt_from.strftime("%d")
            + output_extension
        )
    else:
        leaf = (
            dt_to.strftime("%B%Y")
            + underscore
            + dt_from.strftime("%d")
            + dash
            + dt_to.strftime("%d")
            + output_extension
        )

    output_path =  output_dir / leaf
    with open(output_path, "w") as outfile:
        outfile.write(final_string)
