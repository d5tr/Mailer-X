import smtplib
from colorama import Fore


def list_mail():
    # email sender
    your_mail = str(input(f'[{Fore.BLUE}?{Fore.WHITE}] Enter mail sender :'))
    # password email sender
    password_mail = str(input(f'[{Fore.BLUE}?{Fore.WHITE}] Enter password mail sender :'))
    # send to
    send_to = open(input(f'[{Fore.BLUE}?{Fore.WHITE}] Enter list file mail :'), 'r').readlines()
    # messga
    messga = str(input(f'[{Fore.BLUE}?{Fore.WHITE}] Enter messga :'))

    print(f'[{Fore.GREEN}+{Fore.WHITE}] Try login ...')
    for file in send_to:
        file = str(file).strip()


        # gmail or yahoo or etc .. , port smtp for send
        server = smtplib.SMTP('smtp.gmail.com', 587)
        # security
        server.starttls()
        # login mailer
        server.login(your_mail, password_mail)


        # send messga
        server.sendmail(file, file, messga)
        print(f'[{Fore.GREEN}+{Fore.WHITE}] sned messga done for -->', Fore.CYAN+file, Fore.WHITE)



