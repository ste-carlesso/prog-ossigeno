@echo off
"C:\Program Files\OpenVPN\bin\openvpn-gui.exe" ^
	--silent_connection 0 ^
	--show_script_window 0 ^
	--show_balloon 0 ^
	--config_dir "C:/Users/Fondazione/OpenVPN/config/fondazione-ossigeno-fosforovpn/" ^
	--command connect "fondazione-ossigeno-fosforovpn.ovpn" ^
	>> "D:\script_ossigeno\log\connect.log" 2>&1