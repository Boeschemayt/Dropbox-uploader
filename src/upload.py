import dropbox
import sys
from dropbox.rest import ErrorResponse
client = ""

def main(argv):
    if argv == "upload":
        getAccessToken()
        upload(sys.argv[2])
    else:
        info()

def getAccessToken():
    global client
    with open("AuthCode.txt", "r") as text_file:
        access_token = text_file.readline().rstrip()
        client = dropbox.client.DropboxClient(access_token)   
        
def upload(uploadFile):
    try:
        upload = open(uploadFile, "rb")
        client.put_file("/" + uploadFile, upload)
        print "You have uploaded "+ uploadFile+" to your dropbox."
    except ErrorResponse:
        print "Something went wrong. " + ErrorResponse
        
def info():
    print "some info."

if __name__ == "__main__":
    main(sys.argv[1])
