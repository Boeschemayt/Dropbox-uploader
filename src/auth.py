# -*- coding: utf-8 -*-
import dropbox
from simplecrypt import encrypt
import xml.etree.ElementTree as et
from xml.etree.ElementTree import ParseError


app_key = "zigq5mu2x2jojmt"
app_secret = "biwwzh9fex3r5fu"
flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
def main():

    authUrl = flow.start()
     
    print "Go to this URL and press Accept"
    print authUrl
    code = raw_input("Enter the Auth code here:").strip()
    access_token, user_id = flow.finish(code)
    password = raw_input("select a password for your Authentication.")
    saveAuthCode(access_token, password)
     
def saveAuthCode(auth, password):
    cipherAuth = encrypt(password, auth)
    cipherpass = encrypt(password, password)
    try:
        tree = et.parse("auth.xml")
        root = tree.getroot()
        root[0][0].text = cipherAuth
        root[0][1].text = cipherpass
        tree.write("auth.xml")
        
    except ParseError, e:
        print "**************************"
        print "Something went wrong\n", e
        print "**************************"    
    
    

        
if __name__ == "__main__":
    main()
    
