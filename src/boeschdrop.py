import dropbox
import sys
from dropbox.rest import ErrorResponse
client = ""

def main(argv):

    if argv == "upload":
        getAccessToken()
        upload(sys.argv[2])
    elif argv == "ls":
        getAccessToken()
        ls(sys.argv[2])
    elif argv == "info":
        getAccessToken()
        info()
    elif argv == "rm":
        getAccessToken()
        delete(sys.argv[2])
    else:
        print "Not a valid command."

def getAccessToken():
    global client
    with open("AuthCode.txt", "r") as text_file:
        access_token = text_file.readline().rstrip()
        client = dropbox.client.DropboxClient(access_token)
    return access_token   

#Upload function with one parameter, uploadfile.
#TODO - fix chunked upload for bigger files over 150MB.
def upload(uploadFile):
    try:
        upload = open(uploadFile, "rb")
        client.put_file("/" + uploadFile, upload)
        print "You have uploaded " + uploadFile + " to your dropbox."
    except ErrorResponse:
        print "Something went wrong. " + ErrorResponse
        
def info():
    info = client.account_info()
    print "Display name >> " + info["display_name"]        
    print "Country >> " + info["country"]


# List different elements in remote folder / with parameters:
# dir - for list all the folders
# files - for list all the files
# all - for list everything in root folder.
def ls(listArg):
    try:
        itemArray = []
        folder = client.metadata("/", "true")
        itemArray = folder["contents"]
        if listArg == "dir":  # <- list only dirs
            for item in itemArray:
                if item["is_dir"] is True:
                    print item["path"]
        elif listArg == "files":  # <- list only files
            for item in itemArray:
                if item["is_dir"] is False:
                    print "# "+item["path"]
        elif listArg == "all":  # <- list all the files and dirs.
            sortedArray = sorted(itemArray, key=lambda item: item["is_dir"])
            for item in sortedArray:
                if item["is_dir"] == True:
                    print item["path"]
                else: 
                    print "# "+item["path"]
                
    except ErrorResponse, e:
        print "something went wrong! \n", e
        
def delete(argv):
    try:
        print "Are you sure you want to delete "+ argv+"?"
        answer = raw_input("Yes | No\n").lower()
        if answer == "yes":
            client.file_delete(argv)
        elif answer == "no":
            print "Abort"
        else:
            print "Wrong command. Use Yes or No"
          
    except ErrorResponse, e:
        print "something went wrong! \n", e

def download(argv):
    #TODO <--
    pass

        
if __name__ == "__main__":
    main(sys.argv[1])
