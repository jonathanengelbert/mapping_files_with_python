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


#============================================================================
# Function to list all files
    def list_files(dir):
        r = []
        for root, dirs, files in os.walk(dir):
            for name in files:
                r.append(os.path.join(root, name))
        return r
#============================================================================

    print(list_files("I:/cases/2004"))

    for pdf in r:
        if not pdf.endswith(".PDF") and not pdf.endswith(".pdf"):
            continue
#============================================================================
# Retrieves Document Name and Record Name

        if pdf:
            path = (subdir).replace("\\", "/")
            doc_name = pdf
            record_name = re.sub("(\d\d[.]\d\d\d\w).*$", "\\1", pdf)
            print(pdf)

#============================================================================
#Writes records in csv file

            output_writer.writerow([path, doc_name, record_name])

#============================================================================
    output.close()
except:
    sys.stdout = codecs.getwriter('utf8')(sys.stdout)