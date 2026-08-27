#!/bin/bash

#============================================================================
# take DAT (TOA5) files (MainDataSet and Dia) from third directory 
# upload them to DatametV2 DEV using Rest API 
# and if successful, move them to fourth directory
#============================================================================
base_dir=/D
first_dir=$base_dir/Climate_Network
second_dir=$base_dir/Climate_Network_bis
third_dir=$base_dir/Climate_Network_ter
fourth_dir=$base_dir/Climate_Network_x
log_dir=$base_dir/logs 
# service key is kept separate and ignored by Git 

# Fallisce se manca il file di configurazione
source ./secret.sh 

method='POST'
accept='accept: application/json'
auth="Authorization: Bearer $service_key"
typ='Content-Type: multipart/form-data'

mkdir -p $log_dir

url01=$base_url/api/v1/load-jobs
url02=$base_url/api/v1/battery-samples

cd  $first_dir

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