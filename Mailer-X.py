from ban_Mailer_X import *
from sender.one_mail import *
from sender.list_mail import *
import os

miler_ban()

you_want = int(input('[?] Enter number :'))

if you_want == 1:
    os.system('clear')
    mailer_1()
    one_mail()
elif you_want == 2:
    os.system('clear')
    mailer_2()
    list_mail()
elif you_want == 99 :
    print('Good bay ...')
    exit()