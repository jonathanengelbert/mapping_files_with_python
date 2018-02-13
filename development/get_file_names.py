# -*- coding: utf-8 -*-
#!python3

import re
import os
import csv



#tests for non ASCII characters

# Writes all output
output = open('output.csv', 'w', newline='', encoding='utf-8')
output_writer = csv.writer(output)
output_writer.writerow(["Path", "Document_Name", "Record_ID"])

rootdir = "I:/Cases"
for subdir, dirs, files in os.walk(rootdir):

        for file in files:
            # if not pdf.endswith(".PDF") and not pdf.endswith(".pdf"):
            #     continue
#============================================================================
# Retrieves Document Name and Record Name

            path = (subdir).replace("\\", "/")
            doc_name = file
            record_name = re.sub("(\d\d[.]\d\d\d\w).*$", "\\1", file)

#============================================================================
#Writes records in csv file

            output_writer.writerow([path, doc_name, record_name])

#============================================================================
output.close()
