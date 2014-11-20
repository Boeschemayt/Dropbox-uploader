import dropbox
import sys
import os
import time
from apscheduler.schedulers.background import BackgroundScheduler
from drobo import chunkedUpload, getAccessToken, ls
client = ""

def main(command):
	if command == "backup":
		getAccessToken()
		startBackup()
	else:
		print("Not a valid command.")

#function to use as an argument in addJobbScheduler().
def backUpFile():
	fileToBackUp = chunkedUpload(sys.argv[2])
	
#This should check if the file already exist in the root folder, if the file exist,
#return True.(check if exist do not work right now..)
def checkIfExist():
	global client
	exist = True
	client = dropbox.client.DropboxClient(getAccessToken())
	items = client.metadata("/", "true")
	itemsArray = []
	itemArray = items["contents"]
	for item in itemArray:
		if sys.argv[2] in item["path"]:
			return exist
		else:
			exist = False
	return exist

# Add job to the sceduler.
def addJobToScheduler():
	timeArgv = int(sys.argv[3])
	sc = BackgroundScheduler()
	sc.add_job(backUpFile, 'interval', seconds=timeArgv)		
	sc.start()
	try:
		while True:
			time.sleep(2)
	except(KeyboardInterrupt, SystemExit):
		sc.shutdown()
		
# Main function for start the backup.
#And if the exist check works, this will remove the old file from dropbox 
#and add the new file.
def startBackup():
	if checkIfExist() == False:
		addJobToScheduler()
	else:
		client.file_delete(sys.argv[2])
		addJobToScheduler()
		

if __name__ == '__main__':
	main(sys.argv[1])


