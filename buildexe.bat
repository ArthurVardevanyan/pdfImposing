pyinstaller -F pdfImposer.py
RMDIR "build" /S /Q
RMDIR "__pycache__" /S /Q
del pdfImposer.spec
pause