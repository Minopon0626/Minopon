@echo off
REM UTF-8をサポートするコードページに変更
chcp 65001

REM コマンドプロンプトを開き、仮想環境が存在するディレクトリに移動
cd /d "%~dp0"

REM 仮想環境を有効化
call myenv\Scripts\activate.bat

REM 仮想環境がアクティブ化されたことを確認するメッセージ
echo 仮想環境 myenv がアクティブ化されました

REM コマンドプロンプトが閉じないようにするために、ユーザーからの入力を待つ
cmd /k
