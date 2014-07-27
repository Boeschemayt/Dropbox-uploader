import dropbox
from simplecrypt import encrypt

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
    with open("AuthCode.txt", "w") as text_file:
        text_file.writelines(cipherAuth)
        
        
if __name__ == "__main__":
    main()
    