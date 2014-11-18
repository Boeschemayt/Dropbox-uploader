import dropbox
import xml.etree.ElementTree as et
from xml.etree.ElementTree import ParseError
from binascii import hexlify


app_key = "zigq5mu2x2jojmt"
app_secret = "biwwzh9fex3r5fu"
flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
def main():

    authUrl = flow.start()
       
    print("Go to this URL and press Accept")
    print (authUrl)
    code = input("Enter the Auth code here:").strip()
    access_token, user_id = flow.finish(code)
    password = input("select a password for your Authentication.")
    saveAuthCode(access_token, password)
     
def saveAuthCode(auth, password):
    #Todo. encrypt and save in the xml file.
    #cipherAuth = encrypt(password, auth)
    #cipherpass = encrypt(password, password)
    
    try:
        tree = et.parse("authsave.xml")
        root = tree.getroot()
        root[0][0].text = auth
        root[0][1].text = password
        root[0][2].text = "null"
        tree.write("authsave.xml")
         
    except ParseError as e:
        print("**************************")
        print("Something went wrong\n", e)
        print("**************************")    
     
    

        
if __name__ == "__main__":
    main()
    
