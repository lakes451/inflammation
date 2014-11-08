#copy and rename the file with a different filename (date-drug.dat)
#
#$1 = filename
#$2 = date

DRUG=$(python src/assign_drug.py $1)

DEST=data/$2/$2-$DRUG.dat
#echo $DRUG

echo cp $1 $DEST
echo git add $DEST
echo git commit -m "copy and move $1 to $DEST"
