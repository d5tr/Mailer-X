#!/bin/bash

WHO=$(whoami)

if [ $WHO == root ]
then

cd /root/Mailer-X && sudo python3 Mailer-X.py

else

echo 'you must be root ! '
echo 'use sudo'

fi
