#!/bin/bash

WHO=$(whoami)

if [ $WHO == root ]
then

cd /root && rm -rf Mailer-X
cd /bin && rm Mailer-X

echo 'Done uninstall ...'

else

echo 'you must be root'
echo 'use sudo '

fi
