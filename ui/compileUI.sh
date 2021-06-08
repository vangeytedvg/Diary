DIR=$(pwd)
echo "$DIR"
for FILE in "$DIR"/*.ui; do
  echo "Compiling ${FILE##*/}"
  test=$(basename "$FILE" .ui)
  echo "frm_$test"
  #pyuic5 -o test.py "$f"
done


