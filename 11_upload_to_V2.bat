2@echo off
cd /d "D:\script_ossigeno"
call "D:\script_ossigeno\env\Scripts\activate.bat"
python "D:\script_ossigeno\10_upload_to_V2.py" >> "D:\script_ossigeno\log\upload_to_v2.log" 2>&1
