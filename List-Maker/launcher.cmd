@echo off & cls
color 2

py -m main
py src/combine.py
py src/duplicate.py
py src/reset.py

pause
exit