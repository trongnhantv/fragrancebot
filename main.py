from EMAIL import *
from fra import *
from time import gmtime, strftime
import sys
import logging
import time
FILENAME = (sys.argv[2])

def main():
	url = (sys.argv[1])
	print("start")
	original = str(getFrag(url))
	# dumpToSave(original)
	sendemail("Started " + FILENAME)
	while True:
		# get time  to file the time
		current_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		# check
		try:
			current = str(getFrag(url))
			log = ""
			if current == original:
				# ìf same write same
				log = current_time + " same"
			# if different then write email alert together with the content
			else:
				log = current_time + "\n" + FILENAME + " OLD: \n" + original + "\nNEW: \n" + current
				sendemail(log)
				original = current
				writeToFile(log, FILENAME)
		except:
			logging.exception('OPPSS' + current_time)

		time.sleep(15 * 60)

logging.basicConfig(level=logging.DEBUG, filename=FILENAME + 'error.txt')
main()
