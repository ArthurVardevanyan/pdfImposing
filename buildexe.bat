pyinstaller -F pdfImposing.py
RMDIR "build" /S /Q
RMDIR "__pycache__" /S /Q
del pdfImposing.py.spec
pause