from EMAIL import *
from fra import *
from time import gmtime, strftime
import sys
import logging
import time
FILENAME = "FragrancenetNewArrial"
Subject = "Fragrancenet_NewArrival"
def main():
        sendemail("Started " + FILENAME,Subject)
        original = getFragNetNAList()
        while True:
                # get time  to file the time
                current_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                # check
                try:
                        # current = "\n".join(getFragNetNAList())
                        current = getFragNetNAList()
                        log = ""
                        d = set(current) - set(original)
                        if len(d) == 0 :
                                # ìf same write same
                                log = current_time + " same"
                        # if different then write email alert together with the content
                        else:
                                log = current_time + "\n" + "DIFF:\n" + "\n".join(d) #+ "\n" + "OLD: \n" +"\n".join(original) \
                                   #   + "\nNEW: \n" + "\n".join(current)
                                sendemail(log,Subject)
                                original = current
                        writeToFile(log, FILENAME)
                except:
                        logging.exception('OPPSS' + current_time)

                time.sleep(15 * 60)

logging.basicConfig(level=logging.DEBUG, filename=FILENAME + 'error.txt')
main()
