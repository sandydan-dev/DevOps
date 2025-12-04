#!/bin/bash
yum install httpd -y
cd /var/www/html
echo "Hello terraform" > index.html
systemctl start httpd
systemctl enable httpd