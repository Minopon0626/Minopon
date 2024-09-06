@echo off
REM 仮想環境が存在するディレクトリに移動
cd /d "%~dp0"

REM 仮想環境を有効化
call myenv\Scripts\activate.bat

REM 仮想環境がアクティブ化されたことを確認するメッセージ
echo 仮想環境 myenv がアクティブ化されました
