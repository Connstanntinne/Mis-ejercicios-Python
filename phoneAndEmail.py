#! python3 
# phonAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

phone_regex= re.compile(r'''(
    (\d{3}|\(\d{3}\))?                         # area code
    (\s|-|\.)?                                 # separator
    (\d{3})                                    # first 3 digits
    (\s|-|\.)                                  # separator
    (\d{4})                                    # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?             # extension
    )''', re.VERBOSE)

# Create email regex.

email_regex= re.compile(r'''(
    [a-zA-Zo-9._%+-]+                          # username
    @                                          # @ symbol
    [a-zA-Zo-9.-]+                             # domain name
    (\.[a-zA-Z]{2,4})                          # dot-something
    )''', re.VERBOSE)



# Find matches in clipboard text.
text= str(pyperclip.paste())
matches= []
for groups in phone_regex.findall(text):
    phone_num= '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)
for groups in email_regex.findall(text):
    matches.append(groups[0])



# Copy resultis to the clipboard.
if len(matches)> 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')




