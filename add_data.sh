#copy and rename the file with a different filename (date-drug.dat)
#
#$1 = filename
#$2 = date

DRUG=$(python src/assign_drug.py $1)

DEST=data/$2/$2-$DRUG.dat

MSG="copy and move $1 to $DEST"

cp $1 $DEST
git add $DEST
git commit -m $MSG
echo "New file added to the repository: $DEST"
