@echo off
cd /d "D:\script_ossigeno"
call "D:\script_ossigeno\env\Scripts\activate.bat"
python "D:\script_ossigeno\20_upload_to_V1.py" >> "D:\script_ossigeno\log\upload_to_v1.log" 2>&1
