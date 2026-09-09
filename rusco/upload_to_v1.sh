#!/bin/bash

#============================================================================
# take DAT (TOA5) files MainDataSet*.dat  from second directory 
# upload them to DatametV1 and, if successful, move them to third directory
# take Dia*.dat from second dir and simply move then to third dir
#============================================================================
base_dir=/D
first_dir=$base_dir/Climate_Network
second_dir=$base_dir/Climate_Network_bis
third_dir=$base_dir/Climate_Network_ter
fourth_dir=$base_dir/Climate_Network_x
log_dir=$base_dir/logs
## curl -v -F file=@ANCONA_MainDataSet_2020_09_01_0340.dat http://192.168.1.90:9000/load-jobs


mkdir -p $log_dir

# Datamet V1 PROD
url='http://46.137.162.248/load-jobs'

cd  $second_dir

wow='{ succcess: true }'

for leaf in *.dat; do
	if [[ "$leaf" ==  *MainDataSet*.dat ]] ; then
		echo "main"
		dat="file=@$leaf"
		out=$(/D/script_ossigeno/curl.exe -F $dat $url -s)
		
		echo "$out" >> $log_dir/$(date +%Y%m%d)_to_v1.log
		if [[ $out == $wow ]]; then
		# if [[ $out =~ ^\{\s?succcess\:\s?true\s?\}.* ]] ; then 
			echo "Good"
			mv $leaf $third_dir
		else
			echo "something is wrong"
		fi
		
	elif [[ "$leaf" == *Dia*.dat ]] ; then
		echo "dia"
		mv $leaf $third_dir
	fi


done