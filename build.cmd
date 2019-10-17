@echo off
cd /d "%~dp0"
python setup.py bdist_wheel --plat-name=win_amd64
