#!/bin/bash
yum install httpd -y
cd /var/www/html
echo "Hello Terrform, show web content" > index.html
systemctl start httpd
systemctl enable httpd