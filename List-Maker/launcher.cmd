@echo off & cls
title List Maker - @DARKNOSY
color 2

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Installing now...
    bitsadmin /transfer "DownloadPython" /priority high https://www.python.org/ftp/python/3.12.4/python-3.12.4-amd64.exe %temp%\python-3.12.4-amd64.exe
    %temp%\python-3.12.4-amd64.exe /quiet InstallAllUsers=1 PrependPath=1
    del %temp%\python-3.12.4-amd64.exe
    python --version >nul 2>&1
    if %errorlevel% neq 0 (
        echo Python installation failed. Exiting...
        pause
        exit /b 1
    )
)
cls

py -m main
py src/combine.py
py src/duplicate.py
py src/reset.py

pause
exit
