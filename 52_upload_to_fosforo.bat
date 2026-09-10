@echo off
cd /d "D:\script_ossigeno"
call "D:\script_ossigeno\env\Scripts\activate.bat"
python "D:\script_ossigeno\50_upload_to_fosforo.py" >> "D:\script_ossigeno\log\upload_to_fosforo.log" 2>&1
python "D:\script_ossigeno\51_upload_raw.py" >> "D:\script_ossigeno\log\upload_to_fosforo.log" 2>&1
