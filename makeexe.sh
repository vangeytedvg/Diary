echo "*** Create Executable ***"
pyinstaller -y -w -i app.ico main.py 
echo "Copying resources to dist folder"
cp app.ico ./dist/main
cp ./ui/*.qrc ./dist/main
echo "[*] Done"
