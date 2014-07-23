import dropbox
import sys
from dropbox.rest import ErrorResponse
client = ""

def main(argv):
    if argv == "upload":
        getAccessToken()
        upload(sys.argv[2])
    elif argv == "list":
        getAccessToken()
        list()
    elif argv == "info":
        getAccessToken()
        info()

def getAccessToken():
    global client
    with open("AuthCode.txt", "r") as text_file:
        access_token = text_file.readline().rstrip()
        client = dropbox.client.DropboxClient(access_token)
    return access_token   
        
def upload(uploadFile):
    try:
        upload = open(uploadFile, "rb")
        client.put_file("/" + uploadFile, upload)
        print "You have uploaded "+ uploadFile+" to your dropbox."
    except ErrorResponse:
        print "Something went wrong. " + ErrorResponse
        
def info():
    info = client.account_info()
    print "Display name >> " +info["display_name"]        
    print "Country >> " +info["country"]

def list():
    try:
        itemArray = []
        folder = client.metadata("/", "true")
        itemArray = folder["contents"]
        
        for item in itemArray:
            if item["is_dir"] is True:
                print item["path"]
            
    except ErrorResponse:
        print "something went wrong " + ErrorResponse
        
if __name__ == "__main__":
    main(sys.argv[1])
