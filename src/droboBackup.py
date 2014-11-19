import dropbox
import sys
import os
import time
from apscheduler.schedulers.background import BackgroundScheduler
from drobo import chunkedUpload, getAccessToken

def main(argv):
	
	if argv == "backup":
		startBackup(fileToBackup(sys.argv[2]))

def fileToBackup(sysArgv):
	getAccessToken()
	chunkedUpload(sysArgv)

def startBackup(argv):
	sc = BackgroundScheduler()
	sc.add_job(argv, 'interval', seconds=60)
	sc.start()
	try:
		while True:
			time.sleep(2)
	except(KeyboardInterrupt, SystemExit):
		sc.shutdown()

if __name__ == '__main__':
	main(sys.argv[1])


