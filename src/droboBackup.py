import dropbox
import sys
import os
import time
from apscheduler.schedulers.background import BackgroundScheduler
from drobo import chunkedUpload, getAccessToken, ls

def main(command):
	if command == "backup":
		startBackup()
	else:
		print("Not a valid command.")

def test():
		getAccessToken()
		fileToBackUp = chunkedUpload(sys.argv[2])
def startBackup():
	timeArgv = int(sys.argv[3])
	sc = BackgroundScheduler()
	sc.add_job(test, 'interval', seconds=timeArgv)
	sc.start()
	try:
		while True:
			time.sleep(2)
	except(KeyboardInterrupt, SystemExit):
		sc.shutdown()

if __name__ == '__main__':
	main(sys.argv[1])


