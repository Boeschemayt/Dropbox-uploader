import dropbox
import sys
client = ""

def main():
    getAccessToken()
    upload(sys.argv[1])



def getAccessToken():
    global client
    with open("AuthCode.txt","r") as text_file:
        access_token = text_file.readline().rstrip()
        client = dropbox.client.DropboxClient(access_token)   
        
def upload(uploadFile):
    client.put_file("/"+uploadFile, uploadFile)
    


if __name__ == "__main__":
    main()