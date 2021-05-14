echo "Starting Git "
git add *
echo "Comments?  "
read comment
echo "EXECUTING : $comment"

git commit -m "$comment"

git push -u origin main

echo "DONE...."