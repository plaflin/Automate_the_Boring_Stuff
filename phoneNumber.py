import re
def isPhoneNumber(text):
    # Commented out code does the same thing as the regular expression
    #if len(text) != 12:
    #    return False
    # for i in range(0,3):
    #    if not text[i].isdecimal():
    #         return False
    #if text[3] != '-':
    #    return False
    #for i in range(4,7):
    #    if not text[i].isdecimal():
    #        return False
    #if text[7] != '-':
    #    return False
    #for i in range(8,12):
    #    if not text[i].isdecimal():
    #        return False
    #
    #return True
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    try:
         # The first two lines finds the first phone number
         match_object = phoneNumRegex.search(text)        
         print(match_object.group())
         # This line finds all of the phone numbers
         print(phoneNumRegex.findall(text))
    except:
        print('There were no phone numbers in the text.')
    
isPhoneNumber('813-867-5309')
isPhoneNumber('Hello')

