import dropbox
import sys
import os
import time
from apscheduler.schedulers.background import BackgroundScheduler
from drobo import chunkedUpload, getAccessToken, ls

def main():
	startBackup()
	

def test():
		getAccessToken()
		fileToBackUp = chunkedUpload(sys.argv[1])
def startBackup():
	sc = BackgroundScheduler()
	sc.add_job(test, 'interval', seconds=5)
	sc.start()
	try:
		while True:
			time.sleep(2)
	except(KeyboardInterrupt, SystemExit):
		sc.shutdown()

if __name__ == '__main__':
	main()


