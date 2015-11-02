#!/usr/bin/python2

import tarfile, os, sys, logging, datetime, re

# Get the current date for archive name
# YearMonthDay
date_stamp = datetime.date.today().strftime("%Y%m%d")

# Set the file name of the archive using the time_stamp
file = "%s.tar.bz2" % date_stamp

# Set the logging level
logging.basicConfig(filename='archive.log', level = logging.DEBUG)

# Send string to log file.
logging.info("Checking to see if " + file + " exists")

# If the file exists run this.
if os.path.exists(file):
    logging.info("File already exists.")
    logging.info("Attempting add files to exisiting archive.")

    confirmation = str(raw_input("Do you wish to overwrite the existing archive? "))
    checkconfirmation = re.match(r'^y', str(confirmation), re.I)

    if checkconfirmation:
        print "yes"
        try:
            tar_file = tarfile.open(name=file, mode='w:bz2')
        except:
            err = sys.exc_info()
            logging.error("Unable to open " + file +  " for adding of additional files.")
            logging.error("Error Number: " + str(err[1].args[0]))
            logging.error("Error Message: " + err[1].args[1])
            sys.exit()
    else:
        print "no"
        logging.info("Aborting at user request.")
        sys.exit()

else:
    logging.info("Creating " + file)
    try:
        tar_file = tarfile.open(name=file, mode='w:bz2')
    except:
        err = sys.exc_info()
        logging.error("Unable to create " + file)
        logging.error("Error Number: " + str(err[1].args[0]))
        logging.error("Error Message: " + err[1].args[1])
        sys.exit()

logging.info("Adding files to " + file)

try:
    tar_file.add('.')
    tar_file.close()
except:
    err = sys.exc_info()
    logging.error("There was a critical error.")
    logging.error("Error Number: " + str(err[1].args[0]))
    logging.error("Error Message: " + err[1].args[1])
    sys.exit()
