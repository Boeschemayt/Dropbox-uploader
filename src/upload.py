import dropbox

client = ""

def main():
    getAccessToken()
    printClientInfo()



def getAccessToken():
    global client
    with open("AuthCode.txt","r") as text_file:
        access_token = text_file.readline().rstrip()
        client = dropbox.client.DropboxClient(access_token)   
        
def printClientInfo():
    print client.account_info()

if __name__ == "__main__":
    main()