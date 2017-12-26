echo "Beginning teardown .."
mysql -u root sys < dropDB.txt
echo "teardown complete !"

echo "beginning creation ..."
mysql -u root sys < createDB.txt
echo "creation complete"
