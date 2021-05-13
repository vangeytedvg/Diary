echo "Start Git script"
git add *
echo "Comments?  "
read comment

git commit -m $comment

git push -u origin main