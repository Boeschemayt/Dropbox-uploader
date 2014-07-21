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
    try
    upload = open(uploadFile, "rb")
    client.put_file("/"+uploadFile, upload)
    


if __name__ == "__main__":
    main()