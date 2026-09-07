@echo off
cd /d "D:\script_ossigeno"
call "D:\script_ossigeno\venv\Scripts\activate.bat"
python "D:\script_ossigeno\real_thing.py" >> "D:\script_ossigeno\log\new.log" 2>&1
