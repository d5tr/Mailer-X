import smtplib
from colorama import Fore

def one_mail():

    # email sender
    your_mail = str(input(f'[{Fore.BLUE}?{Fore.WHITE}] Enter mail sender :'))
    # password email sender
    password_mail = str(input(f'[{Fore.BLUE}?{Fore.WHITE}] Enter password mail sender :'))
    # send to
    send_to = str(input(f'[{Fore.BLUE}?{Fore.WHITE}] Enter mail to send :'))

    # messga
    messga = str(input(f'[{Fore.BLUE}?{Fore.WHITE}] Enter message :'))
    try:
        # gmail or yahoo or etc .. , port smtp for send
        server = smtplib.SMTP('smtp.gmail.com', 587)
        # security
        server.starttls()
        # login mailer
        server.login(your_mail, password_mail)
        print(f'[{Fore.GREEN}+{Fore.WHITE}] Login successful ..')

        # send messga
        server.sendmail(send_to, send_to, messga)
        print(f'[{Fore.GREEN}+{Fore.WHITE}] sned message done !')
    except:
        print(f'[{Fore.RED}-{Fore.WHITE}] login filed ..')
        exit()
