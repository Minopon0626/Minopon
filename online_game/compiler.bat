@echo off
REM UTF-8をサポートするコードページに変更
chcp 65001

REM コマンドプロンプトを開き、仮想環境が存在するディレクトリに移動
cd /d "%~dp0"

REM 仮想環境を有効化
call myenv\Scripts\activate.bat

REM 仮想環境がアクティブ化されたことを確認するメッセージ
echo 仮想環境 myenv がアクティブ化されました

REM PyInstallerでserver.pyをexeに変換
pyinstaller --onefile --noconsole server.py

REM PyInstallerでclient.pyをexeに変換
pyinstaller --onefile --noconsole client.py

REM 完了メッセージ
echo server.py と client.py の .exe ファイルの作成が完了しました。

REM コマンドプロンプトが閉じないようにするために、ユーザーからの入力を待つ
cmd /k
