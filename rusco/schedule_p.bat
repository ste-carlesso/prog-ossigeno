SCHTASKS /CREATE ^
 /TN "invia_a_fosforo" ^
 /TR D:\script_ossigeno\UPLOAD_TO_FOSFORO.bat ^
 /SC daily ^
 /ST 06:50 ^
 /RU OSSIGENO\Fondazione ^
 /RP Porta100