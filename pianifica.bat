schtasks /create /tn upload_to_datamet ^
 /tr D:\script_ossigeno\setup_scheduler\upload_to_datamet.bat ^
 /sc daily /st 06:00 ^
 /ru OSSIGENO\Fondazione /rp Porta100

schtasks /create /tn upload_to_fosforo ^
 /tr D:\script_ossigeno\setup_scheduler\upload_to_fosforo.bat ^
 /sc daily /st 06:00 ^
 /ru OSSIGENO\Fondazione /rp Porta100

schtasks /create /tn upload_raw ^
 /tr D:\script_ossigeno\setup_scheduler\raw.bat ^
 /sc daily /st 07:00 ^
 /ru OSSIGENO\Fondazione /rp Porta100
