# -*- coding: utf-8 -*-
#!python3


import sys
import re
import os
import csv
import codecs


#tests for non ASCII characters
try:
    sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)

# Writes all output
    output = open('output.csv', 'w', newline='')
    output_writer = csv.writer(output)
    output_writer.writerow(["Path", "Document_Name", "Record_ID"])

    rootdir = "I:/Cases/2013"
    for subdir, dirs, files in os.walk(rootdir):
            for file in files:
                # if not pdf.endswith(".PDF") and not pdf.endswith(".pdf"):
                #     continue
#============================================================================
# Retrieves Document Name and Record Nam
                if file:
                    path = (subdir).replace("\\", "/")
                    doc_name = file
                    record_name = re.sub("(\d\d[.]\d\d\d\w).*$", "\\1", file)

#============================================================================
#Writes records in csv file

                    output_writer.writerow([path, doc_name, record_name])

#============================================================================
    output.close()
except Exception as e:
    print("ERROR. FILE COULD NOT BE ACCESSED: " + subdir + str(files))
    print("\nPOTENTIAL INVALID ENCONDING. SEE DETAILS BELOW:\n")
    print(e)
    sys.stdout = codecs.getwriter('utf8')(sys.stdout)