@echo off
cd /d "D:\script_ossigeno"
call "D:\script_ossigeno\env\Scripts\activate.bat"
python "D:\script_ossigeno\40_test.py" >> "D:\script_ossigeno\log\test.log" 2>&1

