SCHTASKS /DELETE ^
/TN "invia_a_V2" ^
/F

SCHTASKS /CREATE ^
 /TN "invia_a_V2" ^
 /TR D:\script_ossigeno\11_upload_to_V2.bat ^
 /SC daily ^
 /ST 05:30 ^
 /RU OSSIGENO\Fondazione ^
 /RP Porta100


SCHTASKS /DELETE ^
/TN "invia_a_V1" ^
/F

SCHTASKS /CREATE ^
 /TN "invia_a_V1" ^
 /TR D:\script_ossigeno\21_upload_to_V1.bat ^
 /SC daily ^
 /ST 05:30 ^
 /RU OSSIGENO\Fondazione ^
 /RP Porta100
