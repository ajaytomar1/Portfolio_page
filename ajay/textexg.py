#! python3
#mclip.py - A multi-clipboard program



TEXT = {'agree': """yes, I agree. that sounds fine to me.""",
         'busy': """sorry, can we do this later this week or next week?""",
          'upshell': """would you consider mkeng this a monthly donation?""",

}


import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python mclip.py[keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print(' There is no text for ' + keyphrase)