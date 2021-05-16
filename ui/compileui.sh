echo "Compiling GUI"
echo "Compiling Resource file"
pyrcc5 -o icons_rc.py ./ui/icons.qrc 
echo "Compiling GUI"
echo "[1] main_ui.ui ---> frmMain.py"
pyuic5 -o frmMain.py ./ui/main_ui.ui
echo "[2] settings.ui ---> frmSettings.py"
pyuic5 -o frmSettings.py ./ui/settings.ui

echo "Done"
