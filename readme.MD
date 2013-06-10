This project is about connceting to gmail vai OAthu 2.0(orignal i.e 3-step)

QUE_1
==============================================================
Step 1
Authenticating user for Gmail access by requesting to

https://accounts.google.com/o/oauth2/auth?   (GET/POST  any method)
By 
Scope : https://mail.google.com/
Application client id:  ****************.apps.googleusercontent.com
redirect_url :      http://localhost:14085/grantblank/    (or your server url )
TYPE : code

===============================================================
Step-2:
If every parameter is right than server will response with code to your redirect uri 
From that u have to get your code 
Than u have to request to Google server for access token  to url  

https://accounts.google.com/o/oauth2/token?  ( POST method )
By 
Application client id:  ****************.apps.googleusercontent.com
Application secret id : **********************
Code : code u get from response 
redirect_url :      http://localhost:14085/grantblank/    (or your server url )
grant_type:      authorization_code
        
		==========================
Now if everything is fine u can get the access token from the response 
		
========================================================================
Step-3:
Now u have access token 

how to read the mail from this access token by following code
     ============================================================
     ==== https://developers.google.com/gmail/                  =
     ===  https://developers.google.com/gmail/xoauth2_protocol  =
	 ==== https://developers.google.com/gmail/xoauth2_libraries = (devlopers-google.py)
     ============================================================
code 
"
def GenerateOAuth2String(username, access_token, base64_encode=True):	 
auth_string = 'user=%s\1auth=Bearer %s\1\1' % (username, access_token)
  if base64_encode:
    auth_string = base64.b64encode(auth_string)
  return auth_string
  
  
imap_conn = imaplib.IMAP4_SSL('imap.gmail.com')  ## error in this connection
imap_conn.debug = 4
imap_conn.authenticate('XOAUTH2', lambda x: GenerateOAuth2String(username, access_token, base64_encode=True))   ## method GenerateOAuth2String called from here to genrate OAuth2String
imap_conn.select('INBOX')
  
"
( Requirement )
For my Google app engine what I have done is my application is bill enabled to create socket     
Python 2.7 (use this version )
Import ssl  (no ssl in 2.5 )
See  app.yaml  for other setting

===========================================================================================

QUE_2:

===========================================================================================

que-2 : 2-leged loginvia python script(code is working) 

code :
"
import ssl

conn = imaplib.IMAP4_SSL("imap.gmail.com", 993)
conn.login(user, pwd)
conn.select()
print "logged in"
"

we can connect to gmail via 2-leged and can read mail from it.
the script for that is in the file "demo-2-leged.py "

but i want to know 
Whether Google app script is 2-leged or not and if it is 2-leged than how to use it  .


==============================================================================================