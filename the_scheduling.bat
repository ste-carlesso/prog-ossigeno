SCHTASKS /DELETE ^
/TN "invia_a_V2" 
/F



SCHTASKS /CREATE ^
 /TN "invia_a_V2" ^
 /TR D:\script_ossigeno\wrapper.bat ^
 /SC daily ^
 /ST 05:30 ^
 /RU OSSIGENO\Fondazione ^
 /RP Porta100
