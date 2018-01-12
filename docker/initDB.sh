service mysql restart
echo "beginning creation ..."
mysql -uroot -ppassword < createDB.txt
echo "creation complete"
