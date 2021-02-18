print('''
make by d5tr 
insta = d_5tr
#################################
don't use tool for hurt anyone !!
''')
from mailer import Mailer
file_send = open('enter file name !','r')
for x in file_send:

    mail = Mailer(email='enter your email !',password='enter password email')
  
    mail.send(receiver=x,subject='your subject',message='your meassage !')
    
        