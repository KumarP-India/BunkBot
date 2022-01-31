@echo off

color 6

cd "C:\Users\kumar\OneDrive\Documents\Programs\Windows\Python\BunkBot\Program Files"

call conda activate BunkBot

python BunkBot.py

call conda deactivate

echo "Program Closed Sucessfully!"

:y

set /p ans="Close the Window? [Y]es [n]o: "

if "%ans%"=="Y" (echo " ") else (echo " ")

if "%ans%"=="y" (echo " ") else (echo " ")

if "%ans%"=="n" (goto y) else (echo " ")

if "%ans%"=="N" (goto y) else (echo " ")




