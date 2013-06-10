####################### 2-leded login  ##############################

import imaplib
import email
import getpass

def extract_body(payload):
    if isinstance(payload,str):
        return payload
    else:
        return '\n'.join([extract_body(part.get_payload()) for part in payload])


#get username and password from user
user = raw_input("Enter your username:")
pwd = getpass.getpass("Enter your password: ")


try:
    conn = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    conn.login(user, pwd)
    conn.select()
    print "logged in"
except:
    print "Login failed."

#resp, items = conn.recent()
resp, items = conn.search(None,'UNSEEN')
resp1, item1 = conn.search(None, "ALL")

#print item1[0].split()
count = 0
email_box = []
mails = []

for email_box in item1[0].split():
    count = count + 1
    
print "total no of emails are: ", count

cnt_unread = 0
for mails in items[0].split():
    cnt_unread = cnt_unread + 1

print "total no of unread mail are: ", cnt_unread


#except:
#    print "Not any unseen mail into your mail-box."

#for n in items[0].split():
#    print conn.fetch(n,'(RFC822)')


n=items[0].split()
resp,message = conn.fetch(n[0],'(RFC822)')


emailBody = message[0][1]

mail = email.message_from_string(emailBody)



#print "["+mail["From"]+"] :" + mail["Subject"]
type = mail.get_content_type()


#print type
payload = mail.get_payload()
body=extract_body(payload)
#print(body)


f = open('file.txt','w')
f.write('your message is = ' + repr(body) + '\n')
f.close()




#import implib
#import email
#import getpass




#def extract_body(payload):
#    if isinstance(payload,str):
#        return payload
#    else:
#        return '\n'.join([extract_body(part.get_payload()) for part in payload])


# get user name and password from gmail user

#user = ("Enter your username:")
#pwd = getpass.getpass("Enter your password: ")






#try:
#    conn = imaplib.IMAP4_SSL("imap.gmail.com", 993)
#    conn.login(user, pwd)
#    conn.select()

#except:
#    print "Login failed."


#resp, items = conn.search(None,'UNSEEN')

#n=items[0].split()
#resp,message = conn.fetch(n[0],'(RFC822)')
#emailBody = message[0][1]
#mail = email.message_from_string(emailBody)
#print "["+mail["From"]+"] :" + mail["Subject"]
#type = mail.get_content_type()
#print type
#payload = mail.get_payload()
#body=extract_body(payload)
#print(body)

#from datetime import datetime, timedelta
#import email
#from imapclient import IMAPClient

#HOST = 'imap.gmail.com'
#USERNAME = 'username'
#PASSWORD = 'password'
#ssl = True

#today = datetime.today()
#cutoff = today - timedelta(days=5)

## Connect, login and select the INBOX
#server = IMAPClient(HOST, use_uid=True, ssl=ssl)
#server.login(USERNAME, PASSWORD)
#select_info = server.select_folder('INBOX')

## Search for relevant messages
## see http://tools.ietf.org/html/rfc3501#section-6.4.5
#messages = server.search(['FROM "alerts@azoi.com"', 'SINCE %s' % cutoff.strftime('%d-%b-%Y')])
#response = server.fetch(messages, ['RFC822'])

#for msgid, data in response.iteritems():
 #   msg_string = data['RFC822']
  #  msg = email.message_from_string(msg_string)
   # print 'ID %d: From: %s Date: %s' % (msgid, msg['From'], msg['date'])
