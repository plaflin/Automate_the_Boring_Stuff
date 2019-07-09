#! python3

import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext.123, x12345
(
((\d\d\d) | (\(\d\d\d\)))?  # area code (optional)
(\s | -)                    # first separator
\d\d\d                      # first 3 digits
-                           # separator
\d\d\d\d                    # last 4 digits
(((ext(\.)?\s | x)          # extension word-part (optional)
(\d{2,5}))?                 # extension number-part (optional)
)
''', re.VERBOSE)

# Create a regex for email address
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+
@
[a-zA-Z0-9_.+]+
''', re.VERBOSE)

# Get the text off of the clipboard
text = pyperclip.paste()

# Extract the email addresses/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
