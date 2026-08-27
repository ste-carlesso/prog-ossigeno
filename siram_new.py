from pathlib import Path
import configparser
import requests

base_dir = Path("D:")
first_dir = base_dir / "Climate_Network"
log_dir = base_dir / "logs" 

# Private config
config.read("secret.ini")
token = config.get("api", "token")
base_url = "https://fomdatamet.it"
url01 = base_url + "/api/v1/load-jobs"
url02 = base_url + "/api/v1/battery-samples"
my_headers = {
    "Authorization": f"Bearer {token}", 
    "Content-Type": "application/json"
    }

my_params = {
    "from": timestamp_from,
    "to": timestamp_to,
    "resolution": "R1d",
}


for leaf in *.dat; do
	if [[ "$leaf" ==  *MainDataSet*.dat ]] ; then
		url=$url01
		echo "main"
	elif [[ "$leaf" == *Dia*.dat ]] ; then
		url=$url02
		echo "dia"
	else
		url=""
		echo "undefined"
	fi


    try:
    response = requests.post(endpoint, headers=my_headers, params=my_params)
    station_data = response.json()
    return station_data
    except:
        print("There was an error during HTTP request")

	dat="file=@$leaf"

	out=$(/D/script_ossigeno/curl.exe -X "$method" $url -H "$accept" -H "$auth" -H "$typ" -F $dat -s)

	echo "$out" >> $log_dir/$(date +%Y%m%d)_to_v2.log
	
	# EXAMPLE OF A FAILURE
	# {"message":"Unauthorized"}

	# EXAMPLE OF A SUCCESS
	# {"success":true,"message":"Samples are duplicate. Load job has been updated with warnin
	# g status 'duplicate'","loadJob":{"id":"cmosqsaju01j0s6017yitwxs1","archivedFilePath":"j
	# obs/2026/5/5/05-05-2026-14:47:08-57-OK.csv","originalFileName":"BERGAMO_MainDataSet_202
	# 6_05_04_0450.dat","samplesFrom":"2026-05-04T03:50:00.000Z","samplesTo":"2026-05-05T03:4
	# 0:00.000Z","stationNumber":"R0610134","stationId":"cmoqz7e6u01kr2326mdouw04o","hasError
	# s":false,"warningStatus":"duplicate","createdAt":"2026-05-05T14:47:09.162Z","updatedAt"
	# :"2026-05-05T14:47:09.162Z"}}

	if [[ "$out" =~ ^\{\"success\"\:true.* ||  "$out" =~ \{\"status\"\:\"success\" ]]
	then 
		echo "Good"
		mv $leaf $second_dir
	else

		echo "something is wrong"
	fi
done