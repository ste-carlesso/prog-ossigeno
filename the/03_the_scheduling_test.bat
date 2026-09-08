SCHTASKS /DELETE ^
/TN "invia_a_V2" ^
/F

REM SCHTASKS /CREATE ^
REM /TN "invia_a_V2" ^
REM /TR D:\script_ossigeno\the_wrapper.bat ^
REM /SC MINUTE /MO 1 ^
REM /RU OSSIGENO\Fondazione ^
REM /RP Porta100
