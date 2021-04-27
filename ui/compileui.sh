echo "Compiling GUI"
echo "[1] main_ui.ui ---> frmMain.py"
pyuic5 -o frmMain.py ./ui/main_ui.ui
echo "Done"
