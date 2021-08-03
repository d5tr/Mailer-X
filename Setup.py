import os

XX = os.getcwd()

CLAN = str(XX)

cc = CLAN.replace('Mailer-X', '')

os.system(f'cd {cc} && cp -r Mailer-X /root')
os.system(f'mv Mailer-X.sh /bin/Mailer-X')

print('Done ...')