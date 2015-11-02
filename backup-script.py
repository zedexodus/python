#!/usr/bin/python2

import tarfile, os, sys, logging, datetime, re

# Get the current date for archive name
# YearMonthDay
date_stamp = datetime.date.today().strftime("%Y%m%d")

# Set directory to back up

script, directory = sys.argv

# Set the filename name of the archive using the time_stamp
filename = "%s-%s.tar.bz2" % (sys.argv[1], date_stamp)

# Set the logging level
logging.basicConfig(filename='archive.log', level = logging.DEBUG)

# Send string to log filename.
logging.info("Checking to see if " + filename + " exists")

# If the filename exists run this.
if os.path.exists(filename):
    logging.info("File already exists.")
    logging.info("Attempting add filenames to exisiting archive.")

    confirmation = str(raw_input("Do you wish to overwrite the existing archive? "))
    checkconfirmation = re.match(r'^y', str(confirmation), re.I)

    if checkconfirmation:
        print "yes"
        try:
            tar_file = tarfile.open(name=filename, mode='w:bz2')
        except:
            err = sys.exc_info()
            logging.error("Unable to open " + filename +  " for adding of additional files.")
            logging.error("Error Number: " + str(err[1].args[0]))
            logging.error("Error Message: " + err[1].args[1])
            sys.exit()
    else:
        print "no"
        logging.info("Aborting at user request.")
        sys.exit()

else:
    logging.info("Creating " + filename)
    try:
        tar_file = tarfile.open(name=filename, mode='w:bz2')
    except:
        err = sys.exc_info()
        logging.error("Unable to create " + filename)
        logging.error("Error Number: " + str(err[1].args[0]))
        logging.error("Error Message: " + err[1].args[1])
        sys.exit()

logging.info("Adding files to " + filename)

try:
    tar_file.add('.')
    tar_file.close()
except:
    err = sys.exc_info()
    logging.error("There was a critical error.")
    logging.error("Error Number: " + str(err[1].args[0]))
    logging.error("Error Message: " + err[1].args[1])
    sys.exit()
