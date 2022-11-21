try {
Get-Command python
Get-Command pyinstaller

} catch {
echo "Please make sure you have Python and Pyinstaller"
}
python --version
echo "Pyinstaller"+$(pyinstaller --version)
pyinstaller --onefile --icon=c.ico jcc.py
copy ./dist/jcc.exe ./jcc.exe
echo "All done!"