# -*- coding: utf-8 -*-
#!python3
#working directory

import sys
import re
import os
import csv
import codecs


try:
    sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)

# Writes all output
    output = open('output.csv', 'w', newline='')
    output_writer = csv.writer(output)
    output_writer.writerow(["Path", "Document_Name", "Record_ID"])

    rootdir = "I:/Cases/2004"
    for subdir, dirs, files in os.walk(rootdir):
            for pdf in files:
                if not pdf.endswith(".PDF") and not pdf.endswith(".pdf"):
                    continue
#============================================================================
# Retrieves Document Name and Record Name

                if pdf:
                    path = (subdir).replace("\\", "/")
                    doc_name = pdf
                    record_name = re.sub("(\d\d[.]\d\d\d\w).*$", "\\1", pdf)

#============================================================================
#Writes records in csv file

                    output_writer.writerow([path, doc_name, record_name])

#============================================================================
    output.close()
except:
    sys.stdout = codecs.getwriter('utf8')(sys.stdout)