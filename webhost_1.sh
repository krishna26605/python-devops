
#!/bin/bash


PACKAGE="wget unzip  httpd"
SVC="httpd"
TEMP_FILE="/tmp/webfiles"
URL="https://www.free-css.com/assets/files/free-css-templates/download/page296/healet.zip"
ZIP_FILE="healet.zip"
CP_FILE="healet-html"

sudo yum install $PACKAGE -y > /dev/null

sudo systemctl start $SVC

sudo systemctl enable $SVC

mkdir -p $TEMP_FILE && cd $TEMP_FILE



wget $URL > /dev/null


unzip $ZIP_FILE

sudo cp -r $CP_FILE/* /var/www/html/

sudo systemctl restart $SVC


rm -rf $TEMP_FILE

sudo systemctl status $SVC 


ls /var/www/html/
