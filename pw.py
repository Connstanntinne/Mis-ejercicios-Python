#! python3
# pw.py - An insecure password locker program.

PASSWORDS= {'email': 'Fsmdifi4g45Dg84G39dlss3DU6',
            'blog': 'bnjg8dlsHlf9G2m2odSospdE', 
            'luggage': '12345'}

import sys, pyperclip  
if len(sys.argv) <2:
    print ('Usage: py pw.py [account]- copy account password')
    sys.exit()

account= sys.argv[1]       # firstcommad line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for' + account + 'copied to clipboard.')
else:
    print('There is no account named ' + account)
