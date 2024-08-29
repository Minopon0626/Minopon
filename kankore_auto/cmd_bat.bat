@echo off
REM コマンドプロンプトを開く
start cmd /k "cd /d %~dp0 && virtual_environment\Scripts\activate.bat"
