from EMAIL import *
from fra import *
from time import gmtime, strftime
import sys
import logging
import time
FILENAME = (sys.argv[2])
Subject = "NJP_NewArrival"
def main():
    url = (sys.argv[1])

    original = str(getNJP(url))

    # dumpToSave(original)
    sendemail("Started " + FILENAME,Subject)
    while True:
        #get time  to file the time
        current_time  = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        #check
        current = str(getNJP(url))
        log = ""
        if current == original:
            #ìf same write same
            log = current_time + " same"
        #if different then write email alert together with the content
        else:
            log = current_time +"\n" + FILENAME +  " OLD: \n" + original + "\nNEW: \n" + current
            sendemail(log,Subject)
            original = current
        writeToFile(log, FILENAME)
        time.sleep(5*60)

logging.basicConfig(level=logging.DEBUG, filename=FILENAME + 'error.txt')
try:
    main()

except:
    logging.exception('OPPSS')