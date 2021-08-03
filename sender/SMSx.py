import requests
from colorama import Fore
from twilio.rest import Client

class SMS :
    
    def __init__(self, Number='', Message='', SID='', token='', yor_number=''):
        self.SID = SID
        self.token = token
        self.yor_number = yor_number
        self.Number = Number
        self.Message = Message


    def SMS_textbelt(self):

        resp = requests.post('https://textbelt.com/text', {
          'phone': f'{self.Number}',
          'message': f'{self.Message}',
          'key': 'textbelt',
        })
        if '"success":true' in resp :
            print(f'[{Fore.GREEN}+{Fore.WHITE}] SMS sent ...')

        else:
            print(f"[{Fore.RED}-{Fore.WHITE}] Error can't send now ! \n Try later ...")


    def SMS_twilio(self):
        
        # Find your Account SID and Auth Token at twilio.com/console
        # and set the environment variables. See http://twil.io/secure

        account_sid = self.SID
        auth_token = self.token
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                body=f'{self.Message}',
                from_=f'{self.yor_number}',
                to=f'{self.Number}'
            )

        print(message.sid)