@echo off
cd /d "D:\script_ossigeno"
call "D:\script_ossigeno\env\Scripts\activate.bat"
python "D:\script_ossigeno\the_real_thing.py" >> "D:\script_ossigeno\log\the_real.log" 2>&1
