echo "Starting Git "
git add *
echo "Comments?  "
read comment
echo "EXECUTING : $comment"
# Need to use "" to allow multiple words!
git commit -m "$comment"

git push -u origin main

echo "DONE...."