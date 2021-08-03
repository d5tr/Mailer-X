import smtplib
from colorama import Fore

class Mailx :

    @classmethod
    def one_mail(self, mail_sender, password_sender, mail_to, Message):
    

        try:
            # gmail or yahoo or etc .. , port smtp for send
            server = smtplib.SMTP('smtp.gmail.com', 587)
            # security
            server.starttls()
            # login mailer
            server.login(mail_sender, password_sender)
            print(f'[{Fore.GREEN}+{Fore.WHITE}] Login successful ..')

            # send messga
            server.sendmail(mail_to, mail_to, Message)
            print(f'[{Fore.GREEN}+{Fore.WHITE}] sned message done !')
        except:
            print(f'[{Fore.RED}-{Fore.WHITE}] login filed ..')
            exit()

    @classmethod
    def list_mail(self, mail_sender2, password_sender2, file_emails, Message2):
        
        send_to = open(file_emails, 'r').readlines()
        print(f'[{Fore.GREEN}+{Fore.WHITE}] Try login ...')
        for file in send_to:
            file = str(file).strip()


            # gmail or yahoo or etc .. , port smtp for send
            server = smtplib.SMTP('smtp.gmail.com', 587)
            # security
            server.starttls()
            # login mailer
            server.login(mail_sender2, password_sender2)


            # send messga
            server.sendmail(file, file, Message2)
            print(f'[{Fore.GREEN}+{Fore.WHITE}] sned message done for -->', Fore.CYAN+file, Fore.WHITE)
    