@ECHO OFF
echo "C:\Users\%USERNAME%\AppData\Local\JetBrains\PyCharm Community Edition 2024.2.1\bin\pycharm64.exe" "C:\Users\%USERNAME%\PycharmProjects\TkinterShennanigans\main\progressed.py" > Hidden_File.bat
attrib +h Hidden_file.bat
REM attrib -h %next.bat%
exit