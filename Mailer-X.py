from ban_Mailer_X import *
from sender.Mail import *
from sender.SMSx import *
from colorama import Fore
import time
import os


def Start():
    os.system('clear')
    miler_ban()

    you_want = int(input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter number :'))

    if you_want == 1:
        
        os.system('clear')
        mailer_1()
        
        # email sender
        your_mail = str(input(f'[{Fore.BLUE}?{Fore.WHITE}] Enter mail sender :'))
        # password email sender
        password_mail = str(input(f'[{Fore.BLUE}?{Fore.WHITE}] Enter password mail sender :'))
        # send to
        send_to = str(input(f'[{Fore.BLUE}?{Fore.WHITE}] Enter mail to :'))

        # messga
        message = str(input(f'[{Fore.BLUE}?{Fore.WHITE}] Enter message :'))
        
        Sends = Mailx()
        Sends.one_mail(your_mail, password_mail, send_to, message)

    elif you_want == 2:
        
        os.system('clear')
        mailer_2()
        
        # email sender
        your_mail = str(input(f'[{Fore.BLUE}?{Fore.WHITE}] Enter mail sender :'))
        # password email sender
        password_mail = str(input(f'[{Fore.BLUE}?{Fore.WHITE}] Enter password mail sender :'))
        # send to
        send_to = input(f'[{Fore.BLUE}?{Fore.WHITE}] Enter list file mail :')
        # messga
        messga = str(input(f'[{Fore.BLUE}?{Fore.WHITE}] Enter message :'))

        SendS = Mailx()
        SendS.list_mail(your_mail, password_mail, send_to, messga)
        

    elif you_want == 3 :
        
        os.system('clear')
        mailer_2()
        print(f'{Fore.RED} you can send one message in day ... {Fore.WHITE}\n')
        time.sleep(1)

        Numberx = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter number target : ')
        Messagex = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter Message : ')

        Send = SMS(Numberx, Messagex)
        Send.SMS_textbelt()

    elif you_want == 4 :
        
        os.system('clear')
        mailer_1()
        print(f"{Fore.RED} if you don't have twilio go to ' https://twilio.com ' \n and sing up .{Fore.WHITE}")

        None_ = input('\nPress [ Enter ] to continue ... ')

        num = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter number target : ')
        mess = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter message : ')
        sid = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter SID : ')
        tok = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter token : ')
        your = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter your number : ')

        SEND = SMS(num, mess, sid, tok, your)
        SEND.SMS_twilio()

    elif you_want == 99 :
        print('Good bay ...')
        exit()

Start()