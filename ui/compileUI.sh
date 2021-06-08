DIR=$(pwd)
echo "$DIR"
echo "Compiling GUI files"
for FILE in "$DIR"/*.ui; do
  # Show what is compiling
  echo "Compiling ${FILE##*/}"
  # Get the basename of the file (no extension). We know the extension
  # is .ui, so get rid of it
  source=$(basename "$FILE" .ui)
  # Make the target filename, the syntax for bash 4 will uppercase the
  # first letter of the filename
  echo "frm${source^}".py
  #pyuic5 -o test.py "$f"
done


